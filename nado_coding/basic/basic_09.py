# from basic_09_example.VietnamTrip import VietnamTravel
# import basic_09_example.TailandTrip

# trip_to_t = basic_09_example.TailandTrip.TailandTravel()
# trip_to_t.detail()

# trip_to_v = VietnamTravel()
# trip_to_v.detail()

# # *을 사용하려면 패키지 안에 __init__에 __all__을 추가하여야한다.
# from basic_09_example import *
# trip_to_t = TailandTrip.TailandTravel()
# trip_to_t.detail()

#####################################################################
# 패키지 및 모듈 위치 확인
import inspect
import random

print(inspect.getfile(random))
