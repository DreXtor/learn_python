# 20개의 댓글을 담을 배열
# 랜덤함수중 1등 먼저 뽑고(shuffle n choice) 그 다음 3명 추첨(for?)
# 중복되지 않게 할것 (뽑히면 배열(리스트)에서 삭제하면될듯)

from random import *

people = []     # 참여한 인원수

k = input('몇명?:' "")

for n in range(int(k)):     # 입력받은 숫자만큼 반복
    people.append(n+1)      # people 리스트에 'n+1' 값 추가

shuffle(people)             # people 리스트 섞기

chicken = choice(people)    # chicken 당첨자 1명 추첨
people.remove(chicken)      # chicken 당첨자 people 리스트에서 제외

coupon = []                 # coupon 리스트 생성

for n in range(3):          # 3번 반복
    pick = choice(people)   # 1명씩 추첨
    coupon.append(pick)     # coupon 리스트에 추가
    people.remove(pick)     # 당첨자 people 리스트에서 삭제

print(chicken, coupon)      # 당첨자 출력
