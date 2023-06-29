import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations
#global 변수

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


def createProblem(): ### #문제에 대한 정의. #여기부터 작성 해야하네?
    ## Read in an expression and its domain from a file.   
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'up' is a list of upper bounds of the varaibles.
    fileName = "problem/" + input("Enter the filename of function:") + ".txt"
    infile = open(fileName,'r')
    expression = infile.readline() #txt파일 공식적힌 첫째줄
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
    domain = [varName, low, up]
    
    return expression, domain


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


def randomInit(p): ### #쓰고자 하는거 => random.uniform(_,_) p는 expression, domain 갖고있다. 즉 범위가 있다. 범위안에서
    #값을 뽑아내야지. 반복문 써야겠죠?
    domain = p[1] #어퍼 바운드, 로우 바운드를 줘야겠지~? 이건 도메인 내에 있잖아~ -30~30 까지인거. 다시 끄집어내
    low = domain[1]
    up = domain[2]
    init = []
    for i in range(len(low)): #5개인줄은 알고 있지만은~ low 개수 넣어주면 되겠지? up도 되겠고
        r = random.uniform(low[i], up[i]) #low도 리스트고 up도 리스트니까 [i]
        init.append(r)
        
    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p): #노션 보면서 하셈 -> 함수값 구하는건 여기서 했당~
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval #이건 왜 해줬지? 젤위에 해줬는데? global은 계속 함수 내부에서 바뀌니까 바꿔야 할땐 이렇게 선언해줘야한다.
    #안해주면 안바뀐다.
    
    NumEval += 1 #Evaluation Funcion을 얼마나 수행했는지 카운트~ Global 변수로 초기값 0으로 해줬다.
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain #p에서 추출한게 x1, x2~x5 정보만. 이거에 대한 값을 알고싶오. 이값이 들어갔을때의 f(x)값을 알고싶은거. 이 x값들은 current에 들어가있다
    #x1 = 2 엔터, x2 = 3엔터, ~~x5까지 치고나면 x1+x2+x3+x4+x5 
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i]) #varNames(x1,x2,x3~~) , str(currentp[i]) = 값. 실수(숫자)다. str로 바꿔줘야한다.
        #그럼 윗줄 전체가 String이 된다 ex) x1=3.2 이런게 assignment에 만들어진다.
        exec(assignment) #스테이트먼트를 실행을 하고 반복.
    return eval(expr) #함수값 리턴~ 현재값은 알고있엉~


def mutants(current, p): ### p에서 정보 끄집어내기
    neighbors=[]
    for i in range(len(current)): #커런트, 현재값이 갯수만큼 있을거니 current 넣어도 되겠네
        mutant = mutate(current, i, DELTA , p) #(현재 해당하는 값, 0번째 1번째, 더해주는값, problem) 이렇게 1개 찾음
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA , p) #빼는값도 해줘야지
        neighbors.append(mutant)
    return neighbors     # Return a set of successors


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal #i는 몇번째 변수인지
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best,p) #첫번째 후보만 봤을때. 초기화 일단하고. (neighbor[0] 해도되고). 첫번째값만 해서 초기화
    
    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i],p) # 첫번째값 봤으니 두번째부터 봐야지(1부터 레인지 설정 해놨잖아 반복)
        if newValue < bestValue: #작은게 더 좋은거징~ 최소값 찾기 로직. 알잖아 이건ㅎ
            best = neighbors[i] #best 값도 넣어주고..
            bestValue = newValue
                    
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple
main()
