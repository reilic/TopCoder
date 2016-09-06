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

	def InitUI(self):
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

		self.SetSize((500,400))
		self.SetTitle("Enrollment System")
		self.Centre()
		self.Show(True)

	def OnQuit(self,e):
		self.Close()

	def AddEnrollment(self,e):
		self.Close()

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