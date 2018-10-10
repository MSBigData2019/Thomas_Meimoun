#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:01:21 2018

@author: tmeimoun
"""

import requests
from bs4 import BeautifulSoup

# balises recherchées
balise = ['td', 'th', 'span']

#valeurs recherchées
Stocks = ['LVMH.PA', 'AIR.PA', 'DANO.PA']

Value  = []
Name   = []
Header = []

# pattern commun de l'url pour tous les titres
URLbeg = 'https://www.reuters.com/finance/stocks/financial-highlights/'

# boucle le code pour obtenir informations sur chaque titre
for Titre in Stocks:
    URL = URLbeg + Titre   
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, "lxml")
    
    # récupération des balises dans différentes listes
    for ba in balise:
        for sub_head in soup.find_all(ba):
            if ba == 'td' :
                Value.append(sub_head.text) 
            elif ba == 'th' :
               Name.append(sub_head.text) 
            else : # ba == 'span':
               Header.append(sub_head.text)
               
    # recherche des valeurs souhaitées 

    Qending = Value[1]
    ValQend = Value[3].replace(",","") #
    DivYld = Value[89]
    CompagnyVal = Value[90] #
    IndustryVal = Value[91] #
    SectorVal   = Value[92] #
    ShareOwned =  Value[293]
    ValueShareOwn = Value[294].replace("%","") #
    
    Compagny = Name[7]
    Industry = Name[8]
    Sector   = Name[9] 
    
    NameStock = Header[4].strip()
    PriceStock = Header[5].strip() #
    ValueChange = Header[8].strip()[:6]
    Change = (Header[12].replace("(","").replace(")","").replace("%","")).strip()
    
    # affichage des résultats
    print ("about " + NameStock)
    print ("Mean of the " + Qending + " : " + ValQend)
    print (NameStock[:8] + " Price : " + PriceStock)
    print (NameStock[:8] + " change : " + Change + "%")
    print ("Institutionnal " + ShareOwned  + " : " + ValueShareOwn)
    print (DivYld + ": \n"   + 
           Compagny + " : "  + CompagnyVal + " \n" + 
           Sector + " : "    + SectorVal   + " \n" + 
           Industry + " : "  + IndustryVal )
    print ('======================================================')
    

# tout le reste c'est des string, peut être faire une liste avec le snoms à la main ?
# seulement créer une boucle qui change uniquement le nom des titres

#string = IndustryVal.strip()[:-1]
#Test = float(string.replace(',','.'))
