#!/usr/bin/env python
# coding: utf-8

# In[2]:


FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["GP2_TEXT_SUMMARISATION.py.py"]
ENTRYPOINT ["python3"]


# In[ ]:




