# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# # [코드]
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass

#     def show_detail(self):
#         pass

# my code
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(
            f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")


gangnam_house = House("강남", "아파트", "매매", "10억", "2010년")
mapo_house = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa_house = House("송파", "빌라", "월세", "500/50", "2000년")
print("총 3대의 매물이 있습니다.")
gangnam_house.show_detail()
mapo_house.show_detail()
songpa_house.show_detail()


# sam code
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(
            f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")


houses = []
gangnam_house = House("강남", "아파트", "매매", "10억", "2010년")
mapo_house = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa_house = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(gangnam_house)
houses.append(mapo_house)
houses.append(songpa_house)

print("총 3대의 매물이 있습니다.")
for house in houses:
    house.show_detail()
