# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:14:46 2018

@author: zhangjiaoli
"""
#显示4个商品然后打印分割线，只要第一页36个商品信息
#列出36个商品
#获取所有的商品价格并且给商品排序，从高到低排序
#按照销量排序
#商品过滤，只要15天退款或者包邮的商品信息，显示
#商品销量排序
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
#商品信息
def items():
    for x in range(0,36):
        title=data['mods']['itemlist']['data']['auctions'][x]['title']
        price=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        view_fee=data['mods']['itemlist']['data']['auctions'][x]['view_fee']
        item_loc=data['mods']['itemlist']['data']['auctions'][x]['item_loc']  
        view_sales=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        print('商品名为：'+str(title))
        print('商品价格为：'+str(price))
        print('商品邮费为：'+str(view_fee))
        print('发货地址是：'+str(item_loc))
        print('商品销量：'+str(view_sales))
items()
#价格排序
pr=[]
def price():    
    for a in range(0,36):
        q=float(data['mods']['itemlist']['data']['auctions'][a]['view_price'])
        pr.append(q)    
price()
a=sorted(pr)
print('价格从高到低:')
b=list(reversed([a]))
print(b)
#销量排序
pi=[]
def dat():
    for a in range(0,36):
        q=str(data['mods']['itemlist']['data']['auctions'][a]['view_sales'])
        b=int(q[0:-3])
        pi.append(b)
    return pi
dat()
print('商品销量从高到低:')
print(sorted(pi))
#包邮
def post_fee():
    for i in range(0,36):
        if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.0:
            print('第'+str(i+1)+'件商品包邮')
post_fee()
c=post_fee()
print(c)

for x in range(0,36):
    y=x
    if str(data['mods']['itemlist']['data']['auctions'][x]['item_loc'] ) =='成都':
        print('第{}件发货地是成都'.format(y+1),end=';')
    else:
        continue
#发货地是成都
def post_loc():
    for i in range(0,36):
        if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.0:
            print('第'+str(i+1)+'件商品包邮')