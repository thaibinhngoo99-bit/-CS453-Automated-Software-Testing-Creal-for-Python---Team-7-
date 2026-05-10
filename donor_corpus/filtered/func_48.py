def predict(model, teacher_model, eval_dataset, step, device, STUDENT, BATCH_SIZE, eval_metric='cosine_similarity', feedback=True):
    """
    model = student_model
    teacher_model = labse
    eval_dataset = num of dev set samples to test model on per callback
    device = cuda or cpu
    student = switch or !switch
    eval_metric = metric to evaluate the model - mse or cosine_similarity
    """
    model.eval()
    student_logits = []
    teacher_logits = []
    batch_counts = []
    batch_n_dropped = []
    batch_route_prob = []
    dataloader = DataLoader(eval_dataset, batch_size=BATCH_SIZE)
    print('Running callback function on {} dev set samples...'.format(len(eval_dataset)))
    for batch in dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        with torch.no_grad():
            model_outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            logits_S = model_outputs['pooler_output']
            logits_T = teacher_model(input_ids=input_ids, attention_mask=attention_mask)['pooler_output']
            cpu_logits_S = logits_S.detach().cpu()
            cpu_logits_T = logits_T.detach().cpu()
            if STUDENT == 'switch' and feedback == True:
                counts = model_outputs['counts'].detach().cpu()
                n_dropped = model_outputs['n_dropped']
                route_prob = model_outputs['route_prob'].detach().cpu()
        for i in range(len(cpu_logits_S)):
            student_logits.append(cpu_logits_S[i].numpy())
            teacher_logits.append(cpu_logits_T[i].numpy())
        if STUDENT == 'switch' and feedback == True:
            for i in range(len(counts)):
                batch_counts.append(counts[i].numpy())
                batch_n_dropped.append(n_dropped[i])
                batch_route_prob.append(route_prob[i].numpy())
    model.train()
    student_logits = np.array(student_logits)
    teacher_logits = np.array(teacher_logits)
    if eval_metric == 'cosine_similarity':
        similarities = np.diag(cosine_similarity(student_logits, teacher_logits))
        print('Average cosine similarity for these samples: ', np.mean(similarities))
    if eval_metric == 'mse':
        mse_error = mean_squared_error(student_logits, teacher_logits)
        print('Average mean squared error for these samples: ', mse_error)
    if STUDENT == 'switch' and feedback == True:
        switch_counts = np.array(batch_counts)
        switch_n_dropped = np.array(batch_n_dropped)
        switch_route_prob = np.array(batch_route_prob)
        print('SWITCH BEHAVIOUR:')
        print('Counts Shape: \n', switch_counts.shape)
        print('Counts: \n', switch_counts)
        print('N_dropped: \n', switch_n_dropped)
        print('Route Prob: \n', switch_route_prob)
    return torch.Tensor([np.mean(similarities)])