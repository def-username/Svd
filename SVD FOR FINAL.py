#!/usr/bin/env python
# coding: utf-8

# In[16]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import array
import math 
from scipy.linalg import svd
# define a matrix
A = array([[-math.cos(45*3.14/180),math.cos(45*3.14/180),math.cos(45*3.14/180),-math.cos(45*3.14/180)],
           [math.sin(45*3.14/180),math.sin(45*3.14/180),math.sin(45*3.14/180),math.sin(45*3.14/180)],
           [1,-1,1,-1]])
print(A)
#SVD
U, s, VT = svd(A)
print("U matrix = ")
print(U)
print("S matrix = ")
print(s)
print("VT matrix = ")
print(VT)


# In[ ]:





# In[ ]:




# In[17]:


import numpy as np
newS=np.array([[1/2,0,0],[0,1/1.4,0],[0,0,1/1.4],[0,0,0]])
X=np.matmul(VT.transpose(),newS)
print(X)
L=np.matmul(X,U.transpose())
print(L)

Forces=np.array([[50],[50],[0]])
print(Forces)
Final=np.matmul(X,Forces)
Final


# In[ ]:




