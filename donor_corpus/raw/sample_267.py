#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent import futures

def naehere_pi_an(n):
    pi_halbe = 1
    zaehler, nenner = 2.0, 1.0
    
    for i in range(n):
        pi_halbe *= zaehler / nenner
        if i % 2:
            zaehler += 2
        else:
            nenner += 2
            
    return 2*pi_halbe


N = (
    12345678,
    1234567,
    123456,
    12345,
    1234
)

with futures.ThreadPoolExecutor(max_workers=4) as ex:       
    print(list(ex.map(naehere_pi_an, N)))
    