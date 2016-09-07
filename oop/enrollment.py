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

		#call CreateMenu()
		self.CreateMenu()

		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText("Ready")

		panel = wx.Panel(self)
		panel.SetBackgroundColour('#4f5049')

		vbox = wx.BoxSizer(wx.VERTICAL)
		hbox = wx.BoxSizer(wx.HORIZONTAL)

		btnAddEnrol = wx.Button(panel, label='Add Enrollment', size=(100, 30))
		btnAddEnrol.Bind(wx.EVT_BUTTON, self.AddEnrollment)
		hbox.Add(btnAddEnrol)

		vbox.Add(hbox, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

		wx.StaticText(panel, label="Student: ", pos=(10,100))
		wx.StaticText(panel, label="Course: ", pos=(10,120))

		self.labelStudent = wx.StaticText(panel, label='Text', pos=(80,100))
		self.labelStudent.SetBackgroundColour('#dd9090')

		self.labelCourse = wx.StaticText(panel, label='Text', pos=(80,120))
		self.labelCourse.SetBackgroundColour('#dd9090')

		panel.SetSizer(vbox)

		self.SetSize((500,400))
		self.SetTitle("Enrollment System")
		self.Centre()
		self.Show(True)

	def OnQuit(self,e):
		self.Close()

	def AddEnrollment(self,e):
		self.statusbar.SetStatusText("Clicked on Add Enrolment")
		self.labelStudent.SetLabel(persons[0].getStudentID())


def main():
	app = wx.App()
	enrollment(None)
	app.MainLoop()

if __name__ == '__main__':

	#initiate a student
	persons = []
	persons.append(Student('Cameron', 'U2314313', "Social Science"))
	persons.append(PhDStudent('Simon', 'U9012334', 'Computer Science', 'Impact of Compter on mice reproduction'))

	#initiate new courses
	courses = [course("BUSN1001", "Financial Accounting"), course("ECON1101","Microeconomics")]

	#enrol student into BUSN1001
	persons[0].enroll(courses[0])

	#enrol student into ECON1101
	persons[1].enroll(courses[1])

	main()