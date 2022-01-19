import requests
from bs4 import BeautifulSoup

class DeccanHerald:

    def __init__(self):
      
        self.mainurl="https://www.deccanherald.com"

        self.webrequest=requests.get(self.mainurl,allow_redirects=True)

        self.soup=BeautifulSoup(self.webrequest.content,'html.parser')

    def listNews(self):

        self.news_list={x.a.div.h4.text.strip():self.mainurl+x.a['href'] for x in self.soup.find_all("div",class_="group snippet-list-block")}
        
        return self.news_list

    def getHeadlines(self):

        return list(self.listNews().keys())

    def redirectAndRead(self,headline):

        for news in self.news_list:
            if headline in news:
                url=self.news_list[headline]

        self.request=requests.get(url)
        self.soup=BeautifulSoup(self.request.content,'html.parser')

        full_news=[]
        for i in self.soup.find_all("p"):
            para=i.text
            if para.lower().startswith("check out"):
                break

            elif para.lower().startswith("follows us"):
                break
            
            elif para.lower().startswith("also read"):
                continue
            
            else:
                full_news.append(para)

        return full_news

d=DeccanHerald().getHeadlines()
print(d)