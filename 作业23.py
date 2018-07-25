# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:42:39 2018

@author: zhangjiaoli
"""
a=b'1'
print(a)
import urllib request as r
data=r.urlopen('api.openweathermap.org/data/2.5/weather?q=huining&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996')
imprort json
data=json.loads(data)
data['main']['temp']
data['weather'][0]['description']
data['main']['pressure']