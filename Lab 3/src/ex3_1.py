import json

from ruamel.yaml import YAML

in_file = "schedule.yaml"
out_file="schedule.json"

yaml=YAML(typ="safe")  #чтобы избежать потенциальных угроз безопасности

with open(in_file, "r", encoding="utf-8") as i:
    data = yaml.load(i) #Используется для анализа данных YAML из другого источника данных и преобразования их в структуру данных Python.

with open(out_file, "w", encoding="utf-8") as o:
    json.dump(data, o, indent=4, ensure_ascii=False)
    #Необязательный аргумент для управления обработкой символов, отличных от ASCII, в данных JSON. Если гарантировать_ascii=False, символы, отличные от ASCII, будут сохраняться в выходных данных JSON вместо преобразования их в escape-
