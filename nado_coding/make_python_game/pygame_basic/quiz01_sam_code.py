import pygame
from pygame.constants import K_LEFT, K_RIGHT
import random
##########################################################################################################################
# 기본 초기화 (반드시 해야하는것들)
pygame.init()   # 초기화(반드시 필요!!)

# 화면 크기 설정
screen_width = 480      # 가로 크기
screen_height = 640      # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))    # 창 세팅

# 화면 타이틀 설정
pygame.display.set_caption("Quiz")     # 게임 이름

# FPS
clock = pygame.time.Clock()
##########################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들
background = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/background.jpg")

character = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/character.png")
character_size = character.get_rect().size   # 캐릭터 이미지 크기
character_width = character_size[0]           # 캐릭터 가로 크기
character_height = character_size[1]          # 캐릭터 세로 크기
character_X_position = (screen_width / 2)-(character_width / 2)    # 캐릭터의 X 좌표
character_Y_position = screen_height - character_height         # 캐릭터의 Y 좌표

enermy = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/enermy_01.png")
enermy_size = enermy.get_rect().size   # 캐릭터 이미지 크기
enermy_width = enermy_size[0]           # 캐릭터 가로 크기
enermy_height = enermy_size[1]          # 캐릭터 세로 크기
enermy_X_position = random.randint(
    0, screen_width - enermy_width)    # 캐릭터의 X 좌표
enermy_Y_position = 0         # 캐릭터의 Y 좌표
enermy_speed = 10

to_x = 0
character_move = 1

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                to_x -= character_move
            elif event.key == K_RIGHT:
                to_x += character_move
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                to_x = 0

    character_X_position += to_x * dt

    if character_X_position < 0:
        character_X_position = 0
    elif character_X_position > screen_width - character_width:
        character_X_position = screen_width - character_width

    enermy_Y_position += enermy_speed

    if enermy_Y_position > screen_height:
        enermy_Y_position = 0
        enermy_X_position = random.randint(
            0, screen_width - enermy_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_X_position
    character_rect.top = character_Y_position

    enermy_rect = enermy.get_rect()
    enermy_rect.left = enermy_X_position
    enermy_rect.top = enermy_Y_position

    if character_rect.colliderect(enermy_rect):
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_X_position, character_Y_position))
    screen.blit(enermy, (enermy_X_position, enermy_Y_position))

    pygame.display.update()

pygame.quit()
