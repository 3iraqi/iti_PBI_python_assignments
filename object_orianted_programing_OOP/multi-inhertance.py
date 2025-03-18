
class Parent_1:
    def here(self):
        print("I am a parent 1 ")

class Parent_2(Parent_1):
    def here(self):
        print("I am a parent 2 ")

class Parent_3(Parent_1):
    def here(self):
        print("I am a parent 3 ")

class Child(Parent_2, Parent_3):
    pass

child_1 =Child()

child_1.here() 