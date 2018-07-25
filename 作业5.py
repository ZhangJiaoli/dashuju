# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:37:28 2018

@author: zhangjiaoli
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
#1.优化代码 用函数的方式来来修改练习4，输出每一天的天气（函数）
def weather(a,b):
    print('第'+str(a)+'天')
    print('temperature：'+str(data['list'][b]['main']['temp']))
    print('weather：'+str(data['list'][b]['weather'][0]['description']))
    print('pressure：'+str(data['list'][b]['main']['pressure']))
    print('Maximum temperature：'+str(data['list'][b]['main']['temp_max']))
    print('Minimum temperature：'+str(data['list'][b]['main']['temp_min']))
    print(' ')
    print('..........')
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)
#温度折线图
print('温度折线图：')
def pic(c,d):
    val=str('第'+str(c)+'天'+'-'*int(data['list'][d]['main']['temp']))
    return val
print(pic(1,2))
print(pic(2,10))
print(pic(3,18))
print(pic(4,26))
print(pic(5,34))



