class Vehicle:
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.ID = ID
        self.MaxSpeed = MaxSpeed
        self.IncreaseAmount = IncreaseAmount
        self.CurrentSpeed = 0
        self.HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.CurrentSpeed
    def GetIncreaseAmount(self):
        return self.IncreaseAmount
    def GetHorizontalPosition(self):
        return self.HorizontalPosition
    def GetMaxSpeed(self):
        return self.MaxSpeed
    def OutputCurrentPosition(self):
        print("Current position = ", self.GetHorizontalPosition())
        print("Current speed = ", self.GetCurrentSpeed())
    
    def SetCurrentSpeed(self, currentSpeed):
        self.CurrentSpeed = currentSpeed
    def SetHorizontalPosition(self, hPosition):
        self.HorizontalPosition = hPosition
    
    def IncreaseSpeed(self):
        self.CurrentSpeed += self.IncreaseAmount
        if (self.CurrentSpeed > self.MaxSpeed):
            self.CurrentSpeed = self.MaxSpeed
        self.HorizontalPosition += self.CurrentSpeed

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VertChange, MaxHeight):
        Vehicle.__init__(self,ID, MaxSpeed, IncreaseAmount)
        self.VerticalPosition = 0
        self.VerticalChange = VertChange
        self.MaxHeight = MaxHeight

    def IncreaseSpeed(self):
        self.VerticalPosition += self.VerticalChange
        if(self.VerticalPosition > self.MaxHeight):
            self.VerticalPosition = self.MaxHeight
        Vehicle.SetCurrentSpeed(self, Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmount(self))
        if(Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self)):
            Vehicle.SetCurrentSpeed(self, Vehicle.GetMaxSpeed(self))
        Vehicle.SetHorizontalPosition(self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self))

    def GetVerticalPosition(self):
        return self.VerticalPosition
    def OutputCurrentPosition(self):
        print("Current position = ", Vehicle.GetHorizontalPosition(self))
        print("Current speed = ", Vehicle.GetCurrentSpeed(self))
        print("Current vertical position = ", self.GetVerticalPosition())

Car = Vehicle("Tiger", 100, 20)
Heli1 = Helicopter("Lion", 350, 40, 3, 100)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputCurrentPosition()
print("")
Heli1.IncreaseSpeed()
Heli1.IncreaseSpeed()
Heli1.OutputCurrentPosition()