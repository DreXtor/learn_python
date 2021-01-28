import pygame
from pygame.constants import K_RIGHT

pygame.init()   # 초기화(반드시 필요!!)

# 화면 크기 설정
screen_width = 480      # 가로 크기
screen_height = 640      # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))    # 창 세팅

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")     # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기 : pygame.image.load(경로)
background = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/background.jpg")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/character.png")
character_size = character.get_rect().size   # 캐릭터 이미지 크기
character_width = character_size[0]           # 캐릭터 가로 크기
character_height = character_size[1]          # 캐릭터 세로 크기
character_X_position = (screen_width / 2)-(character_width / 2)    # 캐릭터의 X 좌표
character_Y_position = screen_height - character_height         # 캐릭터의 Y 좌표

# 이동할 좌표
to_X = 0
to_Y = 0

# 이동 속도
character_speed = 0.5

# 적 캐릭터
enemy = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size   # 적 이미지 크기
enemy_width = enemy_size[0]           # 적 가로 크기
enemy_height = enemy_size[1]          # 적 세로 크기
enemy_X_position = (screen_width / 2)-(enemy_width / 2)    # 적의 X 좌표
enemy_Y_position = (screen_height / 2) - (enemy_height / 2)       # 적의 Y 좌표


#  이벤트 루프가 계속 실행중이어야 창이 꺼지지않는다
# 이벤트 루프
running = True
while running:  # 게임이 진행중인가?
    dt = clock.tick(30)
    # 게임 화면 초당 프레임수를 설정 / '값이 없을때에는 최대 프레임을 출력하는듯 하다'
    # 캐릭터가 1초 동안에 100만큼 이동을 해야함
    # 10 fps : 1초 동안에 10번 동작! -> 1번에 몇만큼 이동해야할까? 10만큼! (10*10 = 100)
    # 20 fps : 1초 동안에 20번 동작! -> 1번에 몇만큼 이동해야할까? 5만큼! (20*5 = 100)
    # =========> 그러므로 이동값을 수정해주어야한다 !

    for event in pygame.event.get():        # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:       # 창이 닫히는 이벤트가 발생했는가?
            running = False                 # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:      # 키가 눌리면 명령 실행
            if event.key == pygame.K_LEFT:      # '왼쪽' 방향키가 눌리면
                to_X -= character_speed
            elif event.key == pygame.K_RIGHT:   # '오른쪽' 방향키가 눌리면
                to_X += character_speed
            elif event.key == pygame.K_UP:   # '위로' 방향키가 눌리면
                to_Y -= character_speed
            elif event.key == pygame.K_DOWN:   # '아래로' 방향키가 눌리면
                to_Y += character_speed

        if event.type == pygame.KEYUP:          # 키가 떨어지면
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:    # "왼쪽" 혹은 "오른쪽" 버튼이 떨어진면
                to_X = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:    # "위쪽" 혹은 "아래쪽" 버튼이 떨어진면
                to_Y = 0

    character_X_position += to_X * dt    # 캐릭터 'X position' 이동값 계산
    character_Y_position += to_Y * dt    # 캐릭터 'Y position' 이동값 계산

    # 가로 경계값 처리
    if character_X_position < 0:
        character_X_position = 0
    elif character_X_position > screen_width - character_width:
        character_X_position = screen_width - character_width

    # 세로 경계값 처리
    if character_Y_position < 0:
        character_Y_position = 0
    elif character_Y_position > screen_height - character_height:
        character_Y_position = screen_height - character_height

    # 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_X_position
    character_rect.top = character_Y_position

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_X_position
    enemy_rect.top = enemy_Y_position

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # screen.fill((0, 0, 255))               # 단색으로 배경 채우기
    screen.blit(background, (0, 0))         # 배경 그리기

    screen.blit(character, (character_X_position,
                            character_Y_position))  # 캐릭터 그리기

    screen.blit(enemy, (enemy_X_position,
                        enemy_Y_position))  # 적 그리기

    pygame.display.update()                 # 게임화면 다시 그리기 / 계속해서 그려줘야 보여진다


# pygame 종료
pygame.quit()
