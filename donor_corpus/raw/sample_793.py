#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:19:34 2019

@author: sercangul
"""

from math import erf

std = 10
h1 = 80
h2 = 60
mean = 70

def N(mean, std, x):
    return 0.5 + 0.5 * erf((x-mean)/(std* 2**0.5))

print (round(((1 - N(mean,std,h1))*100),2))
print (round(((1 - N(mean,std,h2))*100),2))
print (round(((N(mean,std,h2)*100)),2))