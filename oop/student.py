from course import course

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

	def __init__(self, n, id, degree):
		Person.__init__(self,n)
		self.id = id
		self.degree = degree
		self.classes = [] #no class enrolled by default

	def getStudentID(self):
		return self.id

	def getDegree(self):
		return self.degree

	def enroll(self,classes):
		self.classes.append(classes)
		course.acceptEnrolment(classes, self)

	def enrollmentRecord(self):
			return self.classes

	def setDegree(self,degree):
		self.degree = degree

	def __str__(self): #Person.__str__(self)
		return  super(Student,self).__str__()+ "%15s%s\n%15s%s\n"  % ("StudentID: ", self.id, "Degree: ", self.degree)

class PhDStudent(Student):

	type = 'PhDStudent'

	def  __init__(self,n,id,degree, thesis):
		Student.__init__(self,n,id,degree)
		self.thesis = thesis

	def getThesis(self):
		return self.thesis

	def __str__(self):
		return super(PhDStudent,self).__str__() + "%15s%s\n" % ("Thesis: ", self.thesis)

class MasterStudent(Student):

	type = 'MasterStudent'

	def __init__(self,n,id,degree,supervisor):
		Student.__init__(self,n,id,degree)
		self.supervisor = supervisor

	def getSupervisor(self):
			return self.supervisor

	def setDegree(self,degree, supervisor):
		self.degree = degree
		self.supervisor = supervisor

	def __str__(self):
		return super(MasterStudent,self).__str__() + "%15s%s\n" % ("Supervisor: ", self.supervisor)