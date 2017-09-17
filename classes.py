students = []


class Student:

    school_name = "New Summit College"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student" + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

#mark = Student('mark')

# print(mark)

# print(Student.school_name)


class HighSchoolStudent(Student):
    """docstring for HighSchoolStudent"""
    Highschool_name = "New summit High School"

    def get_Highschool_name(self):
        return 'This is high school student'

    def get_name_capitalize(self):


hari = HighSchoolStudent('hari')
print(hari.get_Highschool_name())
