# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:04:30 2018

@author: zhangjiaoli
"""
def main():
    try:            
        f=open('裙子成都.txt','w',encoding='utf-8')      
        for i in range (1,101):
            url='http://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&clk1=8e789bcf5c4c905750e92cdab2caa313&keyword=%E8%A3%99%E5%AD%90&loc=%E6%88%90%E9%83%BD&spm=a2e15.8261149.076265160012.13'+'&s=((2i-2)*22)'+'&ajax=true'
            import urllib.request as r
            data=r.urlopen(url).read().decode('utf-8','ignore')
            f.write(data+'\n')
            print('第'+str(i)+'页数据')
        f.close()
        print('100条数据爬取完毕！')           
    except Exception:
        print('出现错误！')

main()
