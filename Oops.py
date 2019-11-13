class Oops:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def fun(self):
        c=a+b
        print("the sum is ",c)
a=int(input("enter 1 number"))
b=int(input("enter 2 number"))
obj=Oops(a,b)
obj.fun()