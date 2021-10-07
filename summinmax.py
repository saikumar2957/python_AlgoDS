a=[1,7,5,6,3 ]
sum=[]
k=len(a)
for i in range(k):
    x=0
    for j in range(k):
        if i==j:
            continue
        else:
            x=x+a[j]
    sum.append(x)
print(max(sum),min(sum))

