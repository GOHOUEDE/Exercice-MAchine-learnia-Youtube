# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 03:51:43 2023

@author: HOME
"""

import numpy as np
import math 
import matplotlib.pyplot as plt
t=np.arange([0, 0.2 ,0.4,0.6,0.8 ,1,1.2,1.4,1.6,1.8,2])
z=np.arange(0,100,1)
D=np.array([5])
io=0.1
ho=1.5
nu=0.03
g=9.8
Ho=ho


for i in range(len(D)):
  beta=1-(2*ho/D[i])
  bo=D[i]*np.sqrt(1-beta**2)
  R=D[i]/4*(1-(beta*np.sqrt(1-beta**2)/math.acos(beta)))
  Cw=R**(1/6)/nu
  x=10+(12*ho/bo)/(3+(6*ho/bo))
  vo=Cw*np.sqrt(io*R)

  a=Cw-vo
  b=2*Cw-(x*vo)
  A=2*(a*Ho)-(ho*vo)/b
  B=Ho-A
  c=-1*g*io*b/(vo*g*ho-a**2)
  C=np.exp(c*z)
  H=A+(B*C)
  
  V=1/ho*a*(H-Ho)+vo
  #print(H)
  plt.plot(z,H,label='courbe de H pour t=0')
  plt.plot(z,V,label='courbe de V pour t=0')
  plt.xlabel('Axe de z')
  plt.ylabel(' H et V')
  # Ajouter une légende
  plt.legend()
  plt.show()