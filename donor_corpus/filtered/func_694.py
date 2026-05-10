def convert_prediction_to_action(prediction):
    index = np.argmax(prediction[0])
    if index == 0:
        return 0
    elif index == 1:
        return 1
    elif index == 2:
        return 3
    elif index == 3:
        return 4
    return 0