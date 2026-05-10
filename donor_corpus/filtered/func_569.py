def analyze_cortical(model, test_data, analyze_loader, args):
    n_states = test_data.n_states
    loc2idx = test_data.loc2idx
    idx2loc = {idx: loc for loc, idx in loc2idx.items()}
    idxs = [idx for idx in range(n_states)]
    idx2tensor = test_data.idx2tensor
    model.eval()
    face_embedding = model.face_embedding
    face_embedding.to(args.device)
    embeddings = []
    if args.cortical_model == 'stepwisemlp':
        hiddens = [[] for i in range(2)]
        hiddens_cong = [[] for i in range(2)]
        hiddens_incong = [[] for i in range(2)]
        hiddens_ctxs = [[[] for j in range(args.N_contexts)] for i in range(2)]
    else:
        hiddens = []
        hiddens_incong = []
        hiddens_cong = []
        hiddens_ctxs = [[] for i in range(args.N_contexts)]
    idxs1 = []
    idxs2 = []
    idxs1_ctxs = [[] for i in range(args.N_contexts)]
    idxs2_ctxs = [[] for i in range(args.N_contexts)]
    samples = []
    samples_ctxs = [[] for i in range(args.N_contexts)]
    samples_cong = []
    samples_incong = []
    with torch.no_grad():
        for idx in range(n_states):
            face_tensor = idx2tensor[idx].unsqueeze(0).to(args.device)
            embedding = face_embedding(face_tensor)
            embedding = embedding.cpu().numpy()
            embeddings.append(embedding)
        embeddings = np.concatenate(embeddings, axis=0)
        for batch in analyze_loader:
            if args.cortical_task == 'face_task':
                f1, f2, ctx, out, idx1, idx2 = batch
            elif args.cortical_task == 'wine_task':
                f1, f2, ctx, out1, out2, idx1, idx2 = batch
            idx1 = idx1[0]
            idx2 = idx2[0]
            samples.append(batch)
            (x1, y1), (x2, y2) = (idx2loc[idx1], idx2loc[idx2])
            f1 = f1.to(args.device)
            f2 = f2.to(args.device)
            ctx = ctx.to(args.device)
            grid_angle = np.arctan2(y2 - y1, x2 - x1)
            phi = np.sin(2 * grid_angle)
            if np.abs(phi) < 1e-05:
                cong = 0
            else:
                cong = np.sign(phi)
            y_hat, out = model(f1, f2, ctx)
            if args.order_ctx == 'first':
                f1_ind = 1
                f2_ind = 2
            elif args.order_ctx == 'last':
                f1_ind = 0
                f2_ind = 1
            if args.cortical_model == 'stepwisemlp':
                out1, out2 = out
                out1 = out1.cpu().numpy()
                out2 = out2.cpu().numpy()
                hiddens[0].append(out1)
                hiddens[1].append(out2)
                hiddens_ctxs[0][ctx].append(out1)
                hiddens_ctxs[1][ctx].append(out2)
            else:
                out = out.cpu().numpy()
                hiddens.append(out)
                hiddens_ctxs[ctx].append(out)
            ctx = ctx[0].cpu().numpy()
            idxs1.append(idx1)
            idxs2.append(idx2)
            idxs1_ctxs[ctx].append(idx1)
            idxs2_ctxs[ctx].append(idx2)
            samples_ctxs[ctx].append(batch)
            if cong == 1 and (ctx == 0 or ctx == 1):
                if args.cortical_model == 'stepwisemlp':
                    hiddens_cong[0].append(out1)
                    hiddens_cong[1].append(out2)
                else:
                    hiddens_cong.append(out)
                samples_cong.append(batch)
            elif cong == -1 and (ctx == 0 or ctx == 1):
                if args.cortical_model == 'stepwisemlp':
                    hiddens_incong[0].append(out1)
                    hiddens_incong[1].append(out2)
                else:
                    hiddens_incong.append(out)
                samples_incong.append(batch)
    hiddens = np.asarray(hiddens).squeeze()
    hiddens_incong = np.asarray(hiddens_incong).squeeze()
    hiddens_cong = np.asarray(hiddens_cong).squeeze()
    if args.cortical_model == 'stepwisemlp':
        hiddens_ctx = np.concatenate(np.asarray(hiddens_ctxs).squeeze(), axis=1)
        hiddens_inc_c = np.concatenate((hiddens_incong, hiddens_cong), axis=1)
    else:
        hiddens_ctx = np.concatenate(hiddens_ctxs, axis=0).squeeze()
        hiddens_inc_c = np.concatenate((hiddens_incong, hiddens_cong), axis=0)
    if args.cortical_model == 'rnn' or args.cortical_model == 'rnncell':
        hiddens_ctx = hiddens_ctx[:, -1, :]
        hiddens_inc_c = hiddens_inc_c[:, -1, :]
    samples_inc_c = np.concatenate((samples_incong, samples_cong), axis=0)
    if args.cortical_model == 'stepwisemlp':
        avg_hidden = np.zeros([2, n_states, hiddens.shape[-1]])
        avg_hidden_ctxs = np.zeros([2, args.N_contexts, n_states, hiddens.shape[-1]])
    else:
        avg_hidden = np.zeros([n_states, hiddens.shape[-1]])
        avg_hidden_ctxs = np.zeros([args.N_contexts, n_states, hiddens.shape[-1]])
    if args.cortical_model == 'rnn' or args.cortical_model == 'rnncell':
        hiddens_ctxs = np.asarray(hiddens_ctxs).squeeze()
        for f in range(n_states):
            temp1 = [np.expand_dims(hiddens[i, f1_ind, :], axis=0) for i, idx1 in enumerate(idxs1) if idx1 == f]
            temp2 = [np.expand_dims(hiddens[i, f2_ind, :], axis=0) for i, idx2 in enumerate(idxs2) if idx2 == f]
            if len(temp1 + temp2) > 1:
                avg_hidden[f] = np.concatenate(temp1 + temp2, axis=0).mean(axis=0)
            for ctx in range(args.N_contexts):
                temp1_ctxs = [hiddens_ctxs[ctx, i, f1_ind, :] for i, idx1 in enumerate(idxs1_ctxs[ctx]) if idx1 == f]
                temp2_ctxs = [hiddens_ctxs[ctx, i, f2_ind, :] for i, idx2 in enumerate(idxs2_ctxs[ctx]) if idx2 == f]
                if len(temp1_ctxs + temp2_ctxs) > 1:
                    m = np.zeros([2, hiddens_ctxs.shape[-1]])
                    m[0] = np.mean(np.asarray(temp1_ctxs), axis=0)
                    m[1] = np.mean(np.asarray(temp2_ctxs), axis=0)
                    avg_hidden_ctxs[ctx, f, :] = np.mean(m, axis=0)
        avg_hidden_ctx = np.concatenate(avg_hidden_ctxs, axis=0)
    elif args.cortical_model in ['mlp', 'mlp_cc']:
        for f in range(n_states):
            temp = [hiddens[i, :] for i, (idx1, idx2) in enumerate(zip(idxs1, idxs2)) if (idx1 == f) | (idx2 == f)]
            if len(temp) > 1:
                avg_hidden[f] = np.mean(temp, axis=0)
            for ctx in range(args.N_contexts):
                temp_ctxs = [hiddens_ctxs[ctx][i] for i, (idx1, idx2) in enumerate(zip(idxs1_ctxs[ctx], idxs2_ctxs[ctx])) if (idx1 == f) | (idx2 == f)]
                if len(temp_ctxs) > 1:
                    avg_hidden_ctxs[ctx, f, :] = np.mean(temp_ctxs, axis=0)
        avg_hidden_ctx = np.concatenate(avg_hidden_ctxs, axis=0)
    elif args.cortical_model == 'stepwisemlp':
        hiddens_ctxs = np.asarray(hiddens_ctxs).squeeze()
        for f in range(n_states):
            temp1 = [hiddens[0, i, :] for i, idx1 in enumerate(idxs1) if idx1 == f]
            temp2 = [hiddens[1, i, :] for i, idx2 in enumerate(idxs2) if idx2 == f]
            if len(temp1) > 1:
                avg_hidden[0, f, :] = np.mean(temp1, axis=0)
            if len(temp2) > 1:
                avg_hidden[1, f, :] = np.mean(temp2, axis=0)
            for ctx in range(args.N_contexts):
                temp1_ctxs = [hiddens_ctxs[0, ctx, i, :] for i, idx1 in enumerate(idxs1_ctxs[ctx]) if idx1 == f]
                temp2_ctxs = [hiddens_ctxs[1, ctx, i, :] for i, idx2 in enumerate(idxs2_ctxs[ctx]) if idx2 == f]
                if len(temp1_ctxs) > 1:
                    avg_hidden_ctxs[0, ctx, f, :] = np.mean(temp1_ctxs, axis=0)
                if len(temp2_ctxs) > 1:
                    avg_hidden_ctxs[1, ctx, f, :] = np.mean(temp2_ctxs, axis=0)
        avg_hidden_ctx = np.concatenate(avg_hidden_ctxs, axis=1)
    samples_res = {'samples': samples, 'samples_ctxs': samples_ctxs, 'samples_inc_c': samples_inc_c}
    results = {'samples_res': samples_res, 'idxs1': idxs1, 'idxs2': idxs2, 'embeddings': embeddings, 'hiddens_ctx': hiddens_ctx, 'hiddens_ctxs': hiddens_ctxs, 'avg_hidden': avg_hidden, 'avg_hidden_ctx': avg_hidden_ctx, 'avg_hidden_ctxs': avg_hidden_ctxs, 'hiddens_inc_c': hiddens_inc_c}
    return results