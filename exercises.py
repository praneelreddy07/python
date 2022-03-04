from student import Student

class course:
    def __init__(self, title, course_id):
        self.title = title
        self.course_id = course_id
        self.student = []

    def add_student(self, name, id):
        self.student.append(Student(name, id))


    def __str__(self):
        out = ''
        for s in self.student:
            out += str(s) + "\n"
        return out