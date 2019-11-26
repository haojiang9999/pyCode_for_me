import requests ##导入requests
from bs4 import BeautifulSoup
import os
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
y=1
for i in range(0,191):
    all_url = 'http://www.fxsolver.com/browse/?&p='+str(i)  ##开始的URL地址
    start_html = requests.get(all_url,  headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
    Soup = BeautifulSoup(start_html.text,'lxml')
    all_fmla = Soup.find_all('div',class_='fmla')
    for fumula in all_fmla:
     mtitle=fumula.find('a')
     title=mtitle.get_text()
     info = mtitle['href']
     info = str(info)
     info = 'http://www.fxsolver.com'+info
     intro_html = requests.get(info, headers=headers)
     # intro_html.encoding='utf-8'
     Soup_intro = BeautifulSoup(intro_html.text, 'lxml')
     description = Soup_intro.find('div', class_='finfoDesc').find_all('p')
     md = str(description)
     if len(md)>10:
        description = str(description[1])[3:-4]
     else:
        description = 'No description.'
     wiki = Soup_intro.find('div', class_='finfoLinks').find_all('a')
     if (len(wiki) > 1):
         wiki = wiki[1]['href']
     else:
         wiki = 'Sorry!No wikipedia.'
     wiki=str(wiki)
     if(wiki.find('wikipedia')<0):
         wiki = 'Sorry!No wikipedia.'
     svg=fumula.find('svg')
     svg=str(svg)
     os.makedirs(os.path.join("D:\\fumula", str(y)))  ##创建一个存放套图的文件夹
     os.chdir("D:\\fumula\\" + str(y))  ##切换到上面创建的文件夹
     y=y+1
     f = open('description.txt', 'wb')
     f.write(description.encode('GBK','ignore'))
     f.close()
     p = open('s.txt', 'w+')
     p.write(svg)
     p.close()
     os.rename('s.txt','s.html')
     w = open('wikipedia.txt','w+')
     w.write(wiki)
     w.close()
     print(y,wiki)

