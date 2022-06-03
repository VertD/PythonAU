from math import *

import random

S = 1*pi/2

def function(x):
    return sin(x)

count = 0
m=0
n = int(input())
while count < n:
    x_coord = random.uniform(0,pi/2)
    y_coord = random.uniform(0,1)
    if y_coord < function(x_coord):
        m+=1
    count+=1
print(S*(m/n))


