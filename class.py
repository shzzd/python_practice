from appnew import *

class Person(Students):
    def __init__(self, dept):
        self.dept = dept
        pass


ob = Person('cse')
print(ob.name)
print(ob.age)
print(ob.dept)
print(ob.gender)