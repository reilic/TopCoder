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
		hbox1= wx.BoxSizer(wx.VERTICAL)

		labelID = wx.StaticText(self, 1, 'Student ID', (20,20))
		self.txtID = wx.TextCtrl(self, 0, "", (120,20))

		hbox1.Add(labelID, 1, wx.EXPAND)
		hbox1.Add(self.txtID, 1, wx.EXPAND)

		#hbox2
		hbox2= wx.BoxSizer(wx.VERTICAL)

		labelName = wx.StaticText(self, 1, 'Student Name', (20,50))
		self.txtName = wx.TextCtrl(self, 0, "", (120,50))

		hbox2.Add(labelName, 1, wx.EXPAND)
		hbox2.Add(self.txtName, 1, wx.EXPAND)

		#hbox3
		hbox3 = wx.BoxSizer(wx.VERTICAL)

		labelDegree = wx.StaticText(self, 1,'Degree', (20, 80))
		self.txtDegree = wx.TextCtrl(self, 0, '', (120, 80))

		hbox3.Add(labelDegree, 1, wx.EXPAND)
		hbox3.Add(self.txtDegree, 1, wx.EXPAND)

		#hbox4
		hbox4 = wx.BoxSizer(wx.VERTICAL)

		self.bAdd = wx.Button(self, 1, "Add Student", (120,110))

		hbox4.Add(self.bAdd)

		#add to vbox
		vbox.Add(hbox1)
		vbox.Add(hbox2)
		vbox.Add(hbox3)
		vbox.Add(hbox4)

	def BindBtnAdd(self, handler):
		self.bAdd.Bind(wx.EVT_BUTTON, handler)

	def DisplayMsgBox(self, field):
			wx.MessageBox("Please fill in the %s field" % field, "Info", wx.OK | wx.ICON_WARNING)

	def Reset(self):
		self.txtID.Clear()
		self.txtName.Clear()
		self.txtDegree.Clear()

class TabTwo(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		t = wx.StaticText(self, -1, "Second Tab", (20,20))
		self.lbStudent = wx.ListBox(self, 1, (40,40))

	def UpdateStudentListbox(self):
		self.lbStudent.Append("test")

class TabThree(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		t = wx.StaticText(self, -1, "Third Tab", (20,20))
		self.courselistbox = wx.ListBox(self, 1, (40,40))

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

		self.tab1.bAdd.Bind(wx.EVT_BUTTON, self.AddStudent_handler)

		self.SetSize((500,400))
		self.SetTitle("Enrollment System")
		self.Centre()
		self.Show(True)

	def AddStudent_handler(self,e):
		self.tab2.UpdateStudentListbox()

def main():
	app = wx.App()
	enrollment(None)
	app.MainLoop()

if __name__ == '__main__':

	#initiate a student
	persons = []
	'''
	#initiate new courses
	courses = [course("BUSN1001", "Financial Accounting"), course("ECON1101","Microeconomics")]

	#enrol student into BUSN1001
	persons[0].enroll(courses[0])

	#enrol student into ECON1101
	persons[1].enroll(courses[1])
	'''

	main()