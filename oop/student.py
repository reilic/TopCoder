class Person(object):

	def __init__(self, n):
		self.name = n

	def Name(self):
		return 'My name is: %r' % self.name

	def setName(self,n):
		self.name = n
		print 'New Name is: %r' % self.name

class Student(Person):

	def __init__(self, n, sid):
		Person.__init__(self,n)
		self.sid = sid
		self.money = 0

	def showStudentID(self):
		return self.sid

Cameron = Student('Cameron', 'U2514483')
	
print 'My Name is %s \nMy UnivID is %s' % (Cameron.Name(), Cameron.showStudentID())

Jeff = Person("Jeff")

print Jeff.Name()