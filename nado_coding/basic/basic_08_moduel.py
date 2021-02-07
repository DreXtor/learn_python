# 모듈

# 영화관 모듈
def price(people):
    print("{0}분, 일반 관람 요금은 {1}입니다".format(people, people*10000))


def price_mornig(people):
    print("{0}분, 조조 할인 요금은 {1}입니다".format(people, people*6000))


def price_soldier(people):
    print("{0}분, 군인 할인 요금은 {1}입니다".format(people, people*4000))
