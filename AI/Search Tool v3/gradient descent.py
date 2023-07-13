from Problem import Numeric #우린 이것만 필요하다

def main():
    # Create an instance of numerical optimization problem
    p = Numeric() #인스턴스 생성 이렇게 바로 해버리네. p 인스턴스 만들었으니까 다 바까봐
    p.setVariable()  #createProblem을 이걸로
    # Call the search algorithm
    solution, minimum = gradientDescent(p) #p라는 인스턴스에 모든 정보가 다 들어가있다.
    # Show the problem and algorithm settings #출력파트. 이 아래.
    p.describe()  #describeProblem(p) p도 여전히 필요없다. 다 들어가있어.
    displaySetting(p) #안에 들어가보면 delta 값도 필요하고 하니까 일단 p 넣어보자. p에 delta값이 있다.
    # Report results
    p.storeResult(solution, minimum) #외부에서 steepest 돌린거니까, 업데이트 해줘야지. Problem.py의 solution, value에 업뎃해야 하니까. 그래서 storeResult를 만들어놨잖아
    p.report()

def gradientDescent(p):   
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
    return current, valueC

def takeStep(self, current, i, d): #gradient로 현재 시점에서 좋은걸 가면 되니까 bestof는 필요없다.
    curCopy = current[:]
    domain = self._domain       
    l = domain[1][i]    
    u = domain[2][i]     
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy





def displaySetting(p):
    print()
    print("Search algorithm: Gradient - descent Hill Climbing")
    print()
   #print("Mutation step size:", p._delta)    #get, set 해줘야한다. 권장법이 아니다. 되긴된다
    print("step size:", p.getAlpha()) #자바랑 달랑~~ public, private 이런게 구분이 안되니까. 
main()
