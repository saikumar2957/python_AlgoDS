def result_rate(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    else:
        print(max(a,b))
a=int(input('Enter number a:'))
b=int(input('Enter number b:'))
result_rate(a,b)