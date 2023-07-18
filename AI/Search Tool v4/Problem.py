import math
import random 
from setup import Setup


#이건 어찌보면 라이브러리다. 객체 만들어서 누구나 꺼내 써.

# interface
class Problem:
    def __init__(self): #공식 클래스 생성시 호출되는 함수가 있다. init 메소드. 이건 무조건 만들어야. init가 생성자다.#self - 자기 자신의 object.들어가야한다. 암기
        
        Setup.__init__(self) #이거 없으면 오버라이딩이 되니까
        
        #필요한 변수들을 또 저장 해야지
        #앞에서 꼭 썼던게 solution, value, NumEval      
        self._solution = [] #클래스의 변수임임을 self로 나타내준다. 
        self._value = 0 #앞에 언더바 : 클래스 변수다. 클래스 변수앞에 _ 붙이자 => 밖에 보이긴 싫다! 즉 private. 파이썬은 보통 다 public이니...
        self._numEval = 0 #자바의 this 가 여기의 self 이다.
        
        self._bestSolution = []
        self._bestMinimum = 0.0
        self._avgMinimum = 0.0
        self._avgNumEval = 0
        self._sumOfNumEval = 0
        
        self._pFileName = '' #Convex.txt 등등 파일 있었쟈냐 #얘는 업뎃 되네
               
        
    def setVariables(self, parameters): #createProblem 역할. #셋업에 있는걸 호출해줘야겠징~        
        self._pFileName = parameters['pFileName'] #이것만 하면 오버라이딩됨.
        Setup.setVariables(self, parameters) 
        #pass #pass 하면 overriding 돼서 아무것도 없게된다. 차라리 이 def를 다 주석처리 하면? setup에 있는걸 자동으로 상속한다.
    
    def getSolution(self):
        return self._solution
    
    def getValue(self):
        return self._value
    
    def getNumEval(self):
        return self._numEval  
        
        
    
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
    
    def storeExpResult(self, results):
        # self._bestSolution = results[0]
        # self._bestMinimum = results[1]
        # self._avgMinimum = results[2]
        # self._avgNumEval = results[3]
        # self._sumOfNumEval = results[4]

        self._bestSolution, self._bestMinimum, self._avgMinimum, self._avgNumEval, self._sumOfNumEval = results
        #둘이 똑같다. 튜플은 이런식으로 가능했쟈냐
    
    
    def report(self):         
        print()
        #print("Total number of evaluations: {0:,}".format(self._numEval)) #numEval 두면 제일 마지막거만 출력되겠네
        print("Average number of evaluations: {0:,}".format(self._avgNumEval))
        
        
        
class Numeric(Problem): #상위클래스가 있을때. TSP와 같은 super(부모)를 가진다. 메소드.
    def __init__(self): #이거까지 Setup 할필요 없다. 바로 위에껏만 건들면 아래로 아래로 건너건너 된다.
        Problem.__init__(self) #Problem의 상속을 받고있으니. 상위꺼도 같이 당연히 호출해야, ###중요
        
        self._expression = ''
        self._domain = []
        
    # def getDelta(self):
    #     return self._delta
    
    # def getAlpha(self):
    #     return self._alpha
    
    # def getDx(self):
    #     return self._dx

        
    def setVariables(self, parameters):      
        Problem.setVariables(self, parameters)
        # fileName = "problem/" + input("Enter the filename of function:(Convex, Ackley, Griewank) ") + ".txt"
        # infile = open(fileName,'r')
        infile = open(self._pFileName, 'r')
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
     
     
    def takeStep(self, x, v): #mutate에서는 도메인 안에 값이 있는지 없는지 확인했다. 벗어나면 stop
        grad = self.gradient(x,v)
        #update 해야지~ for문으로 돌아야지
        xCopy = x[:]
        for i in range(len(x)):
            xCopy[i] = xCopy[i] - self._alpha * grad[i]
        
        if self.isLegal(xCopy): #도메인 범위 내에 있느냐. 없느냐 확인
            return xCopy
        else:
            return x
    
    def isLegal(self, x):
        domain = self._domain
        low, up = domain[1], domain[2] #범위체크. 주변에 비슷한 코드 가져오면 돼~
        for i in range(len(low)):
            if low[i] <= x[i] <= up[i]:                        
                pass #조건 맞으니 패스지 뭐
            else:
                return False        
        return True
        

    def gradient(self, x, v): #current(x), value값이네
        grad = []       
        for i in range(len(x)):
            xCopy = x[:] #편미분 계산. 주어진게 x1 이라면 나머지는 상수취급. x1만 x1+델타 해주고 나머진 x2
        #x1만 바꿔보고, 또 x2만 delta만큼 변화 시켜보고, 또 다시 와서 x3만 또 변화 시켜보고
        #x가 5개 주어지잖아(Convex)
            xCopy[i] += self._dx
            df = self.evaluate(xCopy) - v #원래값은 바뀌지 않으니까 들고온고. evaluate 안써도 되잖아
            g = df / self._dx            
            grad.append(g)   #벡터 생성
        return grad         
       
    
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
          mutant = self.mutate(current, i, self._delta) #(현재 해당하는 값, 0번째 1번째, 더해주는값, problem) 이렇게 1개 찾음 #자기 함수 부를때 self 적어야.
          neighbors.append(mutant)
          mutant = self.mutate(current, i, -self._delta) #빼는값도 해줘야지
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
    
    
    
    def randomMutant(self,current):
        i = random.randint(0, len(current)-1) #steepest ascent 후보들 중에 하나 랜덤 뽑는다 생각해~ current가 5가 나올테니 인덱스로 적용시키기 위해 -1
        if random.uniform(0,1)>0.5: #1/2확률보다 크면
            d = self._delta
        else:
            d = -self._delta           
        return self.mutate(current, i, d) # Return a random successor
    
    def describe(self): #describeProbelm #p와 같은 내용을 위에서 정해줬으니, p를 이용할 필요가 없다. p[1]가 도메인에 관한걸 알고있잖아. 그럼 도메인에 관한걸 바로 써주면되지. p를 받아올필요 없지
        print()
        print("Objective function:")
        print(self._expression)   # Expression
        print("Search space:")
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1] 
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i])) 
    
