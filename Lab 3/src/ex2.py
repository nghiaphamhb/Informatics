import re
with open('test2_ex2.txt', 'r') as input_file:  #test<number>_ex2.txt can be changed
    text=input_file.read()
result=re.findall('[A-Z][a-z]+\s[A-Z]\.[A-Z]\.', text)  #Returns a combination of strings
result=sorted(result)
for x in result:
   y=re.findall('[A-Z][a-z]+', x)
   print(y)




