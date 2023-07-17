#무슨 기능이 있는지 정도만 정의 해놓는게 추상클래스. 추상클래스에선 메소드만 만들어놓음.
#추상클래스를 상속한 다음에 구현해주면 되겠다.

#import abc #abstrac base class 를 해주면 된다.
from abc import *

class Student(metaclass = ABCMeta):
    def __init__(self, name="", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final = final
      
    def setName(self, name):
        self._name = name

    def setMidterm(self, midterm):
        self._midterm = midterm

    def setFinal(self, final):
        self._final = final

    def getName(self):
        return self._name     
        
    # def calcSemGrade(self): #에러방지용.
    #     return ''
    
    # def calcSemGrade(self): #child에서 꼭 구현해줘라고 알려주고싶을때.
    #     raise NotImplementedError("You must implement this function") #Exception을 발생시켜줌. 던져주는 역할.
    # #근데 이것보다 더 좋은게 있다. 추상화. 
    
    @abstractmethod #데코레이터. 얘는 추상화 한 녀석입니다 알려주는거.
    def calcSemGrade(self): #에러방지용.
        pass    
    
    @staticmethod
    def do_something(): #스태틱메소드
        print('Hello world!')
    
    
    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()
     
    


class LGstudent(Student):    
    
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

class PFstudent(Student):
        
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 60:
            return "Pass"
        else:
            return "Fail"
        
#print(LGstudent('Fred', 87, 92))
        
import student
#stu = student.Student('Kim', 10, 20) #얘는 점수 만드는 기능이 없어서. 그냥 ''리턴용으로 만들어줌.
#근데 구현되지 않은걸 구현되게 child에서 이걸 꼭 써라! 하는걸 표현하고 싶으면? Exception을 발생시킴
#@abstractclassmethod 이걸 붙여준애는 반드시 구현해야 하는 객체가 있는데 구현을 안하니까, 에러
#

lgstu = student.LGstudent('Park', 50, 80)
pfstu = student.PFstudent('Lee', 40, 90)

print(lgstu)
print(pfstu)

#print(stu) #이건 안나오네. calcSemGrade() 이거 구현 안해놨으니. 그럼 빈 껍데기만 구현 해놓자. '' 이걸 리턴하도록

#pfstu.do_something() #필요없는 인스턴스 만들필요가 없잖아. 그때 쓸수있는게 스태틱 메소드
student.PFstudent.do_something()

#일반적인 def 애들은 인스턴스를 만들어서 끄집어 내야하지만
#스태틱메소드 데코레이터가 붙은 애들은 인스턴스 만들 필요가 없다. 즉 자바에서 static.
#클래스 변수란? LGstudent 클래스 가봐. human.py 가봥


print(isinstance(lgstu,student.LGstudent))
print(isinstance(lgstu,student.Student)) #상위도 부모라고 나오넹~

