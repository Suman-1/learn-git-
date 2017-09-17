class Bachelor():

    def __init__(self, name, address, roll_no):  # this is the constructor method

        self.studentname = name
        self.address = address
        self.rollnoofstudent = roll_no

# defined the constructor method then

    def Getname(self):
        return self.name

    def Getaddress(self):
        return self.address

    def Getrollnoofstudent(self):
        return self.roll_no

   # the overall constructor is defined here


class faculty(Bachelor):
    def __init__(self, name, address, roll_no, faculty):
        self.name = name
        self.address = address
        self.roll_no = roll_no
        self.faculty = faculty

    def Getname(self):
        return self.name

    def Getaddress(self):
        return self.address

    def Getrollno(self):
        return self.roll_no

    def Getfaculty(self):
        return self.faculty


a = faculty('suman', 'sindhupalchock', '4825', 'Bsc.CSIT')
b = faculty('Ram', "New Road", '3234', "Engeneering")
c = faculty("Abhishek", "Sakhu", "3232", "Nepal")

for v in [a, b, c]:
    print (v.Getname(), v.Getaddress(), v.Getrollno())
