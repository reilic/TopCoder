from student import Student
from student import Person
from student import PhDStudent
from student import MasterStudent
from course import course
import wx

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

app = wx.App()

frame = wx.Frame(None, -1, 'enrollment.py')

frame.Show()

app.MainLoop()