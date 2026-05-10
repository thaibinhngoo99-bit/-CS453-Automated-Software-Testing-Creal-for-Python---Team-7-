def analyze_test_seq(args, test_data, cortical_result, dist_results):
    import sys
    sys.path.append('..')
    data = get_loaders(batch_size=32, meta=False, use_images=True, image_dir='./images/', n_episodes=None, N_responses=args.N_responses, N_contexts=args.N_contexts, cortical_task=args.cortical_task, balanced=args.balanced)
    train_data, train_loader, test_data, test_loader, analyze_data, analyze_loader = data
    idx2loc = {idx: loc for loc, idx in test_data.loc2idx.items()}
    analyze_correct = cortical_result['analyze_correct']
    analyze_correct = np.asarray(analyze_correct).squeeze()
    hidd_t_idx = 1
    ctx0_g0 = []
    ctx0_g1 = []
    ctx0_g2 = []
    ctx0_g3 = []
    ctx1_g0 = []
    ctx1_g1 = []
    ctx1_g2 = []
    ctx1_g3 = []
    for i, batch in enumerate(analyze_loader):
        if args.cortical_task == 'face_task':
            f1, f2, ctx, y, idx1, idx2 = batch
        elif args.cortical_task == 'wine_task':
            f1, f2, ctx, y1, y2, idx1, idx2 = batch
            msg = 'analyze_test_seq is only implemented for one response, two contexts'
            assert args.N_responses == 'one' and args.N_contexts == 2, msg
            if args.N_responses == 'one':
                y = y1
        acc = analyze_correct[i][hidd_t_idx]
        ctx = ctx.cpu().numpy().squeeze()
        idx1 = idx1[0]
        idx2 = idx2[0]
        loc1 = idx2loc[idx1]
        loc2 = idx2loc[idx2]
        if ctx == 0:
            if loc1[ctx] == 0:
                ctx0_g0.append(acc)
            elif loc1[ctx] == 1:
                ctx0_g1.append(acc)
            elif loc1[ctx] == 2:
                ctx0_g2.append(acc)
            elif loc1[ctx] == 3:
                ctx0_g3.append(acc)
        elif ctx == 1:
            if loc1[ctx] == 0:
                ctx1_g0.append(acc)
            elif loc1[ctx] == 1:
                ctx1_g1.append(acc)
            elif loc1[ctx] == 2:
                ctx1_g2.append(acc)
            elif loc1[ctx] == 3:
                ctx1_g3.append(acc)
    ctx0_accs = [np.mean(ctx0_g0), np.mean(ctx0_g1), np.mean(ctx0_g2), np.mean(ctx0_g3)]
    ctx1_accs = [np.mean(ctx1_g0), np.mean(ctx1_g1), np.mean(ctx1_g2), np.mean(ctx1_g3)]
    return (ctx0_accs, ctx1_accs)