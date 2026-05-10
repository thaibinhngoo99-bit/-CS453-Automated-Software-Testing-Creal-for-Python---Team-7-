def analyze_dim_red(args, test_data, cortical_result, dist_results, n_components=2):
    method = args.dimred_method
    n_states = test_data.n_states
    loc2idx = test_data.loc2idx
    idx2loc = {idx: loc for loc, idx in loc2idx.items()}
    idxs = [idx for idx in range(n_states)]
    locs = [idx2loc[idx] for idx in idxs]
    embeddings = cortical_result['embeddings']
    hiddens_ctx = cortical_result['hiddens_ctx']
    avg_hidden = cortical_result['avg_hidden']
    avg_hidden_ctx = cortical_result['avg_hidden_ctx']
    hiddens_inc_c = cortical_result['hiddens_inc_c']
    results = {}
    if method == 'pca':
        pca = PCA(n_components=n_components)
        pca_2d_embed = pca.fit_transform(embeddings)
        if args.cortical_model == 'stepwisemlp':
            pca_2d_hidd = np.zeros([hiddens_ctx.shape[0], hiddens_ctx.shape[1], n_components])
            pca_2d_avg_hidd = np.zeros([avg_hidden.shape[0], avg_hidden.shape[1], n_components])
            pca_2d_ctx_hidd = np.zeros([avg_hidden_ctx.shape[0], avg_hidden_ctx.shape[1], n_components])
            pca_2d_incong_cong = np.zeros([hiddens_inc_c.shape[0], hiddens_inc_c.shape[1], n_components])
            for h in range(hiddens_ctx.shape[0]):
                pca_2d_hidd[h, :, :] = pca.fit_transform(hiddens_ctx[h, :, :])
                pca_2d_avg_hidd[h, :, :] = pca.fit_transform(avg_hidden[h, :, :])
                pca_2d_ctx_hidd[h, :, :] = pca.fit_transform(avg_hidden_ctx[h, :, :])
                pca_2d_incong_cong[h, :, :] = pca.fit_transform(hiddens_inc_c[h, :, :])
        else:
            pca_2d_hidd = pca.fit_transform(hiddens_ctx)
            pca_2d_avg_hidd = pca.fit_transform(avg_hidden)
            pca_2d_ctx_hidd = pca.fit_transform(avg_hidden_ctx)
            pca_2d_incong_cong = pca.fit_transform(hiddens_inc_c)
        results = {'embed_2d': pca_2d_embed, 'hidd_2d': pca_2d_hidd, 'avg_hidd_2d': pca_2d_avg_hidd, 'ctx_hidd_2d': pca_2d_ctx_hidd, 'incong_cong_2d': pca_2d_incong_cong, 'grid_locations': locs, 'samples_res': cortical_result['samples_res']}
    elif method == 'mds':
        mds = MDS(n_components=n_components)
        mds_2d_embed = mds.fit_transform(embeddings)
        mds_2d_hidd = mds.fit_transform(hiddens_ctx)
        mds_2d_avg_hidd = mds.fit_transform(avg_hidden)
        mds_2d_ctx_hidd = mds.fit_transform(avg_hidden_ctx)
        mds_2d_incong_cong = mds.fit_transform(hiddens_inc_c)
        results = {'embed_2d': mds_2d_embed, 'hidd_2d': mds_2d_hidd, 'avg_hidd_2d': mds_2d_avg_hidd, 'ctx_hidd_2d': mds_2d_ctx_hidd, 'incong_cong_2d': mds_2d_incong_cong}
    elif method == 'tsne':
        tsne = TSNE(n_components=n_components)
        tsne_2d_embed = tsne.fit_transform(embeddings)
        tsne_2d_hidd = tsne.fit_transform(hiddens_ctx)
        tsne_2d_avg_hidd = tsne.fit_transform(avg_hidden)
        tsne_2d_ctx_hidd = tsne.fit_transform(avg_hidden_ctx)
        tsne_2d_incong_cong = tsne.fit_transform(hiddens_inc_c)
        results = {'embed_2d': tsne_2d_embed, 'hidd_2d': tsne_2d_hidd, 'avg_hidd_2d': tsne_2d_avg_hidd, 'ctx_hidd_2d': tsne_2d_ctx_hidd, 'incong_cong_2d': tsne_2d_incong_cong}
    return results