class Person(object):

	def __init__(self, n):
		self.name = n

	def getName(self):
		return 'My name is: %r' % self.name

	def setName(self,n):
		self.name = n
		print 'New Name is: %r' % self.name

	def __repr__(self):
		return "%15s%s\n" % ("Name: ", self.name)

class Student(Person):

	def __init__(self, n, sid, d):
		Person.__init__(self,n)
		self.sid = sid
		self.degree = d
#		print Student.__str__(self)
		
	def getStudentID(self):
		return self.sid

	def getDegree(self):
		return self.degree

	def setDegree(self,d):
		self.degree = d

	def __str__(self):
		return Person.__str__(self) + "%15s%s\n%15s%s\n"  % ("StudentID: ", self.sid, "Degree: ", self.degree)

class PhDStudent(Student):

	def  __init__(self,n,sid,degree, thesis):
		Student.__init__(self,n,sid,degree)
		self.thesis = thesis
#		print PhDStudent.__str__(self)

	def getThesis(self):
		return self.thesis

	def __str__(self):
		return Student.__str__(self) + "%15s%s\n" % ("Thesis: ", self.thesis)

class MasterStudent(Student):

	def __init__(self,n,sid,degree,supervisor):
		Student.__init__(self,n,sid,degree)
		self.supervisor = supervisor

	def getSupervisor(self):
			return self.supervisor

	def setDegree(self,degree, supervisor):
		self.degree = degree
		self.supervisor = supervisor

	def __str__(self):
		return Student.__str__(self) + "%15s%s\n" % ("Supervisor: ", self.supervisor)

Jeff = Person("Jeff")

Cameron = Student('Cameron', 'U2514483', "Social Science")
Simon = PhDStudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction')
#Ellan = MasterStudent("Ellan", 'U4354830', "Photography", "Adam Depands")
#Ellan.setDegree("News Photography", "John Simonthian")

print Cameron
print Simon