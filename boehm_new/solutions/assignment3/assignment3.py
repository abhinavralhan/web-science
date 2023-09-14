#!/usr/bin/env python
# coding: utf-8

# In[31]:


import requests

URL = 'https://en.wikipedia.org/w/rest.php/v1/page/boehm'

getRequest = requests.get(url = URL)

jsonFormat = getRequest.json()

articleId = jsonFormat['id']
articleTitle = jsonFormat['title']
articleTimeStamp = jsonFormat['latest']['timestamp']


API_ENDPOINT = "https://pastebin.com/api/api_post.php"
  

API_KEY = "F5aT5BB8R7QV0cFg22_ZzIWBGnSBMRxi"
  
# your source code here
source_code = str(articleId) + '\n' + articleTitle + '\n'+ articleTimeStamp

  
# data to be sent to api
data = {'api_dev_key':API_KEY,
        'api_option':'paste',
        'api_paste_code':source_code,
        'api_paste_format':'python'}
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
  
# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)


httpHeader=requests.get(pastebin_url)
HeaderValue = httpHeader.headers

file = open("boehm.txt", "w") 
file.write(str(HeaderValue))
file.close()



# In[39]:





# In[ ]:




