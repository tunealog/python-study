# Basic of Python

# Title : Modules
# Date : 2020-07-04
# Creator : tunealog

import theater_module
import theater_module as mv
from theater_module import *
from theater_module import price, price_morning
from theater_module import price_soldier as price

# import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

# import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# from theater_module import price, price_morning
price(3)
price_morning(4)
# price_soldier(5)

# from theater_module import price_soldier as price
price(5)
