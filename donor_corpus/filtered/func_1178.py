def build(image_set, args):
    img_dir = Path(args.coco_img_path)
    assert img_dir.exists(), f'provided COCO img path {img_dir} does not exist'
    tokenizer = RobertaTokenizerFast.from_pretrained(args.text_encoder_type)
    if args.do_qa:
        if image_set == 'train':
            datasets = []
            for imset in ['train', 'minival']:
                ann_file = Path(args.vqa2_ann_path) / f'finetune_vqa2_{imset}.json'
                datasets.append(VQAv2QuestionAnswering(img_dir / 'train2014' if imset == 'train' else img_dir / 'val2014', ann_file, transforms=make_coco_transforms(image_set, cautious=True), return_masks=args.masks, return_tokens=True, tokenizer=tokenizer, ann_folder=Path(args.vqa2_ann_path)))
            return torch.utils.data.ConcatDataset(datasets)
        elif image_set == 'val':
            ann_file = Path(args.vqa2_ann_path) / f'finetune_vqa2_minival.json'
            return VQAv2QuestionAnswering(img_dir / 'val2014', ann_file, transforms=make_coco_transforms(image_set, cautious=True), return_masks=args.masks, return_tokens=True, tokenizer=tokenizer, ann_folder=Path(args.vqa2_ann_path))
        elif image_set in ['test', 'testdev', 'trainval']:
            ann_file = Path(args.vqa2_ann_path) / f'finetune_vqa2_{image_set}.json'
            return VQAv2QuestionAnswering(img_dir / 'test2015', ann_file, transforms=make_coco_transforms('val', cautious=True), return_masks=args.masks, return_tokens=True, tokenizer=tokenizer, ann_folder=Path(args.vqa2_ann_path))
        else:
            assert False, f'Unknown image set {image_set}'