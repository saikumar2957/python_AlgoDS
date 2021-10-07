a=[2,6]
b=[24,36]
l=[]
for i in range(a[-1],b[0]+1):
    x=0
    for j in a:
        if i%j==0:
            x+=1
    if len(a)==x:
        l.append(i)
count=[]

for k in l:
    x = 0
    for t in b:
        if t%k==0:
            x+=1
    if x == len(b):
        count.append(k)
print(len(count))

            

