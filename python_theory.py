'''
# 타입을 알아보는 명령어를 기억하자
a_float = 0.2321
a_string = 'hello'
print(type(a_float))
print(type(a_string))
'''

'''
#list에 대하여
days = ['Mon','Tue','Wed','Thur','Fri']
days_02 = ['Mon , Tue , Wed , Thur , Fri']

print("Mon" in days)

print(len(days),len(days_02))
days.copy() #Ccibal 이건 어떻게 쓰는거야?
print(days)
days.clear()
print(days)
'''

'''
#Tuple에 대하여
#수정할수없는것 / 누구도 바꿀수없다

days_tuple = ('Mon','Tue','Wed','Thur','Fri')

print(type(days_tuple))
'''
''''
#Dictionary에 대하여
#'Key : Value'를 모아놓은 사전이라고 생각하자
 
Wonki = {
    "name": "wonki",
    "first name": "Lee",
    "age": 31,
    "Is he Genius?": True,
    "Needs": ["Sucess", "Money", "Home", "etc"]
}

print(Wonki)
print(Wonki["first name"])
print(type(Wonki["Is he Genius?"]))

Wonki["happy"] = True

print(Wonki)
'''

'''
#function에 대하여
# 어떠한 행동(Behavior)을 반복해서 사용가능하도록 정의하는것?

age = 54.55532341
print(age)
print(type(age))
n_age = int(age)
print(n_age)
print(type(n_age))

'''


# define_function과 argument(인자)
'''
def say_hello():
	print("Hello")

say_hello()

def say_hello_arg(who,age):
	print("hello", who, "who" , age , "year old")

say_hello_arg('mini',28)

def plus(a,b):
	print(a + b)

plus(2,44)
'''

# return
'''
def r_plus(a,b):
	return a + b

r_result = r_plus(1,5)

print(r_result)
'''

# code_callenge_01

'''
def plus(a, b):
	return int(a) + int(b)

def minus(a,b):
	return int(a) - int(b)

def multiply(a, b):
	return int(a) * int(b)

def divide(a, b):
	return int(a) / int(b)

def reminder(a, b):
	return int(a) % int(b)

def negated(a):
	return -int(a)

def powerd(a, b):
	return int(a) ** int(b)

r_plus = plus(3,"2")
r_minus = minus(3,"2")
r_mult = multiply("3","2")
r_divide = divide(3,"2")
r_reminder = reminder("3","2")
r_negate = negated("2")
r_powerd = powerd(3,"2")

print(r_plus)
print(r_minus)
print(r_mult)
print(r_divide)
print(r_reminder)
print(r_negate)
print(r_powerd)

'''
## for..in 문에 대하여
'''
days = ("mon", "thu", "wed","thur","fri")

for day in days:
	if day is "fri":
		print(day)
		print("reset")
	else:
		print(day)
'''

## module과 import
## module is 기능들을 모아놓은것
## import 할때 from을 사용하여 필요한 기능만을 가져오는것이 메모리에 부담을 줄여줄수있다.
'''
from math import fsum

print(fsum([1,2]))
'''