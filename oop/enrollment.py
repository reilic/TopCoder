from student import Student
from student import Person
from student import PhDStudent
from student import MasterStudent
from course import course
import wx

APP_EXIT = 1
APP_AddEnrol = 2

class enrollment(wx.Frame):

	def __init__(self,*args, **kwargs):
		super(enrollment, self).__init__(*args, **kwargs)

		self.InitUI()

	def CreateMenu(self):
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()

		# Add Enrollment menu item
		itemAddEnrollment = wx.MenuItem(fileMenu, APP_AddEnrol, 'Add Enrollment')
		fileMenu.AppendItem(itemAddEnrollment)
		self.Bind(wx.EVT_MENU, self.AddEnrollment, id=APP_AddEnrol)

		fileMenu.AppendSeparator()

		# Quit menu item
		itemQuit = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl-Q')
		fileMenu.AppendItem(itemQuit)
		self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

		menubar.Append(fileMenu, '&File')

		self.SetMenuBar(menubar)

	def InitUI(self):

		#create menu
		#self.CreateMenu()

		#create status bar
		#self.statusbar = self.CreateStatusBar()
		#self.statusbar.SetStatusText("Ready")

		panel = wx.Panel(self)
		#panel.SetBackgroundColour('#4f5049')

		box = wx.BoxSizer(wx.HORIZONTAL)

		#row = 3, col = 2, gap is 9 and 25
		fgs = wx.FlexGridSizer(6, 2, 9, 25)

		labelID = wx.StaticText(panel, label='Student ID')
		labelName = wx.StaticText(panel, label='Student Name')
		labelDegree = wx.StaticText(panel, label='Degree')
		self.labelSupervisor = wx.StaticText(panel, label="Supervisor")

		self.txtID = wx.TextCtrl(panel)
		self.txtName = wx.TextCtrl(panel)	
		self.txtDegree = wx.TextCtrl(panel)
		self.txtSupervisor = wx.TextCtrl(panel)

		btnAdd = wx.Button(panel, label="Add Enrollment")
		btnAdd.Bind(wx.EVT_BUTTON, self.AddEnrollment)

		btnCancel = wx.Button(panel, label="Close")
		btnCancel.Bind(wx.EVT_BUTTON, self.OnQuit)

		self.chkMaster= wx.CheckBox(panel, label ='Master Student')
		self.chkMaster.Bind(wx.EVT_CHECKBOX, self.OnCheckBox, self.chkMaster)
		self.chkMaster.SetValue(True)

		fgs.AddMany([
			(wx.StaticText(panel),1,wx.EXPAND),(self.chkMaster, 1, wx.ALIGN_RIGHT),
			(labelID), (self.txtID, 1, wx.EXPAND), 
			(labelName), (self.txtName, 1, wx.EXPAND), 
			(labelDegree), (self.txtDegree, 1, wx.EXPAND),
			(self.labelSupervisor), (self.txtSupervisor, 1, wx.EXPAND),
			(btnAdd, 1, wx.LEFT | wx.ALIGN_LEFT),  (btnCancel, 2, wx.ALIGN_RIGHT)
			])

		#fgs.AddGrowableRow(2,1)
		fgs.AddGrowableCol(1,1)

		box.Add(fgs, proportion = 1, flag = wx.ALL|wx.EXPAND, border=15)

		panel.SetSizer(box)

		self.SetSize((400,400))
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

	def AddEnrollment(self,e):

		if self.txtID.GetValue() == '' :
			wx.MessageBox("Please fill in the StudentID field", "Info", wx.OK | wx.ICON_WARNING)
			self.txtID.SetFocus()
		elif self.txtName.GetValue() == '':
			wx.MessageBox("Please fill in the Name field", "Info", wx.OK | wx.ICON_WARNING)
			self.txtName.SetFocus()
		elif self.txtDegree.GetValue() == '':
			wx.MessageBox("Please fill in the Degree field", "Info", wx.OK | wx.ICON_WARNING)
			self.txtDegree.SetFocus()
		elif self.txtSupervisor.GetValue() == '' and self.chkMaster.IsChecked():
			wx.MessageBox("Please fill in the Supervisor field", "Info", wx.OK | wx.ICON_WARNING)
			self.txtSupervisor.SetFocus()			
		else:
			if self.chkMaster.IsChecked():
				persons.append(MasterStudent(self.txtID.GetValue(), self.txtName.GetValue(), self.txtDegree.GetValue(),self.txtSupervisor.GetValue()))
			else:
				persons.append(Student(self.txtID.GetValue(), self.txtName.GetValue(), self.txtDegree.GetValue()))
			print persons[-1]
			self.Reset()

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