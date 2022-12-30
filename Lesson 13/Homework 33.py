class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.last_name}'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        self.group.discard(res)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            if len(all_students.split()) > 0:
                all_students += f', {student}'
            else:
                all_students += f'{student}'
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 21, 'Monika', 'Smith', 'LT52')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
print(f'Full group:\n {gr}')
print()

print('Find students:')
print(gr.find_student('Jobs'))
print(gr.find_student('Jobs2'))  # None
print()

print('Delete students')
gr.delete_student('Taylor')
gr.delete_student('Jobs')
gr.delete_student('Jobs')
print(gr)  # Only one student
