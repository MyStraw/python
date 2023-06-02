#1
second = int(input("초를 입력하세요"))

minute = second//60
secondd = second%60

print(f"{minute} 분 {secondd}초")

print("----------------------------------")

#2
m=int(input("분을 입력하세요."))

d=m//(24*60)
h=(m//60)%24
m=m%60

print(f"{d}일 {h}시간 {m}분")

print("----------------------------------")

#3
money = 5000000
rate = 0.05

print(f"원리금의 합계 = {money*(1+rate)**5:,.2f} 원")
print("----------------------------------")


#4
n=100
total = n*(n+1)/2
print(f"{total:.0f}")
print("----------------------------------")

#5
포도=75
딸기=113.5

포도개수=int(input("포도개수?"))
딸기개수=int(input("딸기개수?"))

print(f"{포도*포도개수 + 딸기*딸기개수:,.0f}g")

print(f"총 무게는 {총무게}g입니다.")