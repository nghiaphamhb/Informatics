import re
yaml_data=""
with open ("schedule.yaml", "r", encoding="utf-8") as file:
    yaml_data=file.read()

def yaml_to_json(yaml_data):
    json_data=""
    lines=yaml_data.split('\n')
    i=0
    for line in lines:
        words=line.split(' ')
        newWords=[]
        for word in words:
            if(word=='-'or word=="---"or word=="..."): continue
            if (re.match('[0-9]+:[0-9]+(~)?', word)):
                newWords.append('\"'+word+'\"')
                continue
            if (re.match('[\w./]+', word)):
                newWords.append('"'+word+'"')
            else: newWords.append(word)
        line=''.join(newWords)

        if(i==0): json_data="{"+json_data+"\n"
        if(i==1): json_data=json_data+line+",\n"
        if(i==2): json_data=json_data+line+"[\n"
        if(i==3 or i==4 or i==5):
            json_data= json_data+"{"+ line+"},\n"
        if(i==6): json_data= json_data+"{"+ line+"}],\n"
        if(i==7): json_data=json_data+line+"[\n"
        if(i==8 or i==9 or i==10):
            json_data= json_data+"{"+ line+"},\n"
        if(i==11): json_data= json_data+"{"+ line+"}]}\n"
        i=i+1

    return json_data

json_data=yaml_to_json(yaml_data)

with open ("schedule.json", 'w', encoding="utf-8") as file:
    file.write(json_data)
