def eval_one_epoch_joint(model, dataloader, epoch_id, result_dir):
    np.random.seed(666)
    MEAN_SIZE = torch.from_numpy(cfg.CLS_MEAN_SIZE[0]).cuda()
    mode = 'EVAL'
    final_output_dir = os.path.join(result_dir, 'final_result', 'data')
    os.makedirs(final_output_dir, exist_ok=True)
    if True:
        roi_output_dir = os.path.join(result_dir, 'roi_result', 'data')
        refine_output_dir = os.path.join(result_dir, 'refine_result', 'data')
        rpn_output_dir = os.path.join(result_dir, 'rpn_result', 'data')
        os.makedirs(rpn_output_dir, exist_ok=True)
        os.makedirs(roi_output_dir, exist_ok=True)
        os.makedirs(refine_output_dir, exist_ok=True)
    model.eval()
    thresh_list = [0.1, 0.3, 0.5, 0.7, 0.9]
    total_recalled_bbox_list, total_gt_bbox = ([0] * 5, 0)
    total_roi_recalled_bbox_list = [0] * 5
    dataset = dataloader.dataset
    cnt = final_total = total_cls_acc = total_cls_acc_refined = total_rpn_iou = 0
    progress_bar = tqdm.tqdm(total=len(dataloader), leave=True, desc='eval')
    for data in dataloader:
        cnt += 1
        calib = data['calib']
        sample_id, pts_rect, pts_features, pts_input = (data['sample_id'], data['pts_rect'], data['pts_features'], data['pts_input'])
        batch_size = len(sample_id)
        inputs = torch.from_numpy(pts_input).cuda(non_blocking=True).float()
        input_data = {'pts_input': inputs, 'calib': calib}
        ret_dict = model(input_data)
        print(ret_dict.key())
        roi_scores_raw = ret_dict['roi_scores_raw']
        roi_boxes3d = ret_dict['rois']
        seg_result = ret_dict['seg_result'].long()
        rcnn_cls = ret_dict['rcnn_cls'].view(batch_size, -1, ret_dict['rcnn_cls'].shape[1])
        rcnn_reg = ret_dict['rcnn_reg'].view(batch_size, -1, ret_dict['rcnn_reg'].shape[1])
        anchor_size = MEAN_SIZE
        if cfg.RCNN.SIZE_RES_ON_ROI:
            assert False
        pred_boxes3d = decode_bbox_target(roi_boxes3d.view(-1, 7), rcnn_reg.view(-1, rcnn_reg.shape[-1]), anchor_size=anchor_size, loc_scope=cfg.RCNN.LOC_SCOPE, loc_bin_size=cfg.RCNN.LOC_BIN_SIZE, num_head_bin=cfg.RCNN.NUM_HEAD_BIN, get_xz_fine=True, get_y_by_bin=cfg.RCNN.LOC_Y_BY_BIN, loc_y_scope=cfg.RCNN.LOC_Y_SCOPE, loc_y_bin_size=cfg.RCNN.LOC_Y_BIN_SIZE, get_ry_fine=True).view(batch_size, -1, 7)
        if rcnn_cls.shape[2] == 1:
            raw_scores = rcnn_cls
            norm_scores = torch.sigmoid(raw_scores)
            pred_classes = (norm_scores > cfg.RCNN.SCORE_THRESH).long()
        else:
            pred_classes = torch.argmax(rcnn_cls, dim=1).view(-1)
            cls_norm_scores = F.softmax(rcnn_cls, dim=1)
            raw_scores = rcnn_cls[:, pred_classes]
            norm_scores = cls_norm_scores[:, pred_classes]
        recalled_num = gt_num = rpn_iou = 0
        if not False:
            if not cfg.RPN.FIXED:
                rpn_cls_label, rpn_reg_label = (data['rpn_cls_label'], data['rpn_reg_label'])
                rpn_cls_label = torch.from_numpy(rpn_cls_label).cuda(non_blocking=True).long()
            gt_boxes3d = data['gt_boxes3d']
            for k in range(batch_size):
                cur_gt_boxes3d = gt_boxes3d[k]
                tmp_idx = cur_gt_boxes3d.__len__() - 1
                while tmp_idx >= 0 and cur_gt_boxes3d[tmp_idx].sum() == 0:
                    tmp_idx -= 1
                if tmp_idx >= 0:
                    cur_gt_boxes3d = cur_gt_boxes3d[:tmp_idx + 1]
                    cur_gt_boxes3d = torch.from_numpy(cur_gt_boxes3d).cuda(non_blocking=True).float()
                    iou3d = iou3d_utils.boxes_iou3d_gpu(pred_boxes3d[k], cur_gt_boxes3d)
                    gt_max_iou, _ = iou3d.max(dim=0)
                    refined_iou, _ = iou3d.max(dim=1)
                    for idx, thresh in enumerate(thresh_list):
                        total_recalled_bbox_list[idx] += (gt_max_iou > thresh).sum().item()
                    recalled_num += (gt_max_iou > 0.7).sum().item()
                    gt_num += cur_gt_boxes3d.shape[0]
                    total_gt_bbox += cur_gt_boxes3d.shape[0]
                    iou3d_in = iou3d_utils.boxes_iou3d_gpu(roi_boxes3d[k], cur_gt_boxes3d)
                    gt_max_iou_in, _ = iou3d_in.max(dim=0)
                    for idx, thresh in enumerate(thresh_list):
                        total_roi_recalled_bbox_list[idx] += (gt_max_iou_in > thresh).sum().item()
                if not cfg.RPN.FIXED:
                    fg_mask = rpn_cls_label > 0
                    correct = ((seg_result == rpn_cls_label) & fg_mask).sum().float()
                    union = fg_mask.sum().float() + (seg_result > 0).sum().float() - correct
                    rpn_iou = correct / torch.clamp(union, min=1.0)
                    total_rpn_iou += rpn_iou.item()
        disp_dict = {'mode': mode, 'recall': '%d/%d' % (total_recalled_bbox_list[3], total_gt_bbox)}
        progress_bar.set_postfix(disp_dict)
        progress_bar.update()
        if True:
            roi_boxes3d_np = roi_boxes3d.cpu().numpy()
            pred_boxes3d_np = pred_boxes3d.cpu().numpy()
            roi_scores_raw_np = roi_scores_raw.cpu().numpy()
            raw_scores_np = raw_scores.cpu().numpy()
            rpn_cls_np = ret_dict['rpn_cls'].cpu().numpy()
            rpn_xyz_np = ret_dict['backbone_xyz'].cpu().numpy()
            seg_result_np = seg_result.cpu().numpy()
            output_data = np.concatenate((rpn_xyz_np, rpn_cls_np.reshape(batch_size, -1, 1), seg_result_np.reshape(batch_size, -1, 1)), axis=2)
            for k in range(batch_size):
                cur_sample_id = sample_id[k]
                calib = dataset.get_calib(cur_sample_id)
                image_shape = dataset.get_image_shape(cur_sample_id)
                save_kitti_format(cur_sample_id, calib, roi_boxes3d_np[k], roi_output_dir, roi_scores_raw_np[k], image_shape)
                save_kitti_format(cur_sample_id, calib, pred_boxes3d_np[k], refine_output_dir, raw_scores_np[k], image_shape)
                output_file = os.path.join(rpn_output_dir, '%06d.npy' % cur_sample_id)
                np.save(output_file, output_data.astype(np.float32))
        inds = norm_scores > cfg.RCNN.SCORE_THRESH
        for k in range(batch_size):
            cur_inds = inds[k].view(-1)
            if cur_inds.sum() == 0:
                continue
            pred_boxes3d_selected = pred_boxes3d[k, cur_inds]
            raw_scores_selected = raw_scores[k, cur_inds]
            norm_scores_selected = norm_scores[k, cur_inds]
            boxes_bev_selected = kitti_utils.boxes3d_to_bev_torch(pred_boxes3d_selected)
            keep_idx = iou3d_utils.nms_gpu(boxes_bev_selected, raw_scores_selected, cfg.RCNN.NMS_THRESH).view(-1)
            pred_boxes3d_selected = pred_boxes3d_selected[keep_idx]
            scores_selected = raw_scores_selected[keep_idx]
            pred_boxes3d_selected, scores_selected = (pred_boxes3d_selected.cpu().numpy(), scores_selected.cpu().numpy())
            cur_sample_id = sample_id[k]
            calib = dataset.get_calib(cur_sample_id)
            final_total += pred_boxes3d_selected.shape[0]
            image_shape = dataset.get_image_shape(cur_sample_id)
            save_kitti_format(cur_sample_id, calib, pred_boxes3d_selected, final_output_dir, scores_selected, image_shape)
    progress_bar.close()
    split_file = os.path.join(dataset.imageset_dir, '..', '..', 'ImageSets', dataset.split + '.txt')
    split_file = os.path.abspath(split_file)
    image_idx_list = [x.strip() for x in open(split_file).readlines()]
    empty_cnt = 0
    for k in range(image_idx_list.__len__()):
        cur_file = os.path.join(final_output_dir, '%s.txt' % image_idx_list[k])
        if not os.path.exists(cur_file):
            with open(cur_file, 'w') as temp_f:
                pass
            empty_cnt += 1
    ret_dict = {'empty_cnt': empty_cnt}
    avg_rpn_iou = total_rpn_iou / max(cnt, 1.0)
    avg_cls_acc = total_cls_acc / max(cnt, 1.0)
    avg_cls_acc_refined = total_cls_acc_refined / max(cnt, 1.0)
    avg_det_num = final_total / max(len(dataset), 1.0)
    ret_dict['rpn_iou'] = avg_rpn_iou
    ret_dict['rcnn_cls_acc'] = avg_cls_acc
    ret_dict['rcnn_cls_acc_refined'] = avg_cls_acc_refined
    ret_dict['rcnn_avg_num'] = avg_det_num
    for idx, thresh in enumerate(thresh_list):
        cur_roi_recall = total_roi_recalled_bbox_list[idx] / max(total_gt_bbox, 1.0)
        ret_dict['rpn_recall(thresh=%.2f)' % thresh] = cur_roi_recall
    for idx, thresh in enumerate(thresh_list):
        cur_recall = total_recalled_bbox_list[idx] / max(total_gt_bbox, 1.0)
        ret_dict['rcnn_recall(thresh=%.2f)' % thresh] = cur_recall
    if cfg.TEST.SPLIT != 'test':
        name_to_class = {'Car': 0, 'Pedestrian': 1, 'Cyclist': 2}
        ap_result_str, ap_dict = kitti_evaluate(dataset.label_dir, final_output_dir, label_split_file=split_file, current_class=name_to_class[cfg.CLASSES])
        ret_dict.update(ap_dict)
    return ap_result_str