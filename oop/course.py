class course(object):
	"""Skeleton for a course"""
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.enrolled = []

	def acceptEnrolment(self,student):
		self.enrolled.append(student)

	def displayEnrolment(self):
		print "Enrollment: %s" % (self)
		for i in self.enrolled:
			print i

	def __str__(self):
		return self.id + " " + self.name