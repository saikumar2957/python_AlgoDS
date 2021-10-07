import copy
s=[3,4,21,36,10,28,35,5,24,42]
l=len(s)
pre_max=s[0]
k=copy.deepcopy(s)
x=0
for i in range(1,l):
    if s[i] > pre_max:
        pre_max=s[i]
        x+=1
    s[i]=pre_max
print(x)
y=0
pre_max=k[0]
for i in range(1,l):
    if k[i] < pre_max:
        pre_max=k[i]
        y+=1
    k[i]=pre_max
print(y)        
