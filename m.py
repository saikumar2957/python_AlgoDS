

l=[{'s':1,'d':2,'a':3},{'s':4,'d':5,'a':6}]
# print(l[1].keys())
for i in range(2):
    for key,value in l[i].items():
        if key =='d':
            print(value)

        
