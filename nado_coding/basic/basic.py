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
# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
# 조세호가 몇번째 칸에 타고있는가?
print(subway.index("조세호"))
# 하하 추가
subway.append("하하")
print(subway)
# 유재석과 조세호 사이에 정형돈 추가
subway.insert(1, "정형돈")  # 1번째 위치에 정형돈 추가
print(subway)
# 지하철에 있는 사람을 뒤에서부터 한명씩 꺼냄
print(subway.pop())
print(subway)
# 같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

# -------------------------------------------------------------------------------------
# 정렬
num_list = [4, 6, 2, 7, 87, 3]
num_list.sort()
print(num_list)
# 역순으로 정렬
num_list.reverse()
print(num_list)
# 전부 다 지우기
num_list.clear()
print(num_list)

# 확장
num_list = [4, 6, 2, 7, 87, 3]
mix_list = ["미니", 34, True]

num_list.extend(mix_list)
print(num_list)

# Dictionary - { keys : values} 로 표현
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))               # Dic.get(keys)
# print(cabinet.[5])                # 값이 없기떄문에 오류
print(cabinet.get(5))               # 값은 없지만 'None' 출력
print(cabinet.get(5, "Enable"))     # 값이 없을 경우 "Enable" 출력

print(3 in cabinet)                 # cabinet 안에 '3'이라는 key가 있는가? (boolean형 출력)
# cabinet[3] 안에 '유재석'이 value가 있는가? (boolean형 출력)
print("유재석" in cabinet[3])

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet)

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"              # "A-3" key값을 "김종국"으로 변경
cabinet["D-4"] = "조세호"              # "D-4" 라는 key값을 생성하고 "조세호"라는 Value를 추가
print(cabinet)

# 간 손님
del cabinet["A-3"]                    # "A-3" Key와 Value 삭제
print(cabinet)

# Keys만 출력
print(cabinet.keys())
# Values만 출력
print(cabinet.values())
# 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐전
cabinet.clear()
print(cabinet)

# -------------------------------------------------------------------------------------
# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")                # 값을 추가 변경할수 없다, (tuple' object has no attribute 'add')
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")         # 위의 추가방법보다 간단히 값을 만들수있다
print(type((name, age, hobby)))                    # tuple 타입으로 저장된다.

# -------------------------------------------------------------------------------------
# set : 집합
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

Java = {"유재석", "조세호", "정형돈"}
Python = set(["유재석", "김태호"])

# 교집합
print(Java & Python)
# 합집합
print(Java | Python)
# 차집합
print(Java - Python)
# Python 할수있는 사람이 늘어남
Python.add("양세형")
print(Python)
# Java 까먹음
Java.remove("조세호")
print(Java)

# -------------------------------------------------------------------------------------
# 자료구조의 변경
# 커피숍
menu = {"coffee", "milk", "juice"}
print(type(menu))

# 리스트 자료형으로 변경
menu = list(menu)
print(type(menu))
# 튜플 자료형으로 변경
menu = tuple(menu)
print(type(menu))
# 셋 자료형으로 변경
menu = set(menu)
print(type(menu))
