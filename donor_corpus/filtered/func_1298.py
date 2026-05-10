def merge_overlapping_boxes(mapping, boxes, threshold=0.8):
    """Merge boxes which have an overlap greater than threshold.

  TODO(rbharath): This merge code is terribly inelegant. It's also quadratic
  in number of boxes. It feels like there ought to be an elegant divide and
  conquer approach here. Figure out later...
  """
    num_boxes = len(boxes)
    outputs = []
    for i in range(num_boxes):
        box = boxes[0]
        new_boxes = []
        new_mapping = {}
        contained = False
        for output_box in outputs:
            new_mapping[output_box] = mapping[output_box]
            if compute_overlap(mapping, box, output_box) == 1:
                contained = True
        if contained:
            continue
        unique_box = True
        for merge_box in boxes[1:]:
            overlap = compute_overlap(mapping, box, merge_box)
            if overlap < threshold:
                new_boxes.append(merge_box)
                new_mapping[merge_box] = mapping[merge_box]
            else:
                unique_box = False
                merged = merge_boxes(box, merge_box)
                new_boxes.append(merged)
                new_mapping[merged] = list(set(mapping[box]).union(set(mapping[merge_box])))
        if unique_box:
            outputs.append(box)
            new_mapping[box] = mapping[box]
        boxes = new_boxes
        mapping = new_mapping
    return (outputs, mapping)