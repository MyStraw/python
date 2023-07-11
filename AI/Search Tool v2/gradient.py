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


def gradient(curr, next, p):
    return (p.evaluate(next) - p.evaluate(curr)) / p.getDelta() * 10


def gradientDescent(p):
    delta = p.getDelta() / 10
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        past = current[:]
        for i in range(len(current)):
            successor = p.mutate(current, i, delta)
            grad = gradient(current, successor, p)
            current[i] = current[i] - delta * grad #업데이트룰. x <- x-af(x)
        valueC = p.evaluate(successor)
        grad = gradient(past, current, p)
        if abs(grad) == 0:
            break
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
