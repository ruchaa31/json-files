#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import json


f = open(r"iris.csv", newline='')

reader = csv.DictReader(f, fieldnames=("sepal_length", "sepal_width", "petal_length", "petal_width", "species"))


out = json.dumps([row for row in reader])
print("JSON parsed!")


f = open("parsed.json", "w", newline='')
f.write(out)

print("JSON saved!")


# In[ ]:





# In[ ]:




