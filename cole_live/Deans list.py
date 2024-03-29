class Student:
    def __init__(self, first, last, gpa):
        self.first = first # first name
        self.last = last   # last name
        self.gpa = gpa     # grade point average

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last

    def __str__(self):
        return f"{self.first} {self.last} (GPA: {self.gpa})"

class Course:
    def __init__(self):
        self.roster = []  # list of Student objects

    def add_student(self, student):
        self.roster.append(student)

    def get_deans_list(self):
        # Type your code here
        deans_list =[]
        for student in self.roster:
            if student.gpa >= 3.5:
                deans_list.append(student)
        return deans_list

if __name__ == "__main__":
    course = Course()

    course.add_student(Student('Henry', 'Nguyen', 3.5))
    course.add_student(Student('Brenda', 'Stern', 2.0))
    course.add_student(Student('Lynda', 'Robinson', 3.2))
    course.add_student(Student('Sonya', 'King', 3.9))

    deans_list = course.get_deans_list()
    print("Dean's list:")
    for student in deans_list:
        print(student)