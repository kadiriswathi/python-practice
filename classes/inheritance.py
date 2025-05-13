class student:
    name='venky'
    def detalis(self):
        print('student name:')
    def age(self):
        print('student age')
class marks(student):
    def names(self):
        print("student grade")
inst=marks()
inst.age()
print(inst.name)