#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:28:44 2022

@author: kayla
"""
family1 = {'name':'Soybean Flour', 'value': '120810',
          'quant':['1208100000']}

famlist = [{family1}]

products.json

import json

product_info=json.load((open('products.json'))                   

for fam in product_info:
    name=fam['name'] 
    val=fam['value']
    quants=fma['quant']
    
    