#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


#     #  Dimension Array's

# In[2]:


a = np.arange(20)
a


# In[3]:


b = np.arange(14).reshape(2,7)
b


# In[4]:


c= np.arange(24).reshape(2,3,4)
c


#     # Multidimension

# In[5]:


d = np.array([[2,4],[4,5]])
d


#     # Minimum Dimension

# In[6]:


e = np.array([0,1,2,3,4,5,6], ndmin=4)
e


#     # Dtype Perameters

# In[7]:


f = np.array([1,2,3,4,5], dtype = complex)
f


#     # Ndim

# In[8]:


a = np.array([(2,3,4),(5,6,7)])
a.ndim


#     # Itemsize

# In[9]:


b = np.array([(1,2,3)])
b.itemsize


#     # D-type

# In[10]:


a.dtype


#     # Size

# In[11]:


a.size


#     # Shape

# In[12]:


a.shape


#     # Silicing

# In[13]:


a = np.array([(1,2,3,4),(5,6,7,8)])
print(a[0:,1])


#     # Boolean 

# In[14]:


bool_arr = np.array([1, .5, 0, 'aa', ''], dtype = bool)
print(bool_arr)


#     # Multidimension

# In[15]:


a= np.array([(2,3),(4,5),(7,8)])
a[0:2,1]


#     # Linearly Spacing

# In[16]:


a = np.linspace(1,7,9)
print(a)


#     # Minimum Values

# In[17]:


a = np.array([39,94,57])
a.min()


#     # Maximum Values

# In[18]:


a.max()


#     # Values Sum

# In[19]:


a = np.array([192,168,255])
a.sum()


#     # Get a Square-Root

# In[20]:


np.sqrt(a)


#     # Subtracting Metrix

# In[21]:


x= np.array([(1,2,3),(3,4,5)])
y = np.array([(5,6,7),(6,7,8)])
x-y


#     # ADDING Matrix

# In[22]:


x+y


#     # Multiply Matrix

# In[23]:


x*y


#     # Divide Matrix

# In[24]:


x/y


#     # Vertical Stack

# In[25]:


np.vstack((x,y))


#      # Horizontal Stack

# In[26]:


np.hstack((x,y))


#     # Contiguous Flattened Array

# In[27]:


x.ravel()


#     # Odd Number Filtering

# In[28]:


arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
arr[arr % 2 == 1 ]


#     # Zero Array

# In[29]:


arrayid = np.zeros(3)
arrayid


#     # 2D Zero Matrix

# In[30]:


b = np.zeros((2,3))
b


#     # Logspace Array

# In[31]:


A = np.logspace(3,8,num=10,base= 1000.0, dtype=float)
A


#     # Random Number Generator

# In[32]:


np.random.rand(3,3)


#     # Random Number Generator in a Given Range

# In[33]:


np.random.randint(3, size= 5)


# In[34]:


np.random.randint(30, size= (2,2))


#     # Identity Matrix

# In[35]:


np.identity(3)


#     # Digonal Array

# In[36]:


np.diag(np.arange(2,5,5))


#     # Numpy Indexing

# In[37]:


g = np.array([1,2,3,4,5,6])
g[[2,5]]


#     # Last Value

# In[38]:


g[-1]


#     # Joining and Stacking Araays

# In[39]:


Arr1= np.array([[1,9,2],[1,6,8]])
Arr2 = np.array([[2,5,5],[8,4,2]])
Arr1+Arr2


# In[40]:


np.hstack((Arr1,Arr2))


# In[41]:


np.vstack((Arr1,Arr2))


#     # Concatinating

# In[42]:


np.concatenate((Arr1, Arr2))


#     # Append Value

# In[43]:


np.append(Arr1,Arr2, axis = 1)


#     # Trignomatry

# In[44]:


np.sin(Arr1)


# In[45]:


np.cos(Arr2)


# In[46]:


np.tan(Arr1)


# In[47]:


np.log(Arr2)


# In[48]:


np.exp(Arr1)


# In[49]:


np.sqrt(Arr2)


# In[50]:


np.power(Arr1, 5)


# In[ ]:




