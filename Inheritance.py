# 상속 프로그램
class Man:
    def __init__(self, Name):
        self.name = Name
    def tellYourName(self):
        print('My name is ' + self.name)

class BusinessMan(Man):
    def __init__(self, Name, Company, Position):
        self.company = Company
        self.position = Position
        Man.__init__(self, Name)
    def tellYourInfo(self):
        print('My company is ' + self.company)
        print('My position is ' + self.position)
        self.tellYourName()

businessman = BusinessMan(Name='park', Company='Hansung', Position='student')
businessman.tellYourInfo()