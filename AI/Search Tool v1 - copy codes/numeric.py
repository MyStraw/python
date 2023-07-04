import random
import math

DELTA = 0.01   
LIMIT_STUCK = 100 #상수는 뭐 안쓰더라도 이 코드있다고 상관있나.
NumEval = 0    

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