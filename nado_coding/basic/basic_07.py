# 예외처리

try:
    print("나누기 전용 계산기입니다.")
    num = []
    num.append(int(input("첫번째 숫자를 입력하세요 : ")))
    num.append(int(input("첫번째 숫자를 입력하세요 : ")))
    num.append(num[0]/num[1])
    print("{0} / {1} = {2}".format(num[0], num[1], num[2]))

except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:    # 모든 예외를 처리하며 무슨 에러인지 알려준다
    print("알 수 없는 에러가 발생하였습니다")
    print("에러 : {0}".format(err))
