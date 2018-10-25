#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:43:13 2018

@author: thomas
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

Infos = []
Molecule = []
Labo = []
Dosage = []
Masse = []
Consommation = []


# https://www.open-medicaments.fr/swagger-ui.html#!/medicaments/listUsingGET

URL = 'https://www.open-medicaments.fr/api/v1/medicaments?query=paracetamol&page=1&limit=100' #50 plus grandes villes de 2015
requ = requests.get(URL)
soup = BeautifulSoup(requ.text, "lxml")

reponse_object = json.loads(requ.text)

for i in range(0,len(reponse_object)):
    tr = reponse_object[i].get('denomination')
    tr = tr.split()
    tr[3].replace(',','')
    Infos.append(tr)
    Molecule.append(tr[0])
    Labo.append(tr[1])
    Dosage.append(tr[2])
    if len(tr) >= 4:
        Masse.append(tr[3])
    else:
        Masse.append(None)
    if len(tr) >= 5:
        Consommation.append(tr[4])
    else:
        Consommation.append(None)
    
#creation du DataFrame
df = pd.DataFrame({'Molecule':Molecule, 'Labo':Labo, 'Dosage':Dosage, 'Masse':Masse, 'Consommation':Consommation })

    
