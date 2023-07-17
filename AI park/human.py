class HUMAN: #클래스 변수 설명
    SECRETNUMBER = 486
    
    def __init__(self,num):
        self._num = num
        
    @classmethod
    def do_something(cls):
        cls.SECRETNUMBER += 1 #클래스 변수에 영향을 주고싶을때.
        
h1 = HUMAN(10)
h2 = HUMAN(20)
        
print(h1._num)
print(h2._num)

print(h1.SECRETNUMBER) #클래스 변수. 클래스 전체에서 공유.
print(h2.SECRETNUMBER)

h1._num += 1
h2._num += 1

print(h1._num)
print(h2._num)


print(h1.SECRETNUMBER) 
HUMAN.SECRETNUMBER += 1 
print(h2.SECRETNUMBER) #다 공유한다.


h1.do_something() #h1에서만 불렀는데... 전체 바뀌네? @classmethod를 함으로서. cls.SECRETNUMBER을 변경하니 클래스 변수가 바뀌게되었다.
print(h1.SECRETNUMBER)