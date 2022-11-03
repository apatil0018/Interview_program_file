# overloading:two or method having the same name but different parameter
#overridding: child class redifining methods present in the base class with the same parmeter

#Example of overoading
class A:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        return self.x+other.x

a1=A(100)
a2=A(200)
a3=A(300)

print(A(a1+a2)+a3)

#Example of overrriding

class Parent:
    def add(self,a,b):
        print(a+b)

class child(Parent):
    def add(self,a,b):
        print(a*b)
        super().add(20,40)

x=child()
x.add(20,30)
