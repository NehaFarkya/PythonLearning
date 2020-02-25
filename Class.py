class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printname(self):
        print (self.name, self.age)


p1=Person('neha',27)

p1.printname()

class Student(Person):

    def __init__(self,name,age,rollno):
        self.rollno=rollno
        super().__init__(name,age)

    def sample(self):
        print(self.name,self.age,self.rollno)

S1=Student('Neha',27,1234)
S1.sample()
        
