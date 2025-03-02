class Employee:
    def __init__(self, EmpNumP, PayP, JobP):
        self.HourlyPay = PayP
        self.EmployeeNumber = EmpNumP
        self.JobTitle = JobP
        self.PayYear2022 = [0.0] * 52

    def GetEmployeeNumber(self):
        return self.EmployeeNumber.strip()

    def SetPay(self, WeekNumber, Hours):
        self.PayYear2022[WeekNumber - 1] = Hours * self.HourlyPay

    def GetTotalPay(self):
        TotalPay = 0
        for X in range (0, 52):
            TotalPay = TotalPay + self.PayYear2022[X]
        return TotalPay

class Manager(Employee):
    def __init__(self, EmpNumP, PayP, JobP, BonusP):
        super().__init__(EmpNumP, PayP, JobP)
        self.BonusValue = BonusP

    def SetPay(self, WeekNumber, Hours):
        Hours = Hours * (1 + self.BonusValue / 100)
        super().SetPay(WeekNumber, Hours)

def EnterHours():
    try:
        TextFile = "HoursWeek1.txt"
        File = open(TextFile, 'r')
        EmpID = ""
        for x in range(8):
            EmpID = File.readline().strip()
            for Y in range(8):
                if EmployeeArray[Y].GetEmployeeNumber() == EmpID:
                    EmployeeArray[Y].SetPay(1, float(File.readline()))
    except IOError:
        print("Could not find file")

EmployeeArray = []
try:
    TextFile = "Employees.txt"
    File = open(TextFile, 'r')
    for x in range(8):
        Pay = float(File.readline())
        ID = File.readline()
        Temp = File.readline()
        try:
            Bonus = float(Temp)
            Title = File.readline()
            EmployeeArray.append(Manager(ID, Pay, Title, Bonus))
        except ValueError:
            Title = Temp
            EmployeeArray.append(Employee(ID, Pay, Title))
    File.close()
except IOError:
    print("Could not find file")

EnterHours()
for Y in range(8):
    print("{} {:.2f}".format(EmployeeArray[Y].GetEmployeeNumber(), EmployeeArray[Y].GetTotalPay()))
