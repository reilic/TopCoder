class Person(object):

	type = 'Person'

	def __init__(self, n):
		self.name = n

	def getName(self):
		return 'My name is: %r' % self.name

	def setName(self,n):
		self.name = n
		print 'New Name is: %r' % self.name

	def __str__(self):
		return "%15s%s\n" % ("Name: ", self.name)

class Student(Person):

	type = 'Student'

	def __init__(self, n, sid, degree):
		Person.__init__(self,n)
		self.sid = sid
		self.degree = degree
		
	def getStudentID(self):
		return self.sid

	def getDegree(self):
		return self.degree

	def setDegree(self,degree):
		self.degree = degree

	def __str__(self): #Person.__str__(self)
		return  super(Student,self).__str__()+ "%15s%s\n%15s%s\n"  % ("StudentID: ", self.sid, "Degree: ", self.degree)

class PhDStudent(Student):

	type = 'PhDStudent'

	def  __init__(self,n,sid,degree, thesis):
		Student.__init__(self,n,sid,degree)
		self.thesis = thesis

	def getThesis(self):
		return self.thesis

	def __str__(self):
		return super(PhDStudent,self).__str__() + "%15s%s\n" % ("Thesis: ", self.thesis)

class MasterStudent(Student):

	type = 'MasterStudent'

	def __init__(self,n,sid,degree,supervisor):
		Student.__init__(self,n,sid,degree)
		self.supervisor = supervisor

	def getSupervisor(self):
			return self.supervisor

	def setDegree(self,degree, supervisor):
		self.degree = degree
		self.supervisor = supervisor

	def __str__(self):
		return super(MasterStudent,self).__str__() + "%15s%s\n" % ("Supervisor: ", self.supervisor)

persons = [Person("Jeff")]
persons.append(Student('Cameron', 'U2314313', "Social Science"))
persons.append(PhDStudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction'))
persons.append(MasterStudent("Ellan", 'U4354830', "Photography", "Adam Depands"))

for p in persons:
	if p.type == 'PhDStudent':
		print p
	else:
		print p.getName()


'''
Cameron = Student('Cameron', 'U2314313', "Social Science")
Simon = PhDStudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction')
Ellan = MasterStudent("Ellan", 'U4354830', "Photography", "Adam Depands")

print Cameron

Cameron.setDegree("International relations")

print Cameron

print Simon

Simon.setDegree("Database Management")

print Simon

print Ellan

Ellan.setDegree("News Photography", "John Simonthian")

print Ellan
'''
