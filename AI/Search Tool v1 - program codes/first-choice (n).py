import random
import math

DELTA = 0.01   # Mutation step size
LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement #정말 나아지지 않는지 최대횟수. 랜덤.
NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)


def createProblem(): ### 똑같은 수치문제니까. 읽어오고 변수 만들고 하는건 똑같다. #최소값 찾는 알고리즘만 달라
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


def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of values
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK: #랜덤하게 일단 1개 썩세스 선택 하고, 좋아지기만 하면 업데이트
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC: #얘는 주변에 1개 선택. 좋아지면. 즉 작아지면 좋아지는 방향. 그럼 업데이트
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC


def randomInit(p): ###
    domain = p[1] 
    low = domain[1]
    up = domain[2]
    init = []
    for i in range(len(low)): 
        r = random.uniform(low[i], up[i]) 
        init.append(r)
    
    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain: [varNames, low, up]
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


def randomMutant(current, p): ### #딱 1개만 뽑아내는거. steepest ascent의 mutant는 모든 후보들 다 뽑아내는거;
    i = random.randint(0, len(current)-1) #steepest ascent 후보들 중에 하나 랜덤 뽑는다 생각해~ current가 5가 나올테니 인덱스로 적용시키기 위해 -1
    if random.uniform(0,1)>0.5: #1/2확률보다 크면
        d = DELTA
    else:
        d = -DELTA    
#    d = random.uniform(-DELTA, DELTA) #이건 내가 한겅    
    return mutate(current, i, d, p) # Return a random successor


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

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
    print("Search algorithm: First-Choice Hill Climbing")
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
