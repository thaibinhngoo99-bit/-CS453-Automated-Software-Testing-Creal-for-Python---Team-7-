# -*- coding: utf-8 -*-
"""
Goes through the clean dataset and determines when audio is occuring by 
measuring across a simple threshold

We use these labels for the 15, 10 5, 0dB SNR samples

Created on Sun Dec  4 15:37:11 2016

@author: brady
"""

import os
import wavio

from fe_utils import *
from config import TRAIN_CLEAN

os.chdir(TRAIN_CLEAN)

for file in os.listdir():
    if not file.endswith('.wav'):
        continue
    
    mWav = wavio.read(file)
    frame_len = int(getFrameSize(mWav.rate))
    
    mWav.data = normalizeAudio(mWav.data, mWav.sampwidth)
    frame_cnt = int(len(mWav.data)/frame_len )
    
    if (len(mWav.data)%frame_len):
        frame_cnt += 1
    
    class_list = []
    for idx in range(frame_cnt):
        if (idx == frame_cnt-1): 
            # last chunk may be truncated
            chunk = mWav.data[idx*frame_len :]
        else:
            chunk = mWav.data[idx*frame_len : (idx+1)*frame_len]
            
        if aboveFrameThreshold(chunk):
            class_list.append(1)
        else:
            class_list.append(0)
            
    filename = os.path.splitext(file)[0]
    with open(filename + '.csv', 'w') as f:
        f.write(','.join([str(c) for c in class_list]))