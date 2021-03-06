from student import Student
from student import Person
from student import PhDStudent
from student import MasterStudent
from course import course
import wx


class enrollment(wx.Frame):

	def __init__(self,*args, **kwargs):
		super(enrollment, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		#self.statusbar = self.CreateStatusBar() #create status bar
		#self.statusbar.SetStatusText("Ready")

		panel = wx.Panel(self)
		#panel.SetBackgroundColour('#4f5049')

		box = wx.BoxSizer(wx.HORIZONTAL)

		#row = 3, col = 2, gap is 9 and 25
		fgs = wx.FlexGridSizer(7, 2, 9, 25)

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

		hbox = wx.BoxSizer(wx.VERTICAL)
		hbox.Add(btnAdd, 1, wx.EXPAND)

		self.chkMaster= wx.CheckBox(panel, label ='Master Student')
		self.chkMaster.Bind(wx.EVT_CHECKBOX, self.OnCheckBox, self.chkMaster)
		self.chkMaster.SetValue(True)

		self.studenlisttbox = wx.ListBox(panel, 1)
		self.courselistbox = wx.ListBox(panel, 1)

		fgs.AddMany([
			(wx.StaticText(panel),1,wx.EXPAND),(self.chkMaster, 1, wx.ALIGN_RIGHT),
			(labelID), (self.txtID, 1, wx.EXPAND), 
			(labelName), (self.txtName, 1, wx.EXPAND), 
			(labelDegree), (self.txtDegree, 1, wx.EXPAND),
			(self.labelSupervisor), (self.txtSupervisor, 1, wx.EXPAND),
			(wx.StaticText(panel),1,wx.EXPAND),  (hbox, 1, wx.EXPAND),
			(self.studenlisttbox,1,wx.EXPAND), (self.courselistbox,1,wx.EXPAND)
			])

		#fgs.AddGrowableRow(2,1)
		fgs.AddGrowableCol(1,1)

		box.Add(fgs, proportion = 1, flag = wx.ALL|wx.EXPAND, border=15)

		panel.SetSizer(box)

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