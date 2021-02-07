# 모듈 호출

# 일반 호출
from basic_08_moduel import price_soldier as ps
from basic_08_moduel import price, price_mornig
from basic_08_moduel import *
import basic_08_moduel as mv
import basic_08_moduel

basic_08_moduel.price(3)
basic_08_moduel.price_mornig(4)
basic_08_moduel.price_soldier(5)

# 별명 붙여서 호출

mv.price(3)
mv.price_mornig(4)
mv.price_soldier(5)

# 모듈명 안쓰고 사용할수있게 호출
price(3)
price_mornig(4)
price_soldier(5)

# 필요한 함수만 모듈에서 호출
price(3)
price_mornig(4)

# 필요한 함수에 별명을 붙여서 호출
ps(5)
