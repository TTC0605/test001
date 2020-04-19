import requests
from lxml import html
import pandas as pd
import os

etree = html.etree

def get_html(url):
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    try:
        html = requests.get(url,headers= headers)
        html.encoding=html.apparent_encoding
        if html.status_code == 200:
            print("获取成功")
            # print(html.text)
    except Exception as e :
        print('获取源码失败：%s'%e)
    return html.text

def parse_html(html):
    movies =[]
    imgurls = []
    html = etree.HTML(html)
    lis = html.xpath("//ol[@class='grid_view']/li")

    for li in lis:
        name = li.xpath(".//a/span[@class='title']/text()")[0]
        director_actor=li.xpath(".//div[@class='bd']/p/text()")[0].strip()
        info = li.xpath(".//div[@class='bd']/p/text()")[1].strip()
        rating_score = li.xpath(".//div[@class='star']/span[2]/text()")[0]
        rating_num = li.xpath(".//div[@class='star']/span[4]/text()")[0]
        introduce = li.xpath(".//p[@class='quote']/span/text()")[0]
        imgurl = li.xpath(".//img/@src")[0]
        # print(introduce)

        movie = {'name':name,
                 'director_actor':director_actor,
                 'info':info,
                 'rating_score':rating_score,
                 'rating_num':rating_num,
                 'introduce':introduce
                 }
        movies.append(movie)
        imgurls.append(imgurl)
    return movies,imgurls

def daomloadimg(url,movie):
    if 'movieposter' in os.listdir("E:\python\豆瓣爬取\demo"):
        pass
    else:
        os.mkdir('movieposter')
    os.chdir(r'E:\python\豆瓣爬取\demo\movieposter')
    img = requests.get(url).content

    with open(movie['name']+'.jpg','wb') as f:
        print("正在下载:%s"%url)
        f.write(img)


if __name__== '__main__':
    url ="https://movie.douban.com/top250"
    html = get_html(url)
    movies = parse_html(html)[0]
    imgurls = parse_html(html)[1]

    for i in range(25):
        daomloadimg(imgurls[i],movies[i])

    os.chdir(r'E:\python\豆瓣爬取\demo')
    moviedata = pd.DataFrame(movies)


    moviedata.to_csv("movie.csv")
    print("保存完毕到本地")