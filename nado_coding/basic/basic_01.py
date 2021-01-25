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

# -------------------------------------------------------------------------------------
# 랜덤함수
print(int(random() * 45) + 1)
print(randrange(1, 46))      # 1이상 46미만의 임의의 값 생성
print(randint(1, 45))         # 1이상 45이하의 임의의 값 생성

# -------------------------------------------------------------------------------------
# 문자열

jumin = "990120-1234567"

print(f"성별 : {jumin[7]")

문자열
python = "Python is Amazing"
print(python.lower())                       # 모든 글자를 소문자로 출력
print(python.upper())                       # 모든 글자를 대문자로 출력
# python의 [0]위치의 글자가 대문자니? (True 반환)
print(python[0].isupper())
print(len(python))                          # python 리스트의 길이를 출력
print(python.replace("Python", "Java"))     # 'Python' 을 'Java' 로 대치시킨다

index = python.index("n")                   # 'n' 문자의 위치를 구한다
print(index)
index = python.index("n", index + 1)        # 'n' 문자의 다음 위치를 구한다
print(index)

print(python.find("Java"))                  # 리스트에 없는 것을 찾을 때 '-1'을 반환한다 (에러 X)
print(python.index("Java"))                 # 리스트에 없는 것을 찾을 때 에러가 난다.

print(python.count("n"))                    # 리스트 안에 'n'이 몇개 있는지 카운트한다.

# -------------------------------------------------------------------------------------
# 문자열 포맷 : 문자를 출력하는 방법
print("a" + "b")
print("a", "b")
# 방법 1
print(("나는 %d살입니다") % 30)
print("나는 %s을 좋아해요." % "파이썬")
print(" Apple 은 %c로 시작해요." % "A")

# -------------------------------------------------------------------------------------
# 탈출문법
# %s
print(("나는 %s살입니다") % 30)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
# \" \" : 문장내 따옴표 사용가눙
print("저는 \"이원기\" 입니다")
# \\ : 문장내에서 \ 사용
print("C\\User\\work")
# \r : 커서를 맨앞으로 이동하여 덮어쓰기
print("Red Apple\rPine")
# \b : 백스페이스
print("Redd\b Apple")
# \t : 탭
print("Red\tApple")

# -------------------------------------------------------------------------------------
