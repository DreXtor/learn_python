# 연산자
from random import *
from math import *

print(3**3)     # 3^3 제곱
print(10 % 3)     # 나머지
print(16//3)    # 몫
print(abs(-19))  # 절대값
print(pow(4, 2))  # 4^2 제곱
print(max(5, 12))  # 최대값
print(min(5, 12))  # 최소값
print(round(3.14))  # 반올림

print(floor(4.99))  # 내림
print(ceil(3.14))  # 올림
print(sqrt(16))  # 제곱근

# 랜덤함수
print(int(random() * 45) + 1)
print(randrange(1, 46))      # 1이상 46미만의 임의의 값 생성
print(randint(1, 45))         # 1이상 45이하의 임의의 값 생성

# 문자열

jumin = "990120-1234567"

print(f"성별 : {jumin[7]")
