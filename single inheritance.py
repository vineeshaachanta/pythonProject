class Parent:
    def fn1(self):
        print("this is parent class")


class Child(Parent):
    def fn2(self):
        print("this is chlid class")
ob=Child()
ob.fn2()
ob.fn1()