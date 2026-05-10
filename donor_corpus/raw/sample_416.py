import cv2
import sys
import os
import numpy as np
import time

# Initialize the parameters
confThreshold = 0.5  # Confidence threshold
nmsThreshold = 0.4   # Non-maximum suppression threshold
inpWidth = 416       # Width of network's input image
inpHeight = 416      # Height of network's input image
starting_time = 0
frame_id = 0
font = cv2.FONT_HERSHEY_PLAIN

# Load names of classes
classesFile = "coco.names"
classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# Give the configuration and weight files for the model and load the network using them.
modelConfiguration = "yolov3.cfg"
modelWeights = "yolov3.weights"
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

inputFile = "presen_T.mp4"
inputFile2 = "presen_R.mp4"
outputFile = "yolo_out_py.avi"

# Open the video file
if not os.path.isfile(inputFile):
    print("Input video file ", inputFile, " doesn't exist")
    sys.exit(1)
cap = cv2.VideoCapture(inputFile)
cap2 = cv2.VideoCapture(inputFile2)
outputFile = inputFile[:-4] + "_yolo_out_py.avi"

# Get the video writer initialized to save the output video
vid_writer = cv2.VideoWriter(outputFile, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30,
                            (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

# Get the names of the output layers
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Draw the predicted bounding box
def drawPred(classId, conf, left, top, right, bottom):
    # Draw a bounding box.
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0))
    label = '%.2f' % conf

    # Get the label for the class name and its confidence
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    # Display the label at the top of the bounding box
    labelSize, baseLine = cv2.getTextSize(label, font, 0.5, 1)
    top = max(top, labelSize[1])
    cv2.putText(frame, label, (left, top), font, 1, (0, 255, 0), 2)

# Remove the bounding boxes with low confidence using non-maxima suppression
def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    # Scan through all the bounding boxes output from the network and keep only the
    # ones with high confidence scores. Assign the box's class label as the class with the highest score.
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # Perform non maximum suppression to eliminate redundant overlapping boxes with
    # lower confidences.
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        drawPred(classIds[i], confidences[i], left, top, left + width, top + height)

# Main
while True:
    # get frame from the video
    hasFrame, frame = cap.read()
    hasFrame2, frame2 = cap2.read()

    frame = cv2.resize(frame, dsize=(600, 402))
    frame2 = cv2.resize(frame2, dsize=(600, 402))

    cv2.imshow("Camera", frame)
    cv2.imshow("Thermal_Camera", frame2)
    # Stop the program if reached end of video
    if not hasFrame:
        print("Done processing !!!")
        cv2.waitKey(3000)
        break

    # Create a 4D blob from a frame.
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)

    # Sets the input to the network
    net.setInput(blob)

    # Runs the forward pass to get output of the output layers
    outs = net.forward(getOutputsNames(net))

    # Remove the bounding boxes with low confidence
    postprocess(frame, outs)

    # Print the FPS
    current_time = time.time()
    sec = current_time - starting_time
    starting_time = current_time
    fps = 1 / (sec)
    str2 = "FPS : %0.1f" % fps
    # cv2.putText(frame, str2, (10, 50), font, 2, (0, 255, 0), 2)

    # Write the frame with the detection boxes
    vid_writer.write(frame.astype(np.uint8))

    # CAMERA RESULT
    cv2.imshow("CAMERA_Detection", frame)


    img2 = None
    fast = cv2.FastFeatureDetector_create(30)
    fast.setNonmaxSuppression(0)
    kp = fast.detect(frame2, None)
    img2 = cv2.drawKeypoints(frame2, kp, img2, (0, 255, 255))
    # cv2.imshow("THERMAL", img2)


    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    car_prediction = 30
    lower_white = np.array([0, 0, 255 - car_prediction], dtype=np.uint8)
    upper_white = np.array([255, car_prediction, 255], dtype=np.uint8)
    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame2, frame2, mask=mask_white)
    # cv2.imshow("THERMAL_CAR", res)


    res2 = None
    res2 = res
    igray = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
    iret, ibinary = cv2.threshold(igray, 127, 255, cv2.THRESH_BINARY)
    contours, hierachy = cv2.findContours(ibinary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        cv2.drawContours(res2, [contours[i]], 0, (255, 255, 255), 2)
        cv2.putText(res2, "car", tuple(contours[i][0][0]), font, 1, (0, 255, 0), 1)
    # cv2.imshow("THERMAL_CONTOUR", res2)


    # THERMAL PROCESSING RESULT
    dst = cv2.addWeighted(res2, 1, frame2, 1, 0)
    #cv2.imshow('THERMAL_RES',dst)
    #cv2.imshow("THERMAL",frame2)

    # FINAL RESULT
    dst2 = cv2.addWeighted(res2, 1, frame, 1, 0)
    cv2.imshow("RESULT",dst2)


    # End the video with "Esc"
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()