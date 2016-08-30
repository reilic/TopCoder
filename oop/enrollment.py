from student import Student
from student import Person
from student import PhDStudent
from student import MasterStudent
from course import course

persons = []
persons.append(Student('Cameron', 'U2314313', "Social Science"))
persons.append(PhDStudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction'))
persons.append(MasterStudent("Ellan", 'U4354830', "Photography", "Adam Depands"))

persons[1].enroll(persons[1].getDegree() +' 101')
persons[1].enroll('Advanced ' + persons[1].getclasses()[0])
persons[1].enroll(persons[1].getThesis()[::-1])

courses = [course("BUSN1001", "Financial Accouinting")]

courses[0].acceptenrol(persons[1])

courses[0].displayenrolment()

'''
for p in persons:
	if p.type == 'PhDStudent':
		print p.getclasses()
'''


