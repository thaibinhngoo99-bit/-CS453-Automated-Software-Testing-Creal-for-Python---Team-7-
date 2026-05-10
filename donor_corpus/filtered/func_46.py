def teacher_adaptor(batch, model_outputs):
    values = []
    for i in model_outputs['past_key_values']:
        values.append(i[1])
    values = torch.stack(values)
    attentions = []
    for j in model_outputs['attentions']:
        attentions.append(inv_softmax(j))
    attentions = torch.stack(attentions)
    return {'logits': model_outputs['pooler_output'], 'hidden': model_outputs['hidden_states'], 'attention': attentions, 'inputs_mask': batch['attention_mask'], 'value_relation': values, 'pooler_output': model_outputs['pooler_output']}