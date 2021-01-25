# 분기문
# if / elif / else
# case_01
weather = input("오늘 날씨는 어때요?")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("좋은하루 보내세요")

# case_02
temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요, 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요, 나가지 마세요")

-------------------------------------------------------------------------------------
반복문
for
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for n_waiting in range(5):      # range로 범위 지정 가능
    print("대기번호 : {0}".format(n_waiting))

starbucks = ["아이언맨", "토르", "그루트"]      # list 값도 반복할수있슴
for customer in starbucks:
    print("{0}손님, 커피나왔습니다.".format(customer))

-------------------------------------------------------------------------------------
# while
customer = "토르"
index = 5
while index >= 1:       # while (조건):     #조건이 만족할때까지 반복
    index -= 1
    if index == 0:
        print("커피 폐기합니다")
    else:
        print("{0}손님 커피가 준비되었습니다. 호출 {1}번 남았습니다".format(customer, index))

# 무한루프 (종료 : ctrl + c)
customer = "아이언맨"
index = 1               # 몇번 호출하는지 알아보기 위해 넣는다
while True:
    index += 1
    print("{0}손님 커피가 준비되었습니다. 호출 {1}번 남았습니다".format(customer, index))

case_03
customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}손님, 커피 준비되었습니다".format(customer))
    person = input("성함이 어떻게 되세요? ")
print("맛있게 드세요")

-------------------------------------------------------------------------------------
# continue 와 break:
absent = [2, 5]      # 결석
no_book = [7]       # 책 없음
for student in range(1, 11):
    if student in absent:
        continue        # 아래를 실행하지않고 다음 반복으로 넘어감
    elif student in no_book:
        print("수업 끝! {0}번, 교무실로 따라와.".format(student))
        break           # 반복문 탈출
    else:
        print("{0}번, 일어나서 책읽어보자.".format(student))

-------------------------------------------------------------------------------------
# 한줄로 끝내는 for문

# 출석번호가 1,2,3,4,5 에서 101,102,103,104,105 로 변경
student = [1, 2, 3, 4, 5]
print(student)
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
student = ["iron man", "thor", "i am groot"]
student = [len(i) for i in student]
print(student)

# 학생 이름을 대문자로 변환
student = ["iron man", "thor", "i am groot"]
student = [i.upper() for i in student]
print(student)
