#Clear terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Student:

    def __init__(self, phy, math, chem,):
        self.phy = phy
        self.math = math
        self.chem = chem

    @property
    def percent(self):
        return str((self.phy + self.math + self.chem) / 3) +"%"

stu1 = Student(float(input("Physics No:- ")),float(input("Math No:- ")),float(input("Chemistry No:- ")))
#print(stu1.percent)

class per(Student):

    def __init__(self,name, num):
        self.name = name
        self.num = num

per1 = per(input("Enter Your Name:- "),"got")
print(per1.name,per1.num,stu1.percent)

if(stu1.percent >= str(35)):
    print(per1.name,"was Pass")

else:
    print(per1.name,"was Fail")