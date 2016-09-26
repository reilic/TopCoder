from student import Student
from student import Person
from student import PhDStudent
from student import MasterStudent
from course import course
import wx

class TabOne(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		
		vbox = wx.BoxSizer(wx.VERTICAL)

		#hbox1
		hbox1= wx.BoxSizer(wx.HORIZONTAL)

		labelID = wx.StaticText(self, 1, 'Student ID', (20,20))
		self.txtID = wx.TextCtrl(self, 0, "", (120,20))

		hbox1.Add(labelID, 1, wx.EXPAND)
		hbox1.Add(self.txtID, 1, wx.EXPAND)

		#hbox2
		hbox2= wx.BoxSizer(wx.HORIZONTAL)

		labelName = wx.StaticText(self, 1, 'Student Name', (20,50))
		self.txtName = wx.TextCtrl(self, 0, "", (120,50))

		hbox2.Add(labelName, 1, wx.EXPAND)
		hbox2.Add(self.txtName, 1, wx.EXPAND)

		#hbox3
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)

		labelDegree = wx.StaticText(self, 1,'Degree', (20, 80))
		self.txtDegree = wx.TextCtrl(self, 0, '', (120, 80))

		hbox3.Add(labelDegree, 1, wx.EXPAND)
		hbox3.Add(self.txtDegree, 1, wx.EXPAND)

		#hbox4
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)

		self.bStudentAdd = wx.Button(self, 1, "Add Student", (250,250))

		self.bStudentClear = wx.Button(self, 1, "Clear Fields", (350,250))

		hbox4.Add(self.bStudentAdd)
		hbox4.Add(self.bStudentClear)

		#add to vbox
		vbox.Add(hbox1)
		vbox.Add(hbox2)
		vbox.Add(hbox3)
		vbox.Add(hbox4)

	def bStudentAdd_Bind(self, handler):
		self.bStudentAdd.Bind(wx.EVT_BUTTON, handler)

	def bStudentClear_Bind(self, handler):
		self.bStudentClear.Bind(wx.EVT_BUTTON, handler)

	def DisplayMsgBox(self, field):
			wx.MessageBox("Please fill in the %s field" % field, "Info", wx.OK | wx.ICON_WARNING)

	def Reset(self):
		self.txtID.Clear()
		self.txtName.Clear()
		self.txtDegree.Clear()

class TabTwo(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		vbox = wx.BoxSizer(wx.VERTICAL)

		#hbox1
		hbox1= wx.BoxSizer(wx.HORIZONTAL)

		labelCourseID = wx.StaticText(self, 1, 'Course ID', (20,20))
		self.txtCourseID = wx.TextCtrl(self, 0, "", (120,20))

		hbox1.Add(labelCourseID, 1, wx.EXPAND)
		hbox1.Add(self.txtCourseID, 1, wx.EXPAND)

		#hbox2
		hbox2= wx.BoxSizer(wx.HORIZONTAL)

		labelCourseName = wx.StaticText(self, 1, 'Course Name', (20,50))
		self.txtCourseName = wx.TextCtrl(self, 0, "", (120,50))

		hbox2.Add(labelCourseName, 1, wx.EXPAND)
		hbox2.Add(self.txtCourseName, 1, wx.EXPAND)

		#hbox4
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)

		self.bCourseAdd = wx.Button(self, 1, "Add Course", (250,250))

		self.bCourseClear = wx.Button(self, 1, "Clear Fields", (350,250))

		hbox4.Add(self.bCourseAdd)
		hbox4.Add(self.bCourseClear)

		#add to vbox
		vbox.Add(hbox1)
		vbox.Add(hbox2)
		vbox.Add(hbox4)

	def bCourseAdd_Bind(self, handler):
		self.bCourseAdd.Bind(wx.EVT_BUTTON,handler)

	def bCourseClear_Bind(self, handler):
		self.bCourseClear.Bind(wx.EVT_BUTTON,handler)

	def Reset(self):
		self.txtCourseID.Clear()
		self.txtCourseName.Clear()

class TabThree(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		vbox = wx.BoxSizer(wx.VERTICAL)

		#hbox1

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)

		labelStudent = wx.StaticText(self, 1, 'Student List', (40,20))
		labelCourse  = wx.StaticText(self, 1, 'Course List', (40,120))

		hbox1.Add(labelStudent, 1, wx.EXPAND)
		hbox1.Add(labelCourse, 1, wx.EXPAND)

		#hbox2

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbStudent = wx.ListBox(self, 1, (40,40))
		self.lbCourse = wx.ListBox(self, 1, (40,140))

		hbox2.Add(self.lbStudent)
		hbox2.Add(self.lbCourse)

		vbox.Add(hbox2)

	def lbStudent_Update(self, p):
		self.lbStudent.Append(p.getName())

	def lbCourse_Update(self, p):
		self.lbCourse.Append(p.getName())		

class enrollment(wx.Frame):

	def __init__(self,*args, **kwargs):
		super(enrollment, self).__init__(*args, **kwargs)

		panel = wx.Panel(self)
		nb = wx.Notebook(panel)

		self.tab1 = TabOne(nb)
		self.tab2 = TabTwo(nb)
		self.tab3 = TabThree(nb)

		nb.AddPage(self.tab1, "Student")
		nb.AddPage(self.tab2, "Course")
		nb.AddPage(self.tab3, "Enrollment")

		sizer = wx.BoxSizer()

		sizer.Add(nb, 1, wx.EXPAND | wx.ALL, 10)
		panel.SetSizer(sizer)

		self.sb = self.CreateStatusBar()
		
		#bind event handlers
		self.tab1.bStudentAdd_Bind(self.bStudentAdd_handler)
		self.tab1.bStudentClear_Bind(self.bStudentClear_handler)
		self.tab2.bCourseAdd_Bind(self.bCourseAdd_handler)
		self.tab2.bCourseClear_Bind(self.bCourseClear_handler)
		


		self.SetSize((500,400))
		self.SetTitle("Enrollment System")
		self.Centre()
		self.Show(True)

	def bStudentAdd_handler(self,e):
		persons.append(Student(self.tab1.txtName.GetValue(),self.tab1.txtID.GetValue(),self.tab1.txtDegree.GetValue()))
		self.tab3.lbStudent_Update(persons[-1])
		self.SetStatusbar('Student Added: ' + self.tab1.txtName.GetValue())
		self.tab1.Reset()

	def bStudentClear_handler(self,e):
		self.tab1.Reset()
		self.SetStatusbar('')

	def bCourseAdd_handler(self,e):
		courses.append(course(self.tab2.txtCourseID.GetValue(), self.tab2.txtCourseName.GetValue()))
		self.tab3.lbCourse_Update(courses[-1])
		self.SetStatusbar('Course Added: ' + self.tab2.txtCourseName.GetValue())
		self.tab2.Reset()

	def bCourseClear_handler(self,e):
		print 'd'


	def SetStatusbar(self, value):
		self.sb.SetStatusText(value)

def main():
	app = wx.App()
	enrollment(None)
	app.MainLoop()

if __name__ == '__main__':

	#initiation
	persons = []
	courses = []
	'''
	#initiate courses
	courses = [course("BUSN1001", "Financial Accounting"), course("ECON1101","Microeconomics")]

	#enrol student into BUSN1001
	persons[0].enroll(courses[0])

	#enrol student into ECON1101
	persons[1].enroll(courses[1])
	'''

	main()