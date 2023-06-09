from Problem import Tsp
LIMIT_STUCK = 100

def main():
    # Create an instance of TSP
    p = Tsp()    # 'p': (numCities, locations, distanceTable)
    p.setVariable()
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    p.describe
    displaySetting()
    # Report results
    p.storeResult(solution, minimum)
    p.report()
    





def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

# def randomMutant(current, p): # Apply inversion
#     while True: #완전 랜덤하게 i,j를 두개를 뽑으니까. while이 있지만 이건 i가 j보다 작은거 찾으려 하는거고. 1개 뽑으면 끝.
#         i, j = sorted([random.randrange(p[0])
#                        for _ in range(2)])
#         if i < j:
#             curCopy = inversion(current, i, j)
#             break
#     return curCopy

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")


main()
