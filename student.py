class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grade = []

    def add_grade(self,grade):

        if grade >= 90:
            self.grade.append(4.0)
        if grade >= 80:
            self.grade.append(3.0)
        if grade >= 70:
            self.grade.append(2.0)
        if grade >= 60:
            self.grade.append(1.0)
        else:
            self.grade.append(0.0)

    def get_gpa(self):
        return round(sum(self.grade)/len(self.grade),2) if len(self.grade) > 0 else 0.0

    def __str__(self):
        return f"{self.id}, {self.name}, {self.get_gpa()}"

    def __gt__(self, other):
        return self.get_gpa() > other.get_gpa()

if __name__ == '__main__':
    a = Student('test guy', '0000')
    a.add_grade(99)
    a.add_grade(99)
    a.add_grade(99)


