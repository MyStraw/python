from queue import Queue
import numpy as np

K= int(input())

que = Queue()

seroTotal = 0
seroMax = 0
garoTotal = 0
garoMax = 0

# melon = [[0] * 2 for _ in range(6)]
melon = np.zeros((6, 2), dtype=int)
four = [0] * 4

for i in range(6):
    data = input().split()
    compass = int(data[0])
    length = int(data[1])

    melon[i][0] = compass
    melon[i][1] = length

    if (melon[i][0] == 3 | melon[i][0] == 4):
        seroTotal += melon[i][1]
    if (melon[i][0] == 1 | melon[i][0] == 2):
        garoTotal += melon[i][1]    
    que.put(length)    

seroMax = int(seroTotal // 2)
garoMax = int(garoTotal // 2)

lastIndex = 0

for i in range(5):
    if((melon[i][1] == seroMax and melon[i + 1][1] == garoMax) or (melon[i][1] == garoMax and melon[i + 1][1] == seroMax)):
        lastIndex = i + 1
if ((melon[5][1] == seroMax and melon[0][1] == garoMax) or (melon[5][1] == garoMax and melon[0][1] == seroMax)):
		lastIndex = 0
if (lastIndex != 5): 
	for i in range(lastIndex):
		que.put(que.get());                
for i in range(4):
       four[i] = que.get()
result = ((seroMax * garoMax) - (four[1] * four[2])) * K   
print(result)    