#oops syntax
'''class classname():
    #attribute
    name="pooja"
    place="vij"
    age=28
    def fname(method_name):
        print(statements.....)
a=classname()
a.fname()'''

#class declaration
'''class Details():
    name="pooja"
    place="vij"
    age=28
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

'''class emp():
    id=101
    name="pooja"
    mailid="pooja@gmail.com"
    salary=40000
    designation="python mentor"
    def empl(self):
        print(self.id,self.name,self.mailid,self.salary,self.designation)
a=emp()
print(dir(a))
a.empl()'''
#object instantiation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("pooja",28,"hyd")
a.display()
b=Details()
b.data("priya",29,"vij")'''



#object intialization
'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("pooja",28,"vij")
print(dir(a))
a.display()'''

'''class Details():
    def __init__(self):
        self.name=input("enter the name:")
        self.age=int(input("enter the age:"))
        self.place=input("enter the place:")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.display()'''

'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name:"),int(input("age:")),input("place:"))
print(dir(a))
a.display()'''

#diff b/w _ and __

'''class Emp1():
    def __init__(self):
        self.name="pooja"
        self._mailid="pooja@gmail.com"
        self.__salary=10000
a=Emp1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Emp1__salary)

class Emp2():
    def __init__(self):
        self.name="kiran"
        self._mailid="kiran@gmail.com"
        self.__salary=20000
a=Emp2()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Emp2__salary)

class Emp3():
    def __init__(self):
        self.name="basha"
        self._mailid="basha@gmail.com"
        self.__salary=10000
a=Emp3()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Emp3__salary)'''

'''

class Emp1():
    def __init__(self):
        self.name="pooja"
        self._mailid="pooja@gmail.com"
        self.__salary=10000
class Emp2():
    def __init__(self):
        self.name="kiran"
        self._mailid="kiran@gmail.com"
        self.__salary=20000
class Emp3():
    def __init__(self):
        self.name="basha"
        self._mailid="basha@gmail.com"
        self.__salary=10000

a=Emp1()
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Emp1__salary)

b=Emp2()
print(b.name)
print(b._mailid)
#print(a.__salary)
print(b._Emp2__salary)

c=Emp3()
print(c.name)
print(c._mailid)
#print(c.__salary)
print(c._Emp3__salary)'''

#polymorphism
#operator Overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(a.__pow__(2))
print(a.__ge__(b))
print(a.__le__(b))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
print("python".__add__("course"))
print(a.__add__(" "+b))
print(a.__add__(" "+b).title())'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __sub__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(10)
y=B(20)
print(x-y)'''

#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum is",a+b+c)
        elif a!=None and b!=None:
            print("The product is",a*b)
        else:
            print("program ends")
x=new()
x.sum()
x.sum(2,4)
x.sum(4,5,6)'''

'''class new():
    def sum(self,a=2,b=3,c=5):
        if a!=2 and b!=3 and c!=5:
            print("The sum is",a+b+c)
        elif a!=6 and b!=7:
            print("The product is",a*b)
        else:
            print("program ends")
x=new()
x.sum()'''

#method overriding
'''class Animal():
    def speak(self):
        print("animals can make sound")
class Dog():
    def speak(self):
        print("dog can bark")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

'''class car():
    def ride(self):
        print("car has 4  wheels")
class bike():
    def ride(self):
        print("bike has 2 wheels")
a=car()
b=bike()
a.ride()
b.ride()'''

#single inheritance
'''class RBI():
    cash=100000
    def available_cash(cls):
        print("available_cash is",cls.cash)
        print("available_cash is",cls.cash)
class SBI(RBI):#child-1
    pass
class HBFC(RBI):
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HBFC()
a.available_cash()
a.new_cash()'''
#multiple inheritance
'''class father():
    def height_father(cls):
        print("height of father is 5.5")
class mother():
    def weight_mother(cls):
        print("weight of mother is 70 kgs")
class kid(father,mother):
    def dob_kid(cls):
        print("dob of kid is 10-11-2004")
a=kid()
a.height_father()
a.weight_mother()
a.dob_kid()'''
#without inheritance
'''class father():
    def height_father(cls):
        print("height of father is 5.5")
class mother():
    def weight_mother(cls):
        print("weight of mother is 70 kgs")
class kid(father,mother):
    def dob_kid(cls):
        print("dob of kid is 10-11-2004")
a=father()
b=mother()
c=kid()
a.height_father()
b.weight_mother()
c.dob_kid()'''

#multilevel
'''class grandparent():
    def land(cls):#we can use self also
        print("land is 2 acres")
class parent(grandparent):
    def house(cls):
        print("house is 100sqft")
class child(parent):
    def bike(cls):
        print("bike is 20000")
a=child()
a.land()
a.house()
a.bike()'''

#hierarihical
'''class emp():
    def comp_name(self):
        print("company name is codegnan")
class trainer(emp):
    def teach(self):
        print("trainer is pooja")
class student(emp):
    def std(self):
        print("student is nanditha")
a=student()
b=trainer()
a.comp_name()
b.teach()
a.std()'''

#hybrid
'''class emp():
    def company_name(self):
        print("company name is codegnan")
class student(emp):
    def study(self):
        print("prepare for exams")
class developer(emp):
    def develop(self):
        print("develops the code")
class program_manager(student,developer):
    def manage(self):
        print("managing the data")
c=program_manager()
c.company_name()
c.study()
c.develop()
c.manage()'''

#super()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):#sub class
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
a=child("pooja",28)
print(a.name)
print(a.age)'''

#encapsulation
#publicdata()
'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
a=child()
a.method1()
a.method2()'''

#_protectedata
'''class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
a=child()
a.method1()
a.method2()
print(a._protecteddata)'''

#__privatedata
'''class parent():
    __privatedata='python'
    def method1(self):
        print(self._parent__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
a=child()
a.method1()
a.method2()'''

#abstraction
'''class A ():
    def method1(self):
        pass
obj=A()
obj.method1()'''

'''class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A():
    @abstractmethod
    def method1(self):
        print("python")
obj=A()
obj.method1()'''

'''from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''


    
        







