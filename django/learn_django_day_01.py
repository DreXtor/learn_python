#Django에 대하여
# *args (position argument) : 위치에 있는 단일(?)값을 넣을수 있다
# **kwargs (keyword argument) : 키워드(어떤 값?string?) 을 넣을수 있냐?(서치)

def plus(a,b,*args,**kwargs): 

	print(args)
	return a+b

plus(1,2,3,4,5,5,6,7,4)

# 겍체지향 언어(코드를 정리하는 방법)
# 하나의 블루프린트(청사진.설계도)로 여러개의 instance를 만들어 사용할수있다.


class CAR():
	
	def __init__(self, *args, **kwargs):
		self.wheel = 4

		self.color = kwargs.get("color", "black") # 값이 있으면 'color()', 없으면 'black' 반환
		self.price = kwargs.get("price", "$20") # 값이 있으면 'price()', 없으면 '$20' 반환

class SUV(CAR): #SUV라는 extend_class를 만들며 CAR의 정보는 그대로 상속된다
	
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs) #CAR 클래스의 '__init__' method를 가져오고 추가되는 정보들과 취합한다.
		self.size = kwargs.get("size", "tico") # 값이 있으면 'size()', 없으면 'tico' 반환


kia = CAR(color = "blue", price = "$40") #kia라는 instance의 "color","price" 값을 넣어준다.
print(kia.color, kia.price)

hyundai = CAR() #CAR class로 hyundai라는 instance를 만든다.
print(hyundai.color, hyundai.price)

range_rover = SUV(size = "big") #SUV class로 range_rover라는 instance를 만든다. 
range_rover.wheel = "4" #SUV class안에 wheel 이라는 속성을 추가한다.

print(range_rover.size , range_rover.wheel)
