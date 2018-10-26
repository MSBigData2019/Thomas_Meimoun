#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:22:10 2018

@author: thomas
"""

import requests
from bs4 import BeautifulSoup
import numpy as np

def averg():
    pages = ['0','10','20','30','40']
    marques = ['DELL', 'HP']
    reducs = []
    avrg = []
    for marque in marques:
        for page in pages:
            pageNum = page
            pageMarque = marque
            page = requests.get(f'https://www.darty.com/nav/extra/list?p=10&s=def&cat=26055&prix_barre=dcom_BonPlan-dcom_BONPLAN&m={pageMarque}&o={pageNum}.html')
            soup = BeautifulSoup(page.text, 'html.parser')
            remises = soup.find_all('span', class_='striped_price')
            reducs += [float(remise.text[2:-1]) for remise in remises]
        avrg.append([marque, sum(reducs)/len(reducs)])
        reducs = []
    return avrg

print(averg())