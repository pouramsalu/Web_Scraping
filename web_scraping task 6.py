import json
with open ('5_task.json','r') as f:
    j=json.load(f)
ra={}
i=0
k=0
while  i<len(j):
    if j[i]['language']=='English':
        k=k+1
        ra['english']=k
    i=i+1
with open ("6_task.json","w") as f:
    json.dump(ra,f )