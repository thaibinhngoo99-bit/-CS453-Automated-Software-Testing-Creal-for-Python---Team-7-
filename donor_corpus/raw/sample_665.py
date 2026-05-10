# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:36:58 2020

@author: nastavirs
"""
import numpy as np
import tensorflow as tf
def net_u(self, x, t):  
        u = self.neural_net(tf.concat([x,t],1), self.weights, self.biases)
        return u