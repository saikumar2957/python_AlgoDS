def check_palindrome(string):
    l= len(string)
    first=0
    last=l-1
    flag= True
    while first<last:
        if string[first]==string[last]:
            first=first+1
            last=last-1
        else:
            flag= False
            break
    return flag
string=input('Enter the string:')
flag = check_palindrome(string)
if flag:
    print('it is a palindrome')
else:
    print('it is not a palindrome')
