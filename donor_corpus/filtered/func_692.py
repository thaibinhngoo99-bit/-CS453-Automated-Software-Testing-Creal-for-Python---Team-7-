def visualize(featureVector):
    regularImage = featureVector[0, :FRAME_SIZE].reshape((210, 160))
    differenceImage = featureVector[0, FRAME_SIZE:].reshape((210, 160))
    PLT.imshow(regularImage)
    PLT.show()
    PLT.imshow(differenceImage)
    PLT.show()