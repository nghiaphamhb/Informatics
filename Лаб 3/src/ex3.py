# Truyền nội dung file vào yaml_data
yaml_data =""
with open("schedule.yaml", "r", encoding = "utf-8") as f:
    yaml_data=f.read()

def yaml_to_json(yaml_data):
    lines = yaml_data.split('\n')   #chia văn bản thành bộ các dòng
    json_data=""                    #tạo giá trị trả về của hàm
    i=0
    for line in lines:              #xét lần lượt từng dòng
        words=line.split(' ')       #chia dòng thành bộ các từ
        new_words=[]                #tạo 1 danh sách các từ mới
        for word in words:          #xét lần lượt từng từ (trong dòng)
            if(word=="---" or word=="..."):
                break
            if(word=='-' or word==''):
                continue
            if(word==':'):
                new_words.append(word)
                continue
            else: new_words.append("\""+word+"\"")
        line=''.join(new_words)

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

# Chuyển đổi YAML thành JSON
json_data = yaml_to_json(yaml_data)

# In JSON kết quả
with open("schedule.json", "w", encoding = "utf-8") as f:
    f.write(json_data)
