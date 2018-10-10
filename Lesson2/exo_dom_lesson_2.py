#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:01:21 2018

@author: tmeimoun
"""

import requests
from bs4 import BeautifulSoup
 
Value  = []
Name   = []
Header = []

URL = 'https://www.reuters.com/finance/stocks/financial-highlights/LVMH.PA'

req = requests.get(URL)
#req = requests.get('https://www.reuters.com/finance/stocks/financial-highlights/AIR.PA')
#req = requests.get('https://www.reuters.com/finance/stocks/financial-highlights/DANO.PA')

soup = BeautifulSoup(req.text, "lxml")

# 'firstHeading'
 
for sub_heading in soup.find_all('td'):
    Value.append(sub_heading.text)
    
for sub_heading in soup.find_all('th'):
    Name.append(sub_heading.text)
    
for sub_heading in soup.find_all('span'):
    Header.append(sub_heading.text)
    
Qending = Value[1]
ValQend = Value[3].replace(",","") #
#Mean    = Name[2]
NameStock = Header[4].strip()
PriceStock = Header[5].strip() #
ValueChange = Header[8].strip()[:6]
Change = str(round(float(Header[12].replace("(","").replace(")","").replace("%","")) / 100, 3))
ShareOwned =  Value[293]
ValueShareOwn = Value[294].replace("%","") #
DivYld = Value[89]
Compagny = Name[7]
Industry = Name[8]
Sector   = Name[9]

CompagnyVal = Value[90] #
IndustryVal = Value[91] #
SectorVal   = Value[92] #

print ("about " + NameStock)
print ("Mean of the " + Qending + " : " + ValQend)
print (NameStock[:8] + " Price : " + PriceStock)
print (NameStock[:8] + " change : " + Change + "%")
print ("Institutionnal " + ShareOwned  + " : " + ValueShareOwn)
print (DivYld + " \n"   + 
       Compagny + " : "  + CompagnyVal + " \n" + 
       Sector + " : "    + SectorVal   + " \n" + 
       Industry + " : "  + IndustryVal )


# tout le reste c'est des string, peut être faire une liste avec le snoms à la main ?
# seulement créer une boucle qui change uniquement le nom des titres

#string = IndustryVal.strip()[:-1]
#Test = float(string.replace(',','.'))
