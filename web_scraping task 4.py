import json
import requests
from bs4 import BeautifulSoup
with open("first_task.json","r")as f:
    x=json.load(f)
    i=0
    url=[]
    while i<len(x):
        print(i+1,":",x[i]["name"])
        url.append(x[i]["url"])
        i+=1
    user=int(input("enter the movie Sl.no:"))-1
    x=url[user]
    b=requests.get(x)
    soup=BeautifulSoup(b.text,"html.parser")
    c=soup.find("script",type="application/ld+json").text
    a=json.loads(c)

    dic={}
    for j in a:
        dic["name"]=a["name"]
        dic["director"]=a["director"][0]["name"]
        dic["image"]=a["image"]
        dic["description"]=a["description"]
        dic["language"]=a["review"]["inLanguage"]
        dic["genre"]=a["genre"]
        dic["country"]="india"
    with open("task_four.json","w")as f:
        json.dump(dic,f,indent=4)