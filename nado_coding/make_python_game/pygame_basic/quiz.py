# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오
"""
[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능 (o)
2. 똥은 화면 가장 위에서 떨어짐. x좌표는 매번 랜덤으로 설정 (O)
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐 (O)
4. 캐릭터가 똥과 충돌하면 게임 종료
5. fps 는 30으로 고정
"""

import pygame
from random import *
from pygame.constants import K_LEFT, K_RIGHT
##########################################################################################################################
# 기본 초기화 (반드시 해야하는것들)
pygame.init()   # 초기화(반드시 필요!!)

# 화면 크기 설정
screen_width = 480      # 가로 크기
screen_height = 640      # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))    # 창 세팅

# 화면 타이틀 설정
pygame.display.set_caption("DDong Game")     # 게임 이름

# FPS
clock = pygame.time.Clock()
##########################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/background.jpg")

# 캐릭터 이미지 정보
character = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/character.png")
character_width = character.get_width()
character_height = character.get_height()
character_X_position = screen_width / 2 - character_width / 2
character_Y_position = screen_height - character_height

# 적 이미지 정보
enermy = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/enermy_01.png")
enermy_width = enermy.get_width()
enermy_height = enermy.get_height()
enermy_X_position = randint(0, screen_width - enermy_width)
enermy_Y_position = 0

To_x = 0    # 캐릭터 x축 이동값 계산
character_move = 0.5
enermy_down = 0.7


running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 3. 게임 캐릭터 위치 정의(움직임 포함, 입력에 따라)
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                To_x -= character_move
            elif event.key == K_RIGHT:
                To_x += character_move

        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or K_RIGHT:
                To_x = 0

    character_X_position += To_x * dt

    if character_X_position < 0:
        character_X_position = 0
    elif character_X_position > screen_width - character_width:
        character_X_position = screen_width - character_width

    if enermy_Y_position <= screen_height:
        enermy_Y_position += enermy_down * dt
    else:
        enermy_Y_position = 0
        enermy_X_position = randint(0, screen_width - enermy_width)
    # 4. 충돌 처리
    # 위치 기반

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_X_position, character_Y_position))
    screen.blit(enermy, (enermy_X_position, enermy_Y_position))

    pygame.display.update()

pygame.quit()
