#!/usr/bin/python3
#*-* coding: utf-8 *-*

import matplotlib 
import matplotlib.pyplot as ply
import numpy as mp 
# how to check version  librery
# print(matplotlib.__version__)



def  function():
    xpointer = mp.array([0 , 8])
    ypointer = mp.array([0, 100])
    ply.plot(xpointer, ypointer)
    ply.show()

if __name__ == '__main__':
    function()







