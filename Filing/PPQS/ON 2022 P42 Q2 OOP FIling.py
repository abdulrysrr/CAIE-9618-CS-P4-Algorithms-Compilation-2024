class Character:
    def __init__(self, Namep, Xcoord, Ycoord):
        self.__Name = Namep
        self.__XCoordinate = Xcoord
        self.__YCoordinate = Ycoord
    
    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange

Characters = []
TextFile = "Characters.txt"
try: 
    with open("Characters.txt", "r") as File:
        for x in range(10):
            Name = File.readline().strip().lower()
            XCoord = File.readline().strip()
            YCoord = File.readline().strip()
            Temp = Character(Name, int(XCoord), int(YCoord))
            Characters.append(Temp)
except:
    print("File not found!")

Position = -1
while(Position == -1):
    CharInput = input("Enter the character to move: ").rstrip('\n').lower()
    for count in range (10):
        Temp = str(Characters[count].GetName().strip())
    if Temp == CharInput:
        Position = count

isValid = False
while(isValid != True):
    Move = input("Enter A for left, W for up, S for down, and D for right: ").upper()
    if Move == "A":
        Characters[Position].ChangePosition(-1,0)
        isValid = True
    if Move == "W":
        Characters[Position].ChangePosition(0,1)
        isValid = True
    if Move == "S":
        Characters[Position].ChangePosition(0,-1)
        isValid = True
    if Move == "D":
        Characters[Position].ChangePosition(1,0)
        isValid = True
    print("{} has changed its coordinates to ({},{})".format(Characters[Position].GetName(),Characters[Position].GetX(),Characters[Position].GetY()))