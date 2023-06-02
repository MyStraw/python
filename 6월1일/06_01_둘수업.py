# 식별 연산자 사용 예제
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # False 출력
print(a is not b)  # True 출력
print(a is c)  # True 출력
print(b is not c)  # True 출력

#같은 주소를 가리키는 동일한 객체냐? 묻는거


print("--------------------")
pi = 3.14159265

print("pi = %.2f" % pi)  # 출력 결과: "pi = 3.14"
#소수점 찍고 2자리만 표시해주겠다.

print("pi = %10.2f" % pi)  # 출력 결과: "pi =       3.14"
#앞에 10자리 할애하고, 소수점 2자리 찍겠다.


print("--------%연산------------")

# format() 메소드를 이용한 포매팅
name = "John"
age = 30
height = 175.5

print("My name is {}, I'm {} years old, and my height is {:.1f}.".format(name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

print("--------format------------")
# 인덱스를 이용한 대입
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is {1} {0} and I am {2} years old.".format(last_name, first_name, age))
print("My name is {0} {1} and I am {2} years old.".format(last_name, first_name, age))

print("----f-string----------------")
## f-string을 이용한 문자열 포매팅
name = "John"
age = 30
height = 175.5

print(f"My name is {name}, I'm {age} years old, and my height is {height:.1f}.")
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

print("-----------------------")

name = 'Tom'
age = 20
apple = 3
orange = 2
banana = 1

result = 1.23
score = 90

num1 = 10
num2 = 20
addition = num1 + num2


print("My name is {0} and I am {1} years old.".format(name, age))

print(f"I have {apple} apples, {orange} oranges, and {banana} banana.")

print("The result is %.2f." % result)

print(f"Your score is {score}%")

print(f"{num1} + {num2} = {num1+num2}")
#중괄호 안에 다 묶어서 넣어. 원하는거
print("-------------")


