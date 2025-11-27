# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 떄
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# import theater_module as md
# md.price(3)
# md.price_morning(4)
# md.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_morning(5)

from theater_module import price, price_morning
price(5)
price_morning(3)
# price_soldier(4)

from theater_module import price_soldier as ps
ps(5)