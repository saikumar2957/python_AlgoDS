def input_string(alphabet):
    names=['Saikumar Bangalore','arun coimbatore','machine computer','Human earth','animals forest']
    l=[]
    for i in range(len(names)):
        k=(list(names[i]))
        if alphabet.lower()==k[0].lower():
            l.append(names[i])
    if l:
        return l
    else:
        return 'There is no such name and address'
Name_address=input_string('S')
print(Name_address)
