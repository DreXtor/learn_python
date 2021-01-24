import pygame

pygame.init()   # 초기화(반드시 필요!!)

# 화면 크기 설정
screen_width = 480      # 가로 크기
screen_height = 640      # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))    # 창 세팅

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")     # 게임 이름

#  이벤트 루프가 계속 실행중이어야 창이 꺼지지않는다
# 이벤트 루프
running = True
while running:  # 게임이 진행중인가?
    for event in pygame.event.get():        # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:       # 창이 닫히는 이벤트가 발생했는가?
            running = False                 # 게임이 진행중이 아님

# pygame 종료
pygame.quit()
