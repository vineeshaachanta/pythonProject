class Base:
    def display(self):
        print("hello")
class Derived(Base):
    def display(self):
        print("good mrng")
ob=Derived()
ob.display()