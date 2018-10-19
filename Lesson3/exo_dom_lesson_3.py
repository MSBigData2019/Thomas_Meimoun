#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:15:40 2018

@author: thomas
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

Contributors = []
User = []
Contribution = []
Location = []
Rank = []
Trash = []
NickNames = []

userID = "Thomas_Meimoun"
token = "6711aaa1d2de1d3d35865226674c8fb731fe24df"

# URL où l'on souhaite récuperer les données
URL = 'https://gist.github.com/paulmillr/2657075'

# boucle le code pour obtenir informations sur chaque contributeurs
req = requests.get(URL)
soup = BeautifulSoup(req.text, "lxml")
    
# On récupère tout le tableau
for sub_head in soup.find_all('td'):
    Contributors.append(sub_head.text) 
    
# on s'arrete à la 4 * 256 - 1 lignes 
Contributors = Contributors[:1024]

#on slice la liste principale pour récuperer chaque type d'info dans une liste
User = list(Contributors[:1024:4])
for i in range(0,256):
   Trash.append(User[i].split()) 
   NickNames.append(Trash[i][0])
   
   
Contribution = Contributors[1:1024:4]
Location = Contributors[2:1024:4]
for i in range(1,257):
    Rank.append(i)
            
#creation du DataFrame
df = pd.DataFrame({'Rank':Rank, 'User':User,'Location':Location, 'Contribution':Contribution})

            