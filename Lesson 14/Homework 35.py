class UserException(Exception):
    def __int__(self, message):
        super().__init__()
        self.message = message

    def get_exceprion_message(self):
        return self.message

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
        if len(self.group) == 10:
            raise UserException('Достигнут лимит в группе в 10 человек!')
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


st1 = Student('Male', 30, 'Steve', 'Jobs1', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor1', 'AN145')
st3 = Student('Female', 21, 'Monika', 'Smith1', 'LT52')
st4 = Student('Male', 30, 'Steve1', 'Jobs2', 'AN142')
st5 = Student('Female', 25, 'Liza1', 'Taylor2', 'AN145')
st6 = Student('Female', 21, 'Monika1', 'Smith2', 'LT52')
st7 = Student('Male', 30, 'Steve2', 'Jobs3', 'AN142')
st8 = Student('Female', 25, 'Liza2', 'Taylor3', 'AN145')
st9 = Student('Female', 21, 'Monika2', 'Smith3', 'LT52')
st10 = Student('Female', 25, 'Liza3', 'Taylor4', 'AN145')
st11 = Student('Female', 21, 'Monika3', 'Smith4', 'LT52')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
try:
    gr.add_student(st11)
except UserException as e:
    print(e)

print(len(gr.group))
