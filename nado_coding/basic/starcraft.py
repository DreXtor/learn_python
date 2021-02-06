# # 마린 : 공격 유닛, 군인. 총을 쏠수있슴

# name = "마린"       # 유닛의 이름
# hp = 40            # 유닛의 체력
# damage = 5          # 유닛의 공격력

# print(f"{name} 유닛이 생성되었습니다")
# print(f"체력 {hp}, 공격력 {damage}")

# # 탱크 : 공격 유닛, 탱크. 포를 쏠수 있는데, 일반모드 / 시즈모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print(f"{tank_name} 유닛이 생성되었습니다")
# print(f"체력 {tank_hp}, 공격력 {tank_damage}")


# def attack(name, location, damage):
#     print(f"{name} : {location}방향의 적에게 {damage}의 피해를 입혔습니다.")


# attack(name, 5, damage)
# attack(tank_name, 11, tank_damage)

# # 그런데 유닛이 계속해서 추가되면 하나하나 복붙해야하는 어려움이 있다.
# # 그래서 class의 개념을 쓰자 !

########################################################################################


# class Unit():
#     def __init__(self, name, hp, damage) -> None:
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#         print(f"{self.name}유닛이 생성되었습니다")
#         print(f"체력은 {self.hp}이고 공격력은 {self.damage}입니다")


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 50, 25)

# wraith2 = Unit("빼앗은 레이스", 50, 25)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("빼앗은 레이스는 클로킹 상태입니다")

########################################################################################
# # 메소드

# class Unit():
#     def __init__(self, name, hp, damage) -> None:
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#         print(f"{self.name}유닛이 생성되었습니다")
#         print(f"체력은 {self.hp}이고 공격력은 {self.damage}입니다")


# class AttackUnit():
#     def __init__(self, name, hp, damage) -> None:
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
#             self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0}의 데미지를 입었습니다.".format(damage))
#         self.hp -= damage
#         print("현재 체력은 {0}입니다.".format(self.hp))
#         if self.hp <= 0:
#             print("{0}이 사망하였습니다".format(self.name))


# firebat1 = AttackUnit("파이어뱃", 50, 25)
# firebat1.attack("5시")

# firebat2 = AttackUnit("파이어뱃", 50, 25)
# firebat2.damaged(25)
# firebat2.damaged(25)

########################################################################################
# 상속
class Unit():
    def __init__(self, name, hp, speed) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage) -> None:
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{0}의 데미지를 입었습니다.".format(damage))
        self.hp -= damage
        print("현재 체력은 {0}입니다.".format(self.hp))
        if self.hp <= 0:
            print("{0}이 사망하였습니다".format(self.name))

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


valture = AttackUnit("벌쳐", 80, 10, 20)

battlcruiser = FlyingAttackUnit("배틀크루저", 500, 25, 3)

valture.move("11시")
battlcruiser.move("9시")