#    def storeResult(self, solution, value): #최종 솔루션을 저장. #나중에 main에서 get, set을 이용하게 돼있으니까, 세팅을 해줘야한다.
#        self._solution = solution
#        self._value = value
    #parent에서 이미 해줬으니 그걸 쓰면 된다. 이거 이상 적을게 없잖아. 똑같은걸 다시 할필요 없어
    
    
    def report(self):    #solution은 이미 Problem에 정의됐잖아
        print()
        print("Average objective value: {0:,}".format(self._avgMinimum))
        # print("Solution found:")
        print("Best solution found:")
        print(self.coordinate())  # 변수가 있음 안되지. 밑에서 올려주잖아.
        # print("Minimum value: {0:,.3f}".format(self._value)) #minimum = self._value징
        print("Best minimum value: {0:,.3f}".format(self._bestMinimum))
        Problem.report(self) #super().report도 같다. #파이썬은 다중 상속이 되니까 이름 그대로 쓰는게 좋지 않을까.
        
    
    def coordinate(self):
        c = [round(value, 3) for value in self._bestSolution]
        return tuple(c)  # Convert the list to a tuple            
        
    
    
    
    
    
class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self) #Problem의 상속을 받고있으니. 상위꺼도 같이 당연히 호출해야
        
        self._numCities = 0
        self._locations = []
        self._distanceTable = []
    
    
    
    def setVariables(self,parameters):       
        # fileName = "problem/tsp" + input("Enter the filename of function: (30, 50, 100)") + ".txt"
        Problem.setVariables(self, parameters)
        infile = open(self._pFileName, 'r')
        # infile = open(fileName, 'r')
        
        self._numCities = int(infile.readline())
        self._locations = []
        line = infile.readline() 
        while line != '':
            self._locations.append(eval(line))
            line = infile.readline()
        infile.close()
        self._distanceTable = self.calcDistanceTable() #괄호안도 필요없징~
        #return numCities, locations, table
    
    
    
    def calcDistanceTable(self): ###
        table = []  #2d    
        locations = self._locations
        for i in range(self._numCities):
            row = [] #돌때마다 한줄이 초기화. 리스트 안에 리스트로.             
            
            for j in range(self._numCities): #tsp30.txt 이걸 표로 봐
                dx = locations[i][0] - locations[j][0]
                dy = locations[i][1] - locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2),1) #제곱의 루트 math.sqrt. 소수첫째자리까지 반올림.
                row.append(d)        
            table.append(row)   
    
        return table # A symmetric matrix of pairwise distances  
    
    
    def randomInit(self):
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init 
    
    def evaluate(self, current): 
        ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
       
        self._numEval += 1 
        
        n = self._numCities #도시수
        table = self._distanceTable #아까 distance 계산한거 2번째에 넣었잖아
        cost = 0
        
        for i in range(n-1):
            locFrom = current[i] #현재, 랜덤으로 섞인 table들의 거리 계산을 위해 좌표
            locTo = current[i+1] 
            cost += table[locFrom][locTo] #2d테이블 거리들 다 더해
        cost += table[current[n-1]][current[0]]    
        return cost
    
    
    
    def mutants(self,current): # Apply inversion
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors
    
    def inversion(self, current, i, j):  # Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy
    
    def randomMutant(self, current): # Apply inversion
        while True: #완전 랜덤하게 i,j를 두개를 뽑으니까. while이 있지만 이건 i가 j보다 작은거 찾으려 하는거고. 1개 뽑으면 끝.
            i, j = sorted([random.randrange(self._numCities)
                        for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy
    
    
    def describe(self): #describeProbelm
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()
    
 
    
    def report(self):   #오버라이딩 하고있는거다. 슈퍼클래스에 있는걸 안쓴다. 직접적으로 다 작성하되, 상속 받을것만 super(). 혹은 Problem. 으로 하면 되지
        print()        
        print("Average tour costs: {0:,}".format(round(self._avgMinimum)))
        print("Best of best order of visits:")
        self.tenPerRow()       # Print 10 cities per row, #self._solution 없애면 되겠네. 아래에서 해주니까.
        print("Best minimum tour cost: {0:,}".format(round(self._bestMinimum)))                     
        Problem.report(self)
        
    def tenPerRow(self):
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()