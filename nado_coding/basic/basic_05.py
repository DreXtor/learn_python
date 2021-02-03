import sys
print("Python", "Java", file=sys.stdout)    # 정상 출력
print("Python", "Java", file=sys.stderr)    # 에러로 출력

# 출력 포맷
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject, score)
    # ljust(숫자) : 숫자만큼 공간확보라고 왼쪽정렬하겠다
    print(subject.ljust(8), str(score).rjust(4), sep=" : ")

# 은행 대기순번표
# 001, 002, 003....
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))    # zfill(숫자) : '0'을 숫자만큼 출력

# 사용자 입력값은 항상 문자열(str)이다
answer = input("아무값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")


# 출력 예제
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10 자리 공간을 확보
# (빈칸 : 자리에 들어가는 것으로 공간채움 , ">" =오른쪽 정렬 , "10" = 10자리 확보)
print("{0: >10}".format(500))
# 양수일땐 +로 표시, 음수일땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
# 3자리마다 콤마 찍어주기
print("{0:,}".format(1000000000000))
# 3자리마다 콤마 찍어주기 , +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))
# 3자리마다 콤마 찍어주기 , +- 부호도 붙이기 , 자릿수 확보하기
# 돈이 많으면 행복하니까 ^로 빈공간 채워주기
print("{0:^<+30,}".format(10000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 2자릿수까지만 출력
print("{0:.2f}".format(5/3))
