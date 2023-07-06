import math
import random 

#이건 어찌보면 라이브러리다. 객체 만들어서 누구나 꺼내 써.

# interface
class Problem:
    def __init__(self): #공식 클래스 생성시 호출되는 함수가 있다. init 메소드. 이건 무조건 만들어야. init가 생성자다.#self - 자기 자신의 object.들어가야한다. 암기
        #필요한 변수들을 또 저장 해야지
        #앞에서 꼭 썼던게 solution, value, NumEval      
        self._solution = [] #클래스의 변수임임을 self로 나타내준다. 
        self._value = 0 #앞에 언더바 : 클래스 변수다. 클래스 변수앞에 _ 붙이자 => 밖에 보이긴 싫다! 즉 private. 파이썬은 보통 다 public이니...
        self._numEval = 0 #자바의 this 가 여기의 self 이다.
        
    def setVariable(self): #createProblem 역할.
        pass 
    
    def randomInit(self):
        pass  
    
    def evaluate(self): 
        pass 
    
    def mutants(self):
        pass
    
    def randomMutant(self):
        pass
    
    def describe(self): #describeProbelm
        pass
    
    def storeResult(self, solution, value): #최종 솔루션을 저장.        
        self._solution = solution
        self._value = value
    
    def report(self):         
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))
        
        
        
class Numeric(Problem): #상위클래스가 있을때. TSP와 같은 super(부모)를 가진다. 메소드.
    def __init__(self):
        Problem.__init__(self) #Problem의 상속을 받고있으니. 상위꺼도 같이 당연히 호출해야, ###중요
        
        self._expression = ''
        self._domain = []
        self._delta = 0.01
        
    def setVariable(self):      
        fileName = "problem/" + input("Enter the filename of function:") + ".txt"
        infile = open(fileName,'r')
        self._expression = infile.readline() #txt파일 공식적힌 첫째줄
        varName = []
        low = []
        up = []
        line = infile.readline()        
        while line != '':
            data = line.split(',')
            varName.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
            line = infile.readline() 
                
        infile.close()
        self._domain = [varName, low, up]       
     #  return expression, domain #필요없어졌다

    
    def randomInit(self): ###
        domain = self._domain #p[1]이 셀프._도메인이다
        low = domain[1]
        up = domain[2]
        init = []
        for i in range(len(low)): 
            r = random.uniform(low[i], up[i]) 
            init.append(r)
        
        return init
    
    
    def evaluate(self, current):    #p는 있으니 current는 추가해야지 #상속 받았잖아 위에서. Problem.__init__(self)이걸로         
        self._numEval += 1
        expr = self._expression         # p[0] is self._expression
        varNames = self._domain[0]  # p[1] is self._domain
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)
        
    
    def mutants(self, current):
        neighbors=[]
        for i in range(len(current)): #커런트, 현재값이 갯수만큼 있을거니 current 넣어도 되겠네
          mutant = mutate(current, i, self._delta) #(현재 해당하는 값, 0번째 1번째, 더해주는값, problem) 이렇게 1개 찾음
          neighbors.append(mutant)
          mutant = mutate(current, i, -self._delta) #빼는값도 해줘야지
          neighbors.append(mutant)
        return neighbors     # Return a set of successors
    
    
    def mutate(self, current, i, d): #이건 추가 해줘야지. mutants의 sub격이라... 내부 메소드. private
        curCopy = current[:]
        domain = self._domain        # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy
    
    
    
    
    def randomMutant(self):
        pass
    
    def describe(self): #describeProbelm
        pass
    
    def storeResult(self, solution, value): #최종 솔루션을 저장.        
        self._solution = solution
        self._value = value
    
    def report(self):         
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))    
        
        
    
    
    
    
    
    
    
    
    
    
class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self) #Problem의 상속을 받고있으니. 상위꺼도 같이 당연히 호출해야
        
        self._numCities = 0
        self._locations = []
        self._distanceTable = []
    
    def setVariable(self): 
        pass 
    
    def randomInit(self):
        pass  
    
    def evaluate(self): 
        pass 
    
    def mutants(self):
        pass
    
    def randomMutant(self):
        pass
    
    def describe(self): #describeProbelm
        pass
    
    def storeResult(self, solution, value): #최종 솔루션을 저장.        
        self._solution = solution
        self._value = value
    
    def report(self):         
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))