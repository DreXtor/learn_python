import pygame
import os

from pygame import image
from pygame.constants import KEYDOWN, K_LEFT, K_RIGHT, K_SPACE

##########################################################################################################################
# 기본 초기화 (반드시 해야하는것들)
pygame.init()   # 초기화(반드시 필요!!)

# 화면 크기 설정
screen_width = 640      # 가로 크기
screen_height = 480      # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))    # 창 세팅

# 화면 타이틀 설정
pygame.display.set_caption("MS_AP")     # 게임 이름

# FPS
clock = pygame.time.Clock()
##########################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)    # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")        # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size      # 스테이지 사이즈 반환(가로, 세로)
stage_height = stage_size[1]            # 캐릭터를 스테이지 위에 올려놓기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size      # 캐릭터 사이즈 반환(가로, 세로)
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - stage_height - character_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 볼 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path, "ball_160.png")),
    pygame.image.load(os.path.join(image_path, "ball_80.png")),
    pygame.image.load(os.path.join(image_path, "ball_40.png")),
    pygame.image.load(os.path.join(image_path, "ball_20.png"))
]

# 공 크기에 따른 위에서 떨어지는 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

# 공의 속성값 정의
balls = []

balls.append({
    "pos_x": 50,   # 공의 x 좌표
    "pos_y": 50,   # 공의 y 좌표
    "img_index": 0,    # 공의 종류
    "to_x": 3,      # 공의 x 축 이동방향
    "to_y": -6,      # 공의 y 축 이동방향
    "init_speed_y": ball_speed_y[0]    # 공의 y 최초 속도 정의
})

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                character_to_x -= character_speed
            elif event.key == K_RIGHT:
                character_to_x += character_speed
            elif event.key == K_SPACE:      # 무기 발사
                weapon_x_pos = character_x_pos + \
                    (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # sam_code
    # weapons =[ [w[0], w[1] - weapon_speed] for w in weapons] => 무기 위치 위로
    # weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0 ] => 천장(0) 아래의 값만 리스트에 넣겠다
    # 무기를 위로 쏘아 올리고 천장(0)에 닿으면 리스트 값을 없앤다
    for location_weapon in weapons:
        if location_weapon[1] > 0:
            location_weapon[1] -= weapon_speed
        else:
            weapons.remove(location_weapon)

    # 공 위치 정의
    # enumerate는 키값과 그에 해당하는 밸류를 반환한다.
    for ball_index, ball_val in enumerate(balls):
        ball_x_pos = ball_val["pos_x"]
        ball_y_pos = ball_val["pos_y"]
        ball_image_index = ball_val["img_index"]

        ball_size = ball_images[ball_image_index].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을때 공 이동방향 변경
        if ball_x_pos < 0 or ball_x_pos > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
        # 세로 위치
        if ball_y_pos >= screen_height - stage_height - ball_height:
            # 공이 바닥에 닿으면 최초 y속도로 변경
            ball_val["to_y"] = ball_val["init_speed_y"]
        else:
            ball_val["to_y"] += 0.5

        # 앞에 정의한 ball_x_pos = ball_val["pos_x"]의 ball_x_pos의 값을 변경해줘도 된다고 생각했었는데
        # ball_x_pos는 하나의 변수일뿐 ball딕셔너리 안의 값을 수정하지는 못한다.
        # 그러므로 ball_val["pos_x"]의 값을 수정해주어야 ball 딕셔너리 안에 값이 수정되는것이었다 !
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌 처리

    # 5. 화면에 그리기 (순서대로 뒤에 그려진다)
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for ball_index, ball_val in enumerate(balls):
        ball_x_pos = ball_val["pos_x"]
        ball_y_pos = ball_val["pos_y"]
        ball_image_index = ball_val["img_index"]
        screen.blit(ball_images[ball_image_index], (ball_x_pos, ball_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
