class Human:
    def __init__(self, name, age, iin):
        self.name = name
        self.age = age
        self.iin = iin
    
    def introduce(self):
        print(f"Hello! My name is {self.name}")

class Student(Human):
    def __init__(self, name, age, iin, group, gpa):
        super().__init__(name, age, iin)
        self.group = group
        self.gpa = gpa
    
    def introduce(self):
        super().introduce()
        print(f"My group is {self.group}. My gpa is {self.gpa }")

class Teach(Human):
    def __init__(self, name, age, iin, subject):
        super().__init__(name, age, iin)
        self.subject = subject
        self.grouplist = []

    def addgroup(self, group):
        self.grouplist.append(group)

    def introduce(self):  
        print(f"I teach {self.subject} in groups: ")
        for items in self.grouplist:
            print(items)

Bob = Student("Bob", 19, 111112501124, "1303", 3.52)
Bob.introduce()

Nigger = Teach("Nigger", 52, 52525255252, "Niggerology")
Nigger.addgroup('1234')
Nigger.addgroup('7788')
Nigger.addgroup('1454')
Nigger.addgroup('1666')
Nigger.addgroup('1212')
Nigger.introduce()