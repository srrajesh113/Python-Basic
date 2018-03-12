#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:13:54 2018

@author: cs2017a207
"""
import matplotlib.pyplot as plt

i=0
j=0
 plt.axis([0,10,0,20])
while(i<=10 and j<=20):
    plt.plot(i,j,'ro')
   
    i=i+1
    j=j+2
    plt.show()