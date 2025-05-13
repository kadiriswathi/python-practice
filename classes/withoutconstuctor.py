class  Person:
    def ind(self):
        if hasattr(self ,'name') and (self,'age'):
             print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
        else:
            print('there is no student detail')
person=Person()
#erson.ind()
person.name='swati'
person.age=30
person.ind()