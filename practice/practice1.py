import requests
from bs4 import BeautifulSoup
from datetime import datetime
url="https://music.bugs.co.kr/chart"
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
results=soup.findAll("p","title")

rank=1
f=open("practice1.txt","w")
f.write(datetime.today().strftime("20%y-%m-%d의 벅스 실시간 차트 순위입니다."))
f.write("\n")
for i in results:
    f.write(str(rank)+"위:"+i.get_text()+"\n")
    rank+=1