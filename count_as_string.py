#!/usr/bin/env python
# coding: utf-8

# In[16]:


random_number = int(input("random whole number: "))

def collatz(x):
    if x % 2 == 0:
        x = int(x / 2)
    else:
        x = int(x * 3 + 1)
    return x
        
count = 0
while random_number != 1:
        random_number = collatz(random_number)
        count = count + 1
        print(random_number)
count_as_string = str(count)
print("It took " + count_as_string + " iterations to reach 1")


# In[ ]:





# In[ ]:




