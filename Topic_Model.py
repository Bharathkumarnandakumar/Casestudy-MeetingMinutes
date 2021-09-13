#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pycaret.datasets import get_data
import pandas as pd


# In[2]:


import os


# In[ ]:





# In[3]:


with open("C:/Users/bhara/Downloads/CASESTUDY22 (1).text") as f:
    lines = f.readlines()


# In[4]:


data= pd.DataFrame(lines)


# In[5]:


data=data.rename(columns={0:'discussion'})


# In[6]:


data


# In[ ]:





# In[7]:


import spacy


# In[8]:


from pycaret.nlp import *


# In[9]:


nlp1=setup(data,target='discussion')


# In[10]:


lda=create_model('lda')


# In[11]:


print(lda)


# In[12]:


df_lda=assign_model(lda)


# In[13]:


df_lda


# In[14]:


plot_model(lda,plot='wordcloud',topic_num='Topic 1')


# In[15]:


plot_model(lda,plot='topic_model')


# In[ ]:




