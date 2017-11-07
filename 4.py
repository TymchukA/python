from datetime import datetime

class Person:
    def __init__(self,first_Name,last_Name,doB):
        self.last_Name = str(last_Name)
        self.first_Name = str(first_Name)
        self.doB = datetime.strptime(doB, "%d-%m-%Y")
    
    def ages(self):
        return int((datetime.now() - self.doB).days / 365.25)

    
    
    ////from datetime import datetime, timedelta

from Teacher import *

ivi = Teacher("Ihor", "Ivaniuk", "25-07-1965", "Biology", "Proffesor", "PhD", 5000, 4)
dst = Teacher("Dmytro", "Troyanivskii", "01-09-1959", "Biology", "Docent", "MD", 4500, 6)
kvv = Teacher("Konstyantyn", "Voitovych", "12-12-1989", "Economics", "Asisstant", "BD", 3200, 2)
vsd = Teacher("Valentyna", "Bobrova", "25-01-1970", "Economics", "Docent", "Ms", 4700, 5)
arp = Teacher("Artem", "Prentkovych", "20-11-1955", "AM", "Proffesor", "PhD", 5670, 7)
mlm = Teacher("Mykola", "Marchenko", "19-06-1990", "AM", "Assistant", "BD", 3200, 4)
mak = Teacher("Maksym", "Kortenko", "02-02-1978", "AM", "Docent", "MD", 4890, 6)

print(str(arp) + " age is " + str(arp.ages()))

all_faculties = [ivi, dst, kvv, vsd, arp, mlm, mak]
my_faculty = get_faculty(all_faculties, "AM")
print("Sum of courses for all faculties: " + str(get_courses(all_faculties)))
print("Sum of courses for my faculty: " + str(get_courses(my_faculty)))
print("Average age of  all teachers: " + str(get_avr_age(all_faculties)))
print("Average age of teachers from my faculty: " + str(get_avr_age(my_faculty)))
