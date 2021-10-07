def check_palindrome(number):
    num=number
    reverse_num=0
    flag=False
    while (number>0):
        digit=number%10
        reverse_num=reverse_num*10+digit
        number=number//10
    if (num==reverse_num):
        flag=True
    return flag
number= int(input('Enter the number:'))
flag=check_palindrome(number)
if flag:
    print('it is a palindrome')
else:
    print('it is not a palindrome') 



