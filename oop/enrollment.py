from student import Student
from student import Person
from student import PhDStudent
from student import MasterStudent

persons = [Student('Cameron', 'U2314313', "Social Science")]
persons.append(PhDStudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction'))
persons.append(MasterStudent("Ellan", 'U4354830', "Photography", "Adam Depands"))

persons[1].enroll("test")

print persons[1].classes




for p in persons:
	if p.type == 'PhDStudent':
		print p
	else:
		p.getName()