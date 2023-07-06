from Problem import Numeric #우린 이것만 필요하다

def main():
    # Create an instance of numerical optimization problem
    p = Numeric() #인스턴스 생성 이렇게 바로 해버리네. p 인스턴스 만들었으니까 다 바까봐
    p.setVariable()  #createProblem을 이걸로
    # Call the search algorithm
    solution, minimum = steepestAscent(p) #p라는 인스턴스에 모든 정보가 다 들어가있다.
    # Show the problem and algorithm settings #출력파트. 이 아래.
    p.describe()  #describeProblem(p) p도 여전히 필요없다. 다 들어가있어.
    displaySetting(p) #안에 들어가보면 delta 값도 필요하고 하니까 일단 p 넣어보자. p에 delta값이 있다.
    # Report results
    p.storeResult(solution, minimum) #외부에서 steepest 돌린거니까, 업데이트 해줘야지. Problem.py의 solution, value에 업뎃해야 하니까. 그래서 storeResult를 만들어놨잖아
    
    p.report()


def steepestAscent(p): #p가 주어지면 전체적으로 반복 #얘는 주변 후보들 다 찾아봐
    current = p.randomInit() # 'current' is a list of values #시작점.->랜덤하게 뽑는다.
    valueC = p.evaluate(current) #p업새고
    while True:
        neighbors = p.mutants(current) #p없애고
        successor, valueS = bestOf(neighbors,p) #제일 좋은거 찾아내
        if valueS >= valueC: #현재 다음으로 가야할 후보를 찾았으니, 현재보다 좋아지는지 판단해야지. valueS(후보값) 이 valueC(현재값) 보다 좋으면 나빠지는거니 탈출.
            break
        else:
            current = successor #커런트를 석세서로 업뎃 해주고
            valueC = valueS #현재값을 후보로. 업데이트 된걸로 또 돌아주고.
    return current, valueC



def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = p.evaluate(best) #p없애고
    
    for i in range(1, len(neighbors)):
        newValue = p.evaluate(neighbors[i]) # p없애고
        if newValue < bestValue: 
            best = neighbors[i] 
            bestValue = newValue                    
    return best, bestValue


def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
   #print("Mutation step size:", p._delta)    #get, set 해줘야한다. 권장법이 아니다. 되긴된다
    print("Mutation step size:", p.getDelta()) #자바랑 달랑~~ public, private 이런게 구분이 안되니까. 
main()
