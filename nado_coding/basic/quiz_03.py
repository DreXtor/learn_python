# Quiz) 당신의 학교에서는 파이썬 코딩대회를 주최합니다
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게됩니다.
# 추첨프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# -------------------------------------------------------------------------------------
# 1st my code

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


# -------------------------------------------------------------------------------------
# 2nd my code

people = []

for n in range(20):     # 입력받은 숫자만큼 반복
    people.append(n+1)

shuffle(people)

chicken = sample(people, 1)
people.remove(chicken[0])
coupon = sample(people, 3)

print(f"--당첨자발표--\n 치킨 당첨자 : {chicken}\n 쿠폰 당첨자 : {coupon}\n--축하합니다--")


# -------------------------------------------------------------------------------------
# sam code

users = range(1, 21)    # 1부터 20까지 숫자 생성 (range타입으로 생성)
users = list(users)     # list 타입으로 생성

shuffle(users)

winners = sample(users, 4)  # 일단 4명을 뽑아버린다

print("--당첨자발표--")
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print("--축하합니다--")
