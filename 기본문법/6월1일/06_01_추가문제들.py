num1 = int(input("첫 번째 정수를 입력하세요:"))
num2 = int(input("두 번째 정수를 입력하세요:"))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division:.2f}")

print("사과쇼핑몰")


사과수=int(input("사과개수?"))
사과가격=int(input("가격?"))
부과세=int(input("부가세율?"))/100

price = 사과수*사과가격
tax = price*부과세
total = price+tax

print(f"결제금액 : {total:.0f}원")
        
        
