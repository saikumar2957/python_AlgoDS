a=[1,2,-3,-4,0,5]
p=0
n=0
z=0
l=len(a)
for i in range(l):
    if a[i]>0:
        p=p+1
    elif a[i]<0:
        n=n+1
    else:
        z=z+1
k=('%.6f' %(p/l))
m=('%.6f' %(n/l))
s=('%.6f' %(z/l))
print(k,m,s)
