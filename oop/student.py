class Person(object):

	def __init__(self, n):
		self.name = n

	def getName(self):
		return 'My name is: %r' % self.name

	def setName(self,n):
		self.name = n
		print 'New Name is: %r' % self.name

class Student(Person):

	def __init__(self, n, sid, d):
		Person.__init__(self,n)
		self.sid = sid
		self.degree = d

	def getStudentID(self):
		return self.sid

	def getDegree(self):
		return self.degree

	def setDegree(self,d):
		self.degree = d

class PhDtudent(Student):

	def  __init__(self,n,sid,degree, thesis):
		Student.__init__(self,n,sid,degree)
		self.thesis = thesis

	def getThesis(self):
		return self.thesis

class MasterStudent(Student):

	def __init__(self,n,sid,degree,supervisor):
		Student.__init__(self,n,sid,degree)
		self.supervisor = supervisor

	def getSupervisor(self):
			return self.supervisor

Cameron = Student('Cameron', 'U2514483', "Social Science")
	
print 'My Name is %s \nMy UnivID is %s' % (Cameron.getName(), Cameron.getStudentID())

Jeff = Person("Jeff")

print Jeff.getName()

Simon = PhDtudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction')

print Simon.getDegree()

Simon.setDegree("Earth Science")

print Simon.getDegree()

print Simon.getName()

print Simon.getThesis()

Ellan = MasterStudent("Ellan", 'U4354830', "Photography", "Adam Depands")

print Ellan.getDegree()

print Ellan.getName()

print Ellan.getSupervisor()