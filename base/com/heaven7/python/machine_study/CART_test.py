# coding:utf-8

## CART决策树测试.(CART 代码尚未仔细研究)

from __future__ import division  
import numpy as np  
#import scipy as sp  

from CART import DTC;

X = np.array([  
[0, 0, 0, 0, 8],
[0, 0, 0, 1, 3.5],
[0, 1, 0, 1, 3.5],
[0, 1, 1, 0, 3.5],
[0, 0, 0, 0, 3.5],
[1, 0, 0, 0, 3.5],
[1, 0, 0, 1, 3.5],
[1, 1, 1, 1, 2],
[1, 0, 1, 2, 3.5],
[1, 0, 1, 2, 3.5],
[2, 0, 1, 2, 3.5],
[2, 0, 1, 1, 3.5],
[2, 1, 0, 1, 3.5],
[2, 1, 0, 2, 3.5],
[2, 0, 0, 0, 10],
])  
  
  
y = np.array([  
[1],
[0],
[1],
[1],
[0],
[0],
[0],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
])  

prop = np.zeros((5, 1))  
prop[4] = 1  
a = DTC(X, y, prop)  
a.train()  
print a.pred([[0, 0, 0, 0, 3.0], [2, 1, 0, 1, 2]])  


