# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#     남자 : 키(m) x 키(m) x 22
#     여자 : 키(m) x 키(m) x 21

# 조건 1 : 표중 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# -------------------------------------------------------------------------------------
# my_code       # 전역변수의 활용이 부족하여 심플하지 못했다
def std_weight(height, gender):
    height = height / 100       # cm -> m 단위로 변경

    # 남여 구분 조건문
    if gender == "남자":
        avr_weight = height * height * 22
    else:
        avr_weight = height * height * 21

    return avr_weight, height, gender


avr_weight, height, gender = std_weight(175, "남자")

avr_weight = round(avr_weight, 2)
height = int(height * 100)

print(f"{height}cm {gender}의 몸무게 평균은 {avr_weight}입니다")

# -------------------------------------------------------------------------------------
# sam_code
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print(f"{height}cm {gender}의 몸무게 평균은 {weight}입니다")
