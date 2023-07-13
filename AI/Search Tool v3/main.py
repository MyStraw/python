from Problem import *
from optimizer import *

def main(): #키보드 임포트는 별로 안해. 마우스도. 입출력을 매번 알고리즘 input으로 적을거야? file로 open 하자. 대부분 이래(이건 너무 점프)
    p, pType = selectProblem() #pType: 1(Numeric), 2(Tsp)
    alg = selectAlgorithm(pType)    
    alg.run(p) #다 오브젝트.    
    # solution, minimum = alg.run(p)  #storeResult()를 main에서 안쓰고 계산해주는 곳에서. 리턴을 안하고.
    p.describe()  
    alg.displaySetting()   
    # p.storeResult(solution, minimum)  #storeResult()를 main에서 안쓰고 계산해주는 곳에서. 리턴을 안하고.
    p.report()

def selectProblem():  
    print("Select the problem type: ")
    print(" 1. Numeric")
    print(" 2. Tsp")
    pType = int(input("Enter the number: "))   
    if pType == 1:
        p= Numeric()
    elif pType == 2:
        p= Tsp()
    else:    
        print("1,2중에 하라니까 진쨔")           
        raise Exception #raise 로 예외 던지기.
    p.setVariables()    
    return p, pType

    
def selectAlgorithm(pType):
    print()
    print("Select the algorithm: ")
    print(" 1. Steepest Ascent")
    print(" 2. First Choice")
    if(pType == 1):
        print(" 3. Gradient Descent")      

    aType = int(input("Enter the number: "))
    
    optimizers = {1:'SteepestAscent' , 2:'FirstChoice' , 3:'GradientDescent', 4:'Stochastic'}    
    alg = eval(optimizers[aType] + '()') #키값에 따라 value가 나와야. 키는 aType에 다 들어가있다. optimizers[aType] 이것만 하면 string이 된다.
    #그냥 string을 원하는게 아니라 실행하는게 할당되어야... 즉 "SteepestAscent()" 라는 글자가 아니라 SteepestAscent()라는 오브젝트가 되어야하니까.
       
    alg.setVariables(pType)    
    return alg
main()
