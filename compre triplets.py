def comparison_points(a,b):
    m=0
    p=0
    for i in range(len(a)):
        if a[i]>b[i]:
            m=m+1
        elif b[i]>a[i]:
            p=p+1
        else:
            pass
    print([m,p])
a,b=map(list,input().split())
comparison_points(a,b)


