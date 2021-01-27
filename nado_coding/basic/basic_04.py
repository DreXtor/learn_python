# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("{0}원이 출금되었습니다, 잔액은 {1}원입니다.".format(money, balance - money))
    else:
        print("잔액이 부족합니다, 현재 잔액은 {0}원입니다.".format(balance))

    return balance

    def withdraw_night(balance, money):     # 저녁에 출금
    comission = 100     # 수수료
    print("{0}원이 출금되었습니다. 현재 잔액은 {1}입니다.".format(
        money + comission, balance - money - comission))

    return balance, comission


balance = 0     # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
balance = withdraw(balance, 5000)
balance, withdraw_money = withdraw_night(balance, 500)
print("수수료는 {0}원입니다".format(withdraw_money))

# -------------------------------------------------------------------------------------
# 힘수 기본값 설정
# 위, 아래 함수 출력값이 같다.


def profile(name, age, main_lang):
    print(f"이름 : {name} , 나이 : {age} , 언어 : {main_lang}")


profile("유재석", 17, "python")
profile("김태호", 17, "python")


def profile(name, age=17, main_lang="python"):
    print(f"이름 : {name} , 나이 : {age} , 언어 : {main_lang}")


profile("유재석")
profile("김태호")

-------------------------------------------------------------------------------------
# 가변인자


def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    # end = " " 은 줄 바꾸지 않고 이어서 출력해준다.
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")


def profile(name, age, *languege):      # *languege 로 입력받은만큼 출력한다
    # end = " " 은 줄 바꾸지 않고 이어서 출력해준다.
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lan in languege:
        print(lan, end=" ")
    print()     # 줄바꿈에 사용


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")

# -------------------------------------------------------------------------------------
# 지역변수와 전역변수
gun = 10


def checkpoint_return(gun, soldiers):       # 총 개수 , 경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun      # 지역변수인 '남은 총의 개수'를 밖으로 던져준다


print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)     # return 된 남은 총의 개수를 전역변수로 계산한다.
print("남은 총 : {0}".format(gun))
