#성적 계산기"를 작성하세요
# 사용자로부터 국어, 영어, 수학 세 과목의 성적을 입력받아, 각 과목의 평균 점수와 총 평균 점수를 계산한 후, 학점을 출력하는 프로그램을 작성하세요.
# 평균 점수는 소수점 둘째자리까지 출력합니다.
# 총 평균 점수는 국어: 40%, 영어: 40%, 수학: 20%로 가중치를 부여하여 계산합니다.
# 총 평균 점수가 90점 이상인 경우 "A", 80점 이상인 경우 "B", 70점 이상인 경우 "C", 60점 이상인 경우 "D", 60점 미만인 경우 "F"를 출력합니다.





국어 = int(input("국어점수 입력하셈"))
영어 = int(input("영어점수 입력하셈"))
수학 = int(input("수학점수 입력하셈"))

평균 = (국어+영어+수학)/3

총평균 = 국어*0.4 + 영어 * 0.4 + 수학*0.2

grade = ["A","B","C","D","F"]

if 총평균 >= 90:
    print(f"학점{grade[0]}")    
    학점 = 'A'
elif 총평균 >= 80 :
    print(f"학점{grade[1]}")
    학점 = 'B'
elif 총평균 >= 70 :
    print(f"학점{grade[2]}")
    학점 = 'C'
elif 총평균 >= 60 :
    print(f"학점{grade[3]}")  
    학점 = 'D'    
else:
    print(f"학점{grade[4]}")   
    학점 = 'F' 
    
결과 = f"\n[성적결과]\n국어:{국어}, 영어:{영어}, 수학:{수학}\n평균점수:{총평균:.2f}\n학점:{학점}"
print(결과)