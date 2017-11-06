
from Person import Person

class Teacher(Person):
    def __init__(self, first_Name,last_Name, doB, faculty, position, acad_status, salary, courses):
        super().__init__(first_Name,last_Name,doB)
        self.faculty = str(faculty)
        self.position = str(position)
        self.acad_status = str(acad_status)
        self.salary = float(salary)
        self.courses = float(courses)

def get_faculty(objects, faculty):
    result = []
    for i in objects:
        if i.faculty == faculty:
            result.append(i)
    return result

def get_courses(objects):
    result = 0
    for i in objects:
        result += i.courses
    return result


def get_avr_age(objects):
    result = 0
    for i in objects:
        result += i.ages()
    return result / len(objects)
    
