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
		txtID = wx.TextCtrl(self, 0, "", (120,20))

		hbox1.Add(labelID, 1, wx.EXPAND)
		hbox1.Add(txtID, 1, wx.EXPAND)

		#hbox2
		hbox2= wx.BoxSizer(wx.VERTICAL)

		labelName = wx.StaticText(self, 1, 'Student Name', (20,50))
		txtName = wx.TextCtrl(self, 0, "", (120,50))

		hbox2.Add(labelName, 1, wx.EXPAND)
		hbox2.Add(txtName, 1, wx.EXPAND)

		#hbox3
		hbox3 = wx.BoxSizer(wx.VERTICAL)

		labelDegree = wx.StaticText(self, 1,'Degree', (20, 80))
		txtDegree = wx.TextCtrl(self, 0, '', (120, 80))

		hbox3.Add(labelDegree, 1, wx.EXPAND)
		hbox3.Add(txtDegree, 1, wx.EXPAND)

		#add to vbox
		vbox.Add(hbox1)
		vbox.Add(hbox2)
		vbox.Add(hbox3)

class TabTwo(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		t = wx.StaticText(self, -1, "Second Tab", (20,20))

class TabThree(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		t = wx.StaticText(self, -1, "Third Tab", (20,20))

class enrollment(wx.Frame):

	def __init__(self,*args, **kwargs):
		super(enrollment, self).__init__(*args, **kwargs)

		panel = wx.Panel(self)
		nb = wx.Notebook(panel)

		tab1 = TabOne(nb)
		tab2 = TabTwo(nb)
		tab3 = TabThree(nb)

		nb.AddPage(tab1, "Student")
		nb.AddPage(tab2, "Course")
		nb.AddPage(tab3, "Enrollment")

		sizer = wx.BoxSizer()

		sizer.Add(nb, 1, wx.EXPAND | wx.ALL, 10)
		panel.SetSizer(sizer)

		'''
		labelID = wx.StaticText(panel, label='Student ID')
		labelName = wx.StaticText(panel, label='Student Name')
		labelDegree = wx.StaticText(panel, label='Degree')
		self.labelSupervisor = wx.StaticText(panel, label="Supervisor")

		self.txtID = wx.TextCtrl(panel)
		self.txtName = wx.TextCtrl(panel)	
		self.txtDegree = wx.TextCtrl(panel)
		self.txtSupervisor = wx.TextCtrl(panel)

		btnAdd = wx.Button(panel, label="Add Student")
		btnAdd.Bind(wx.EVT_BUTTON, self.AddStudent)

		#btnCancel = wx.Button(panel, label="Close")
		#btnCancel.Bind(wx.EVT_BUTTON, self.OnQuit)

		self.chkMaster= wx.CheckBox(panel, label ='Master Student')
		self.chkMaster.Bind(wx.EVT_CHECKBOX, self.OnCheckBox, self.chkMaster)
		self.chkMaster.SetValue(True)

		self.studenlisttbox = wx.ListBox(panel, 1)
		self.courselistbox = wx.ListBox(panel, 1)
		'''

		self.SetSize((500,400))
		self.SetTitle("Enrollment System")
		self.Centre()
		self.Show(True)

	def OnQuit(self,e):
		self.Destroy()

	def OnCheckBox(self,e):
		if self.chkMaster.IsChecked():
			self.labelSupervisor.Show(True)
			self.txtSupervisor.Show(True)
		else:
			self.labelSupervisor.Show(False)
			self.txtSupervisor.Show(False)

	def AddStudent(self,e):

		if self.txtID.GetValue() == '' :
			self.DisplayMsgBox("Student ID")
			self.txtID.SetFocus()
		elif self.txtName.GetValue() == '':
			self.DisplayMsgBox("Name")
			self.txtName.SetFocus()
		elif self.txtDegree.GetValue() == '':
			self.DisplayMsgBox("Degree")
			self.txtDegree.SetFocus()
		elif self.txtSupervisor.GetValue() == '' and self.chkMaster.IsChecked():
			self.DisplayMsgBox("Supervisor")
			self.txtSupervisor.SetFocus()			
		else:
			if self.chkMaster.IsChecked():
				persons.append(MasterStudent(self.txtName.GetValue(), self.txtID.GetValue(), self.txtDegree.GetValue(),self.txtSupervisor.GetValue()))
			else:
				persons.append(Student(self.txtName.GetValue(), self.txtID.GetValue(), self.txtDegree.GetValue()))
			
			self.studenlisttbox.Append(persons[-1].getStudentID() + ' - '  + persons[-1].name)
			self.Reset()

	def DisplayMsgBox(self, field):
			wx.MessageBox("Please fill in the %s field" % field, "Info", wx.OK | wx.ICON_WARNING)

	def Reset(self):
		self.txtID.Clear()
		self.txtName.Clear()
		self.txtDegree.Clear()
		self.txtSupervisor.Clear()

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