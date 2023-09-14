#!/usr/bin/env python
# coding: utf-8

# In[10]:


import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)
sock.bind(server_address)

sock.listen(1)
while True:
    print("Waiting...")
    client,addr = sock.accept()
    print("HOST " + socket.getfqdn() + " Established connection with ",addr)
    try:
        client.send(bytes('Thank you for connecting','utf-8'))
    except:
        print("Exited by User")
    client.close()
    break
sock.close()


# In[ ]:





# In[ ]:




