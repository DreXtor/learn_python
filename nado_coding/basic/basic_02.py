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
