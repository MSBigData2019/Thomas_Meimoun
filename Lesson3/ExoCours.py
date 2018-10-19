#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:31:02 2018

@author: thomas
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

Villes = []
Points = []
Trash = []
dist = []

Villes50 = 'http://www.linternaute.com/ville/classement/villes/population' #50 plus grandes villes de 2015
req = requests.get(Villes50)
soup = BeautifulSoup(req.text, "lxml")

for sub_head in soup.find_all('a'):
    Villes.append(sub_head.text) 

Villes = Villes[179:179+50]

for i in range(0,50):
   Trash.append(Villes[i].split()) 
   Points.append(Trash[i][0])
   
   
URL2 = 'https://fr.distance.to/Paris/Marseille'
req2 = requests.get(URL2)
soup2 = BeautifulSoup(req2.text, "lxml")

for sub_head in soup2.find_all('span'):
    dist.append(sub_head) 

#https://www.annuaire-mairie.fr/distance-paris.html