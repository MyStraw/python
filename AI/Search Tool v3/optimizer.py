from setup import Setup


class HillClimbing:
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0
        self._limitStock = 100
    
    def run(self):
        pass
    
    def displaySetting(self):
        if self._pType == 1: #Numeric 일때
            print()
            print("Mutation step size:", self._delta) #이거 p.getDelta 또 이렇게 가져와야해? 겟알파 계속 이런걸로 해야돼?
            #Problem과 main간에 있어야한다. 이거 두개의 상위클래스로. Setup라는 상위클래스로 하나 만들어서. 돌고 돌아왔다.
            
            
    def setVariables(self, pType):
        self._pType = pType    
    

     
class SteepestAscent(HillClimbing):
    #init 메소드 무조건 써야하는데 이건 안써도 돼. 안쓰면 오버라이딩 안하고. 바로 parent것만 불르는거.
    #init 안써도 HillClimbing꺼 가져온다.
    def run(self, p):
        current = p.randomInit() # 'current' is a list of values #시작점.->랜덤하게 뽑는다.
        valueC = p.evaluate(current) #p업새고
        while True:
            neighbors = p.mutants(current) #p없애고
            successor, valueS = self.bestOf(neighbors,p) #제일 좋은거 찾아내
            if valueS >= valueC: #현재 다음으로 가야할 후보를 찾았으니, 현재보다 좋아지는지 판단해야지. valueS(후보값) 이 valueC(현재값) 보다 좋으면 나빠지는거니 탈출.
                break
            else:
                current = successor #커런트를 석세서로 업뎃 해주고
                valueC = valueS #현재값을 후보로. 업데이트 된걸로 또 돌아주고.
        p.storeResult(current, valueC) 
        #return current, valueC #storeResult()를 main에서 안쓰고 계산해주는 곳에서. 리턴을 안하고.
    
    def bestOf(self, neighbors, p): ###
        best = neighbors[0]
        bestValue = p.evaluate(best) #p없애고
        
        for i in range(1, len(neighbors)):
            newValue = p.evaluate(neighbors[i]) # p없애고
            if newValue < bestValue: 
                best = neighbors[i] 
                bestValue = newValue                    
        return best, bestValue
    
    def displaySetting(self): #오버라이딩.
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")              
        HillClimbing.displaySetting(self)
        
        
class FirstChoice(HillClimbing):
    def run(self,p):
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStock: #랜덤하게 일단 1개 썩세스 선택 하고, 좋아지기만 하면 업데이트
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC: #얘는 주변에 1개 선택. 좋아지면. 즉 작아지면 좋아지는 방향. 그럼 업데이트
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        p.storeResult(current, valueC) 
        #return current, valueC

    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        HillClimbing.displaySetting(self)
        print("Max evaluations with no improvement: {0:,} iterations".format(self._limitStock))
    
    
class GradientDescent(HillClimbing):    
    def run(self,p):   
        current = p.randomInit() 
        valueC = p.evaluate(current)
        while True:        
            successor = p.takeStep(current, valueC) #이미 계산 했는데.. 값만 전달하면 되겠네
            valueS = p.evaluate(successor)       
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC) 
        #return current, valueC

    def takeStep(self, current, i, d): #gradient로 현재 시점에서 좋은걸 가면 되니까 bestof는 필요없다.
        curCopy = current[:]
        domain = self._domain       
        l = domain[1][i]    
        u = domain[2][i]     
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy

    def displaySetting(self):
        print()
        print("Search algorithm: Gradient - descent Hill Climbing")
        print()
        print("Update rate:", self._alpha)
        print("Increment for calculating derivatives: ", self._dx)