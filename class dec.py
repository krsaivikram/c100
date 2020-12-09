class Cars(object):
    def __init__(self,company,model,horsepower,color,speedlimit):
        self.company=company
        self.model = model
        self.horsepower = horsepower
        self.color=color
        self.speedlimit = speedlimit

    def setCompany(self):
        print('honda')

    def changegear(self):
        print("press the clutch and change the gear") 
suzuki = Cars("suzuki",'swift',100,'white',200)
print(suzuki.setCompany())        
