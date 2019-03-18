# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:52:51 2019

@author: jianfengsong
"""

import numpy as np
import math
import matplotlib.pyplot as plt
blocking_pro=list()
p=np.arange(0,5,0.1)
c=[5,7,9]
def out(p,c):
    sum_=0
    for a in range(c+1):
        sum_+=pow(p,a)/math.factorial(a)
    out=(pow(p,c)/math.factorial(c))/sum_
    return out
cont=0
for a in c:
    blocking_pro.append([])
    for b in p:
        blocking_pro[cont].append(out(b,a))
    cont+=1
plt.plot(p,blocking_pro[0],'r--',label='c=5')
plt.plot(p,blocking_pro[1],'bs',label='c=7')
plt.plot(p,blocking_pro[2],'g^',label='c=9')
plt.ylabel('Blocking Prob')
plt.xlabel('p')
plt.title('HW6')
plt.legend()
plt.show()
out_3=100
c=0
p=500
while  out_3>=0.001:
    out_3=out(p,c)
#    print(out_3)
    c+=1
       