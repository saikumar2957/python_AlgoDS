class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print('{} is now sitting'.format(self.name))
    def roll_over(self):
        print('{} rolled over!'.format(self.name))
    def get_age(self):
        print('{} is {} years old'.format(self.name,self.age))
d1=Dog('browny',23)
d2=Dog('shiro',21)
d1.sit()
d2.roll_over()
d1.get_age()
d2.get_age()
