import json
with open ('5_task.json','r') as f:
    j=json.load(f)
a={"english:2"}
lan={}
i=0
k=0
x=0
ch=0
while  i<len(j):
    if j[i]['director']=='madhavan':
        if j[i]['language']=='English':
           k=k+1
           a['english']=k
    lan['madhavan']=a
             
    if j[i]['director']=='sundar':
        if j[i]['language']=='engish':
            lan['sundar']=a
            x=x+1
            a['english']=x
    lan['sundar']=a
        
    if j[i]['director']=='mani ratnam':
        if j[i]['language']=='english':
            ch=ch+1
            a['english']=ch
    lan['mani ratnam']=a
    i=i+1
    
# with open ("10_task.json","w") as f:
#     json.dump(lan,f,indent=8)
        
print(lan)