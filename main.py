from student import Student
from exercises import  course
from random import randint

def add_random_grades(s: Student):
    s.add_grade(randint(75,90))

def main():
    oop = course('OOP II', 'PO2-001')
    oop.add_student('naruto', '183')
    oop.add_student('sasuke', '172')
    oop.add_student('sakura', '161')

    for student in oop.student:
        for i in range(5):
            add_random_grades(student)
    print(oop)

if __name__== '__main__':
    main()

#naruto = Student('naruto','183')
#for i in range(10):
 #   naruto.add_grade(randint(75,90))

#with open('classlist.txt', 'a') as file:
 #   file.write(str(naruto))


#print(naruto.get_gpa())
