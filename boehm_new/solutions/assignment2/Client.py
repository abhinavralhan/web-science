#!/usr/bin/env python
# coding: utf-8

# In[7]:


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 12345))

try:
    while True:
        data=client.recv(1024)
        print(str(data))
        break
except KeyboardInterrupt:
    print("Exited by user")
client.close()


# In[ ]:





# In[ ]:




