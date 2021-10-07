str1='09:15:35PM'
hrs=int(str1[:2])
med=str1[-2:]
if med=='PM':
    k=12+(hrs%12)
elif str1[-2:] == "AM" and str1[:2] == "12": 
    k= "00"
else:
    k = str1[:2]         
print(str(k)+str1[2:-2])