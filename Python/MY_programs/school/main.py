class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.grades = {}
        self.cgpa = 0.0

    def enroll_course(self, course_id):
        self.courses.append(course_id)
        print(f"{self.name} just enrolled in a new course with the id '{course_id}'")
    def add_grade(self, course_id, grade):
        self.grades[course_id] = grade
        print(f"new term grade '{grade}' for {self.name}")
       
       

    def cal_cgpa(self):
        sum = 0
        for key in self.grades:
            if self.grades[key] == 'A':
                sum += 4
            elif self.grades[key] == 'B':
                sum += 3
            elif self.grades[key] == 'C':
                sum += 2
            elif self.grades[key] == 'D':
                sum += 1
            elif self.grades[key] == 'F':
                sum += 0.5
        self.cgpa = sum / len(self.grades)
        print(f"{self.name}'s CGPA is: {self.cgpa:.1f}")


    def get_details(self):
        return [self.name, self.student_id, self.courses, self.cgpa]


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits
        self.students = []

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

    def remove_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)
        else:
            print(f'student {student_id} not enrolled in {course_id}')

    def get_details(self):
        return {'id':self.course_id, 'name':self.name, 'credits':self.credits, 'students':self.students }




student1 = Student('Atila', 171108)
course1 = Course(583531, 'C programming', 5)
course1.add_student(171108)
student1.enroll_course(583531)
student1.add_grade(583531, 'A')
student1.cal_cgpa()
print(course1.get_details())
