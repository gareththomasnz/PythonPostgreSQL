
student_list = []

class Student:
    def __init__(self,  name):
        self.name = name
        self.marks = []

    def average_mark(self):
        number = len(self.marks)
        if number == 0:
            return 0
        total = sum(self.marks)
        return total / number


def create_student():
    name = input("Please input the students name: ")
    student_data = Student()

    return student_data


def add_mark(student, mark):
    student.marks.append(mark)


def student_details(student):
    print("{}, average mark: {}.".format(student.name,
                                         student.average_mark()))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print(student_details(student))


def menu():
    selection = input("enter 'p' to print the student list,"
                      " 's' to add a student or "
                      " 'a' to add a mark to a student or "
                      "'q' to quit: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)
        selection = input("enter 'p' to print the student list,"
                          " 's' to add a student or "
                          " 'a' to add a mark to a student or "
                          "'q' to quit: ")

menu()

