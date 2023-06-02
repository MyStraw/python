# 사용자로부터 숫자를 입력받아, 홀수인지 짝수인지 판별하기
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")


#num이 10보다 큰지 판별하여, True이면 "10보다 큽니다"를, False이면 "10보다 작거나 같습니다"를 출력

num = 10
result = "10보다 큽니다" if num > 10 else "10보다 작거나 같습니다"
print(result)


#한줄 if문. if 앞부분이 참일때 조건. else 뒷부분이 아닐때 조건. 
string = input("문자열을 입력하세요: ")
length = len(string) if string else 0 #if가 string(true) 일땐 length가 string의 길이, 아니면 0
print("문자열의 길이는", length, "입니다.")



#변수 a와 b 중 값이 큰 변수를 출력하는 프로그램
a = 10
b = 20
result = a if a > b else b #a>b 가 참이면 a, 거짓이면 b. 가볍게 한줄로
print(result)


#세 개의 수 중 가장 작은 수를 출력하는 프로그램

a = 10
b = 20
c = 5
min_value = a if a < b and a < c else (b if b < c else c)
print("가장 작은 수는", min_value, "입니다.")



#입력한 값이 양수, 음수, 0인지 판별하는 프로그램

num = int(input("숫자를 입력하세요: "))
sign = "양수" if num > 0 else ("음수" if num < 0 else "0")
print(sign)




#사용자로부터 입력받은 수가 양수인 경우에만 제곱근을 구하고, 그 외에는 "잘못된 입력입니다."라는 메시지를 출력하는 프로그램
import math

num = float(input("양수를 입력하세요: "))

result = math.sqrt(num) if num > 0 else "잘못된 입력입니다."

print("결과: ", result)

