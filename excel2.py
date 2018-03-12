#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:35:16 2018

@author: cs2017a207
"""
import xlrd
import matplotlib.pyplot as plt

file="/home/cs2017a207/Desktop/rk.xlsx"
workbook=xlrd.open_workbook(file)
f = workbook.sheet_by_index(0)
x=[f.cell_value(i,0) for i in range(f.nrows)]
y=[f.cell_value(i,0) for i in range(f.nrows)]
plt.xlabel('x')
plt.ylabel('y')
plt.title("rk")
plt.ylim(0,10)
plt.xlim(0,10)
plt.plot(x,y)
plt.show()