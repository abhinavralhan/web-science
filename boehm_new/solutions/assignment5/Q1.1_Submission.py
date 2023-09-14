# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 00:09:52 2021

@author: Vishal Vidhani
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from dateutil import parser
import pandas as pd
import random as rd


import re

internal_urls = set()
external_urls =set()
reference_urls = set()
df = pd.DataFrame(columns=['PageCount','INTcount', 'EXTcount', 'URLfragments'])
url = "https://simple.wikipedia.org/wiki/Climate_change"


def Set_New_Url(internal_links_Count, internal_urls):
    url = ""
    if internal_links_Count != 0:
        if internal_links_Count == 1:
            index = 0
        else:
            index = rd.randint(1, int(internal_links_Count/2))
            internal_url_list = list(internal_urls)
            if r'https://' in internal_url_list[index]:
                url = internal_url_list[index]
            else:
                url = f'https://simple.wikipedia.org{internal_url_list[index]}'
    else:
        print(f'No any Internal Links in URL: {url}, so continue it with the initial URL')
        url = 'https://simple.wikipedia.org/wiki/Climate_change'
    
    return url


for pageCount in range(200):
    
    print(f'\nVisiting Url {pageCount+1}: {url}')
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, "lxml")

        #Find internal links count
        internal_links = bs.find("div",{"id" : "content"}).findAll("a" , href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))
        internal_links_Count = 0
        for link in internal_links:
            if(type(link['href']) == str):
                splitted = link['href'].split('/')
            if splitted:
                if len(splitted) >= 3:
                    if  splitted[1]=="wiki":
                        internal_urls.add(link['href'])
                        internal_links_Count += 1    
            if r"simple.wikipedia.org" in link['href']:
                internal_urls.add(link['href'])
                internal_links_Count += 1
    
        #Find reference links count
        reference_links = bs.find("div",{"id" : "content"}).findAll("a" , href=re.compile("(#[A-Za-z0-9_:()])+"))
        reference_links_Count = 0
        for link in reference_links:
            reference_urls.add(link['href'])
            reference_links_Count += 1

        #Find external links count
        external_links = bs.find("div",{"id" : "content"}).findAll("a", href=re.compile("([A-Za-z0-9_:()])+"))
        external_links_Count = 0
        for link in external_links:
            if r'/w/' not in link['href'] and link['href'] not in internal_urls and link['href'] not in reference_urls:
                external_urls.add(link['href'])
                external_links_Count += 1

        #Fetch Last Modified DateTime
        timestamp = "None"
        timestamp_text = bs.find(id="footer-info-lastmod")  
        if timestamp_text:
            res = parser.parse(timestamp_text.text, fuzzy=True)
            timestamp = (str(res).replace(" ", "T"))
            

        #print(f'Visiting link :- {url}')
        print(f'Internal Link Count:- {internal_links_Count}')
        print(f'External Link Count:- {external_links_Count}')
        print(f'Reference Link Count:- {reference_links_Count}')
        print(f'Time Stamp:- {timestamp}')    
        df = df.append({'PageCount': pageCount+1, 'INTcount' : internal_links_Count, 'EXTcount' : external_links_Count, 'URLfragments' : reference_links_Count, 'TimeStamp': timestamp}, ignore_index=True) 
        
        url = Set_New_Url(internal_links_Count, internal_urls, )        
    except:
        url = Set_New_Url(internal_links_Count, internal_urls, )        
        pass

print(df)
df.to_csv("LinkInformation.csv")

