# __str__ and __repr__
from datetime import date
name="Laman"
print(name)             # if string is,write;else:find repr
print(str(name))        # string print
print(repr(name))       # all print

number=25
print(number)
print(str(number))
print(repr(number))     # str and repr are the same

date=date.today()
print(date)
print(str(date))
print(repr(date))      # object + date

class Teacher:
    def __init__(self,name,surname,subject):
        self.name=name
        self.surname=surname
        self.subject=subject

    def __str__(self):
        return f"Name: {self.name}    Surname: {self.surname}     Subject: {self.subject}"

    def __repr__(self):
        return f'Teacher("{self.name}", "{self.surname}" , "{self.subject}")'

teacher1=Teacher("Samir","Aliyev","Discrete math")
print(teacher1)           # firstly,it researchs str,if it isn't,it print repr.If you want to it,you comment str and check)
print(teacher1.__repr__())





