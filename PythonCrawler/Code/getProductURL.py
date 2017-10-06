#encoding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import xlrd
import pandas
from pandas import DataFrame

def getHTML(url):
    r = requests.get(url, headers = {'user-agent': 'Mozilla/5.0'})
    r.encoding = r.apparent_encoding
    if r.status_code != 200:
        print "Error!"
        return r.status_code
    else:
        return r.text.encode('utf-8')

def getURLByPages(pageNum):
    url1 = "https://list.jd.com/list.html?cat=670,671,672&"
    url2 = "page="
    url3 = "&sort=sort_totalsales15_desc&trans=1&JL=6_0_0&ms=6#J_main"
    url2 += str(pageNum)
    return url1 + url2 + url3

def getHTMLByPages(pageNum):
    res = []
    for i in range(pageNum):
        res.append(getHTML(getURLByPages(i)))
    return res

def getURL(htmls):
    res = []
    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
        res.append(soup.find_all('a', attrs={'title': re.compile(r'^('')'), 'target': "_blank"}))
    return res

def saveFileURL(urls):
    with open(r'..\ProductURLData\URL.csv', 'a') as f:
        f.write('Product' + ',' + 'Url' + '\n')
        for i in urls:
            for url in i:
                f.write(url.em.string.encode('utf-8') + ',' + str("https://" + url['href']) + '\n')


if __name__ == '__main__':
    saveFileURL(getURL(getHTMLByPages(1)))
    print 'OK'






