class TailandTravel:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕 자유 여행 80만원")


# 모듈이 잘 작동하는지 확인하기
if __name__ == "__main__":
    print("ThailandTrip 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할때만 실행되요")
    trip_to = TailandTravel()
    trip_to.detail()
else:
    print("Tailand 외부에서 모듈 호출")
