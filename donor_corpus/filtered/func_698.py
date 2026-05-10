def applyPolicyVectorToNN(policyVector):
    offset = FILTER_SIZE_1[0] * FILTER_SIZE_1[1] * INPUT_SHAPE[2] * L1
    sec1 = policyVector[:offset].reshape(FILTER_SIZE_1[0], FILTER_SIZE_1[1], INPUT_SHAPE[2], L1)
    sec2 = policyVector[offset:offset + L1]
    offset += L1
    sec3 = policyVector[offset:offset + FILTER_SIZE_2[0] * FILTER_SIZE_2[1] * L1 * L2].reshape(FILTER_SIZE_2[0], FILTER_SIZE_2[1], L1, L2)
    offset += FILTER_SIZE_1[0] * FILTER_SIZE_1[1] * L1 * L2
    sec4 = policyVector[offset:offset + L2]
    offset += L2
    sec5 = policyVector[offset:offset + FINAL_DIMENSION_X * FINAL_DIMENSION_Y * L2 * L3].reshape(FINAL_DIMENSION_X * FINAL_DIMENSION_Y * L2, L3)
    offset += FINAL_DIMENSION_X * FINAL_DIMENSION_Y * L2 * L3
    sec6 = policyVector[offset:offset + L3]
    offset += L3
    sec7 = policyVector[offset:offset + L3 * L4].reshape(L3, L4)
    offset += L3 * L4
    sec8 = policyVector[offset:]
    nnFormat = []
    nnFormat.append(sec1)
    nnFormat.append(sec2)
    nnFormat.append(sec3)
    nnFormat.append(sec4)
    nnFormat.append(sec5)
    nnFormat.append(sec6)
    nnFormat.append(sec7)
    nnFormat.append(sec8)
    return nnFormat