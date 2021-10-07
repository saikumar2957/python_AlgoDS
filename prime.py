n=int(input('k'))
flag=True
for i in range(2,19):
    if n%i==0:
         
         flag=False
         break
if flag:
    print('prime')
else:
    print('not prime')
        




    