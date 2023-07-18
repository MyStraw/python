
x=10
y=20        #주석은 샵으로
x+y

print(x+y)

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange"
print(fruits)

print()

num = 10
text = "apple"
print(str(num) + text)

print()

num = 10
float_num = float(num)
str_num = str(num)
bool_num = bool(num)

print(type(num))         # <class 'int'>
print(type(float_num))   # <class 'float'>
print(type(str_num))     # <class 'str'>
print(type(bool_num))    # <class 'bool'>


print()


# 산술연산자 사용 예제
a = 10
b = 3
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
print(c)  # 13 출력
print(d)  # 7 출력
print(e)  # 30 출력
print(f)  # 3.3333333333333335 출력
print(g)  # 1 출력

print()

# 멤버쉽 연산자 사용 예제
a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)  # True 출력
print(6 in a)  # False 출력
print("o" in b)  # True 출력
print("k" not in b)  # True 출력

print("------------------")

# 산술식 및 비교식 응용 예제
x = 10
y = 5
a = x + y
b = x - y
c = x * y
d = x / y

if a > c and b < d:  # a가 c보다 크고, b가 d보다 작은 경우
    print("a > c and b < d")  # 출력 안 됨
elif a < c or b > d:  # a가 c보다 작거나, b가 d보다 큰 경우
    print("a < c or b > d")  # "a < c or b > d" 출력
else:
    print("neither")  # 출력 안 됨

print("------------------")

# 문자열 출력 예제
print("Hello, world!")  # "Hello, world!" 출력
print("My name is John.")  # "My name is John." 출력
print('The "quick brown" fox jumps over the lazy dog.')  # 'The "quick brown" fox jumps over the lazy dog.' 출력
print("I'm a boy.")  # "I'm a boy." 출력
print("He said, \"Hello!\"")  # "He said, "Hello!"" 출력
print("10"+"20") #문자열 잇기  1020
print("abc " * 3) #문자열 3번 출력  abc abc abc

# 변수 출력 예제
x = 10
y = 5
z = x + y
print(x, y, z)  # 10 5 15 출력

print(10+20)  # 30

print(10/3)


print("------------------")


# 딕셔너리 출력 예제
person = {"name": "John", "age": 25, "city": "New York"}
print(person)  # {'name': 'John', 'age': 25, 'city': 'New York'} 출력

# 딕셔너리 값 출력 예제
print(person["name"])  # 'John' 출력
print(person["age"])  # 25 출력
print(person["city"])  # 'New York' 출력


print("------------------")

# % 연산자를 이용한 포매팅
name = "John"
age = 30
height = 175.5

print("My name is %s, I'm %d years old, and my height is %.1f." % (name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

print("------------------")
# 문자열
name = "John"
print("Hello, %s!" % name)

# 정수
num = 42
print("The answer is %d." % num)

# 실수
pi = 3.14159
print("Pi is approximately %.2f." % pi)

# 여러 개의 변수
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is %s %s and I am %d years old." % (first_name, last_name, age))

# 진수 변환
decimal_num = 42
binary_num = bin(decimal_num)
print("The decimal number %d is equal to the binary number %s." % (decimal_num, binary_num))



