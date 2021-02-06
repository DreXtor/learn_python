from random import *


class Unit():
    def __init__(self, name, hp, speed) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}이 사망하였습니다".format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage) -> None:
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
            self.name, location, self.damage))

# 마린 클래스


class Marine(AttackUnit):
    def __init__(self) -> None:
        super().__init__("마린", 40, 1, 5)

    # 스팀팩 : 일정시간동안 이동 및 공격속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 0:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. [체력 10 감소]".format(
                self.name))
        else:
            print("{0} : 체력이 부족합니다.".format(
                self.name))

# 탱크 클래스


class Tank(AttackUnit):
    # 시즈모드 : 이동불가, 공격력 증가
    seize_developed = False     # 시즈모드 개발 여부

    def __init__(self) -> None:
        super().__init__("탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if self.seize_developed == False:
            return  # 아무 동작없이 나가겠다
        else:
            if self.seize_mode == False:
                self.damage *= 2
                self.speed = 0
                print("{0} : 시즈모드를 사용합니다. [공격력 : {1}]".format(
                    self.name, self.damage))
                self.seize_mode = True
            else:
                self.damage /= 2
                self.speed = 1
                print("{0} : 시즈모드를 해제합니다. [공격력 : {1}]".format(
                    self.name, self.damage))
                self.seize_mode = False


# 공중 유닛


class Flyable:
    def __init__(self, flying_speed) -> None:
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(
            name, location, self.flying_speed))

# 공중 공격 유닛


class FlyingAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed) -> None:
        AttackUnit.__init__(self, name, hp, 0, damage)      # 지상 스피드 = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 레이스 클래스
class Wraith(FlyingAttackUnit):
    def __init__(self):
        super().__init__("래이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 설정합니다".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")
    print("[Plyaer]님이 퇴장하셨습니다.")


# 게임 시작
game_start

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2대 생성
t1 = Tank()
t2 = Tank()

# 레이스 1대 생성
w1 = Wraith()

# 유닛 일괄관리 (리스트)
unit_list = []
unit_list.append(m1)
unit_list.append(m2)
unit_list.append(m3)
unit_list.append(t1)
unit_list.append(t2)
unit_list.append(w1)

# 전군 이동
for unit in unit_list:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("시즈모드가 개발되었습니다")

# 공격 모드 준비(마린 : 스팀팩 , 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in unit_list:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in unit_list:
    unit.attack("5시")

# 전군 피해
for unit in unit_list:
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()
