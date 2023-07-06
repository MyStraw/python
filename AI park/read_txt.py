infile = open('textfile.txt', 'r', encoding='UTF-8')

firstName = 'George'

for s in infile:
    #print(s) #이것만 하면 한칸씩 더 띄워진다.
    #print(s, end='')
    #print(s.rstrip()) #줄바꿈도 없애준다 strip는. print는 기본이 \n 이니까.
    
    #if s.startswith(firstName + ' '):
    #    print(s.rstrip())
    pass #암것도 안한다~
print(s.rstrip()) #pass 있으면 에러 안나는데 pass 없으니까 에러
#for에서 실행한게 아무것도 없. for 안에 있으면 가능.
#pass 하면 for랑 상관없는 녀석이 됨
infile.close() #반드시 해줘야한다. 안그럼 붙잡고 있는게 된다.