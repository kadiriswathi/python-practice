class Grandparent:
    def wisdom(self):
        print("I have some wisdom")
class Parent(Grandparent):
    def knowledge(self):
        print('I have some knowledge') 
class Child(Parent):
    def skill(self):
        print('I have  skill') 
obj=Child()
obj.knowledge()                      