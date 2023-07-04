from numeric import *

def main():
    # Create an instance of numerical optimization problem
    p = createProblem()    # 'p': (expr, domain) #첫단계. pseudo 코드 알고리즘 처럼
    # Call the search algorithm
    solution, minimum = steepestAscent(p) #직접 구현해야.
    # Show the problem and algorithm settings #출력파트. 이 아래.
    describeProblem(p) 
    displaySetting()
    # Report results
    displayResult(solution, minimum)


def steepestAscent(p): #p가 주어지면 전체적으로 반복 #얘는 주변 후보들 다 찾아봐
    current = randomInit(p) # 'current' is a list of values #시작점.->랜덤하게 뽑는다.
    valueC = evaluate(current, p) #p에 expression, 도메인이랑~ 들어가있다
    while True:
        neighbors = mutants(current, p) #주변의 후보'들'을 다 찾아본다.
        successor, valueS = bestOf(neighbors, p) #제일 좋은거 찾아내
        if valueS >= valueC: #현재 다음으로 가야할 후보를 찾았으니, 현재보다 좋아지는지 판단해야지. valueS(후보값) 이 valueC(현재값) 보다 좋으면 나빠지는거니 탈출.
            break
        else:
            current = successor #커런트를 석세서로 업뎃 해주고
            valueC = valueS #현재값을 후보로. 업데이트 된걸로 또 돌아주고.
    return current, valueC

def mutants(current, p): ### p에서 정보 끄집어내기
    neighbors=[]
    for i in range(len(current)): #커런트, 현재값이 갯수만큼 있을거니 current 넣어도 되겠네
        mutant = mutate(current, i, DELTA , p) #(현재 해당하는 값, 0번째 1번째, 더해주는값, problem) 이렇게 1개 찾음
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA , p) #빼는값도 해줘야지
        neighbors.append(mutant)
    return neighbors     # Return a set of successors

def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best,p) #첫번째 후보만 봤을때. 초기화 일단하고. (neighbor[0] 해도되고). 첫번째값만 해서 초기화
    
    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i],p) # 첫번째값 봤으니 두번째부터 봐야지(1부터 레인지 설정 해놨잖아 반복)
        if newValue < bestValue: #작은게 더 좋은거징~ 최소값 찾기 로직. 알잖아 이건ㅎ
            best = neighbors[i] #best 값도 넣어주고..
            bestValue = newValue
                    
    return best, bestValue


def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)
main()
