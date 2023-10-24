input=open('test_ex1.txt','r')
pattern=';-{/'
for x in input:
    if(pattern in x):
        print(x, end='')
        print(x.count(pattern))
