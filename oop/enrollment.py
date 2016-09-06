from student import Student
from student import Person
from student import PhDStudent
from student import MasterStudent
from course import course

#initiate a student
persons = [Student('Cameron', 'U2314313', "Social Science")]

#initiate a new course
courses = [course("BUSN1001", "Financial Accouinting"), course("ECON1101","Microeconomics")]


#enrol student into BUSN1001
persons[0].enroll(courses[0])

persons[0].enroll(courses[1])

#persons.append(PhDStudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction'))
#persons.append(MasterStudent("Ellan", 'U4354830', "Photography", "Adam Depands"))


for i in courses:
	i.displayEnrolment()


'''
for p in persons:
	if p.type == 'PhDStudent':
		print p.getclasses()
'''


