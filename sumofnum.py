def sum_of_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input('enter value n:'))
print(sum_of_numbers(n))

