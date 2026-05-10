def get_psp(dataset='pascal_voc', backbone='resnet101', pretrained=False, pretrained_base=True, jpu=False, root=os.path.expanduser('~/.torch/models'), **kwargs):
    acronyms = {'pascal_voc': 'voc', 'citys': 'citys'}
    from data import datasets
    model = PSPNet(datasets[dataset].NUM_CLASS, backbone=backbone, pretrained_base=pretrained_base, jpu=jpu, **kwargs)
    if pretrained:
        from model.model_store import get_model_file
        name = 'psp_%s_%s' % (backbone, acronyms[dataset])
        name = name + '_jpu' if jpu else name
        model.load_state_dict(torch.load(get_model_file(name, root=root)))
    return model