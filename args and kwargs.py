def Multi(a,b):         # positional argument
    return a*b

def Mult(a,b,c):            # positional argument
    return a*b*c

def Book(name,number,author="Unknown"):        # key word argument
    return "Book_name: {}    Author_name: {}    Book_number: {}".format(name,author,number)

print(Book("Crime and Punishment",25))

def Type(*args):
    print(type(args))       # type
    for arg in args:
        print(arg)

Type(1,2,3,4,5)

def Sum(*args):
    sum=0
    for arg in args:         # dinamik sum
        sum+= arg
    return sum

def Average(*args):
    return Sum(*args)/len(args)      # dinamik average

print(Sum(2,4,6,8,10))
print(Average(2,3,4,5,6))

def Student(**kwargs):
    for key,value in kwargs.items():      # keyWord args
        print(key,value)

Student(name="Laman",surname="Mikayilova",age=19)

def Mix(p,*par,**param):
    for i in par:
        p+=" "
        p+=i
    for i in param.values():
        p+=" "
        p+=i
    print(p)

Mix("I am","proud","of",sep=",",name="i",att="am from",country="Azerbaijan",end="!")

