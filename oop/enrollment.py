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
		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText("Ready")

		panel = wx.Panel(self)
		panel.SetBackgroundColour('#4f5049')

		box = wx.BoxSizer(wx.HORIZONTAL)

		#row = 3, col = 2, gap is 9 and 25
		fgs = wx.FlexGridSizer(4, 2, 9, 25)

		labelID = wx.StaticText(panel, label='Student ID')
		labelName = wx.StaticText(panel, label='Student Name')
		labelDegree = wx.StaticText(panel, label='Degree')

		self.txtID = wx.TextCtrl(panel)
		self.txtName = wx.TextCtrl(panel)
		self.txtDegree = wx.TextCtrl(panel)

		btnAdd = wx.Button(panel, label="Add Enrollment")
		btnAdd.Bind(wx.EVT_BUTTON, self.AddEnrollment)

		btnCancel = wx.Button(panel, label="Close")
		btnCancel.Bind(wx.EVT_BUTTON, self.OnQuit)

		fgs.AddMany([
			(labelID), (self.txtID, 1, wx.EXPAND), 
			(labelName), (self.txtName, 1, wx.EXPAND), 
			(labelDegree), (self.txtDegree, 1, wx.EXPAND),
			(btnAdd, 1, wx.LEFT),  (btnCancel, 2, wx.RIGHT)
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

	def AddEnrollment(self,e):

		if self.txtID.GetValue() == '' or self.txtName.GetValue() == '' or self.txtDegree.GetValue() == '':
			wx.MessageBox("Please fill in all details", "Info", wx.OK | wx.ICON_WARNING)
		else:
			persons.append(Student(self.txtID.GetValue(), self.txtName.GetValue(), self.txtDegree.GetValue()))
			print persons[-1]
			self.txtID.Clear()
			self.txtName.Clear()
			self.txtDegree.Clear()

def main():
	app = wx.App()
	enrollment(None)
	app.MainLoop()

if __name__ == '__main__':

	#initiate a student
	persons = []
	'''
	persons.append(PhDStudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction'))	

	#initiate new courses
	courses = [course("BUSN1001", "Financial Accounting"), course("ECON1101","Microeconomics")]

	#enrol student into BUSN1001
	persons[0].enroll(courses[0])

	#enrol student into ECON1101
	persons[1].enroll(courses[1])
	'''

	main()