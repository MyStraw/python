import math
import random 

#이건 어찌보면 라이브러리다. 객체 만들어서 누구나 꺼내 써.

# interface
class Problem:
    def __init__(self): #공식 클래스 생성시 호출되는 함수가 있다. init 메소드. 이건 무조건 만들어야.
        
        
        
class Numeric(Problem):
    def __init__(self):
        Problem.__init__(self) #Problem의 상속을 받고있으니. 상위꺼도 같이 당연히 호출해야
        
        
    
class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self) #Problem의 상속을 받고있으니. 상위꺼도 같이 당연히 호출해야