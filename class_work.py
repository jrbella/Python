#

class lotteryPlayer:
    def __init__(self):
        self.name = "Jeff"
        self.numbers =(5,3,7,11,22,1,3)

player = lotteryPlayer()

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []
        
    def average(self):
        return sum(self.grades) / len(self.grades)

    
    
        
jeff = Student("Jeff", "United")
jeff.grades.append(96)
jeff.grades.append(88)
print(jeff.average())