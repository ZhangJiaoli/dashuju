# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:00:46 2018

@author: zhangaoli
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
def weather(a,b):
    print('temperature：'+str(data['list'][2]['main']['temp']))
    print('weather：'+str(data['list'][2]['weather'][0]['description']))
    print('pressure：'+str(data['list'][2]['main']['pressure']))
    print('Maximum temperature：'+str(data['list'][10]['main']['temp_max']))
    print('Minimum temperature：'+str(data['list'][10]['main']['temp_min']))
    a=str(data['list'][b]['weather'][0]['main'])
    if a=='Clear':
        print('Pay attention to sunscreen')
    elif a=='Clouds':
         print('go out for a walk')
    elif a=='Rain':
        print('Remember to take an umbrella in a rainy day')
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)