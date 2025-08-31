class GroupFullError(Exception): pass

class Student:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name
    def __str__(self): return f'{self.first_name} {self.last_name}'

class Group:
    def __init__(self, number): self.number, self.group = number, set()
    def add_student(self, student):
        if len(self.group) >= 10: raise GroupFullError("У групі не може бути більше 10 студентів")
        self.group.add(student)
    def __str__(self): return f'Number: {self.number}\n' + '\n'.join(str(s) for s in self.group)