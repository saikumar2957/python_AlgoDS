def odd_numbers(l,r):
    k=[]
    for i in range(l,r+1):
        if i%2!=0:
            k.append(i)
    return(k)
l=int(input('enter number l:'))
r=int(input('enter number r:'))
print(odd_numbers(l,r))


    

