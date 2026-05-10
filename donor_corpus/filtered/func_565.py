def drawPred(classId, conf, left, top, right, bottom):
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0))
    label = '%.2f' % conf
    if classes:
        assert classId < len(classes)
        label = '%s:%s' % (classes[classId], label)
    labelSize, baseLine = cv2.getTextSize(label, font, 0.5, 1)
    top = max(top, labelSize[1])
    cv2.putText(frame, label, (left, top), font, 1, (0, 255, 0), 2)