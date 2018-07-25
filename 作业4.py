# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:15:04 2018

@author: zhangjiaoli
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)

#写出英文版的天气-天气情况，用户输入英文   application应用
print('第一天')
print('temperature：'+str(data['list'][2]['main']['temp']))
print('weather：'+str(data['list'][2]['weather'][0]['description']))
print('pressure：'+str(data['list'][2]['main']['pressure']))
print('Maximum temperature：'+str(data['list'][10]['main']['temp_max']))
print('Minimum temperature：'+str(data['list'][10]['main']['temp_min']))
print('..........')

print('第二天')
print('temperature：'+str(data['list'][10]['main']['temp']))
print('weather：'+str(data['list'][10]['weather'][0]['description']))
print('pressure：'+str(data['list'][10]['main']['pressure']))
print('Maximum temperature：'+str(data['list'][10]['main']['temp_max']))
print('Minimum temperature：'+str(data['list'][10]['main']['temp_min']))
print('..........')

print('第三天')
print('temperature：'+str(data['list'][18]['main']['temp']))
print('weather：'+str(data['list'][18]['weather'][0]['description']))
print('pressure：'+str(data['list'][18]['main']['pressure']))
print('Maximum temperature：'+str(data['list'][18]['main']['temp_max']))
print('Minimum temperature：'+str(data['list'][18]['main']['temp_min']))
print('..........')

print('第四天')
print('temperature：'+str(data['list'][26]['main']['temp']))
print('weather:'+data['list'][26]['weather'][0]['description'])
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('Maximum temperature:'+str(data['list'][26]['main']['temp_max']))
print('Minimum temperature:'+str(data['list'][26]['main']['temp_min']))
print('..........')

print('第五天')
print('temperature:'+str(data['list'][34]['main']['temp']))
print('weather:'+str(data['list'][34]['weather'][0]['description']))
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('Maximum temperature:'+str(data['list'][34]['main']['temp_max']))
print('Minimum temperature:'+str(data['list'][34]['main']['temp_min']))
print('..........')

#温度折线图
print('温度折线图如下：')
print('第一天'+'-'*int(data['list'][0]['main']['temp']))
print('第二天'+'-'*int(data['list'][10]['main']['temp']))
print('第三天'+'-'*int(data['list'][18]['main']['temp']))
print('第四天'+'-'*int(data['list'][26]['main']['temp']))
print('第五天'+'-'*int(data['list'][34]['main']['temp']))
print('..........')

#排序
print('排序如下：')
temper=[data['list'][0]['main']['temp'],
             data['list'][10]['main']['temp'],
             data['list'][18]['main']['temp'],
             data['list'][26]['main']['temp'],
             data['list'][34]['main']['temp']]
print(sorted(temper))

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