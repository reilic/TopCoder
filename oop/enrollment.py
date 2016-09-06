from student import Student
from student import Person
from student import PhDStudent
from student import MasterStudent
from course import course
import wx

class enrollment(wx.Frame):
	def __init__(self,parent):
		super(enrollment, self).__init__(parent)
		self.Centre()
		self.Show()
		self.InitUI()

	def InitUI(self):
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit System')
		menubar.Append(fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

		sysMenu = wx.Menu()
		sitem = sysMenu.Append(wx.ID_OK, 'Add enrollment', "add enrollment")
		menubar.Append(sysMenu, "&System")
		self.Bind(wx.EVT_MENU, self.OnAddEnrollment, sitem)

		self.SetMenuBar(menubar)

		self.SetSize((500,400))
		self.SetTitle("Enrollment System")
		self.Centre()
		self.Show(True)

	def OnQuit(self,e):
		self.Close()

	def OnAddEnrollment(self,e):
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