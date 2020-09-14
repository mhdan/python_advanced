# some training and examples on namedtuple!!!!

from collections import namedtuple

# Car = namedtuple("car", "color speed")
# # Car = namedtuple("Car", ['color', 'speed'])
# my_car = Car('red', 100)
# print(my_car.color)
# print(my_car.speed)
# print(my_car)
# print(*my_car)  # '*' for unpacking the arguments!!!
# #
# # output: red
# # output: 100
# # output: car(color='red', speed=100)
# # output: red 100

# ###########

# print(my_car[0])
# print(tuple(my_car))
# #
# # output: red
# # output: ('red', 100)

###############################################

# # make class form tupple with desired methods
# Car = namedtuple('Car', "color speed")
# class MyCarWithMethods(Car):    # inherit from Car!!! so it require it's arguments!!!
#     def hexcolor(self):
#         if self.color == 'red':
#             return '#ff0000'
#         else:
#             return '#000000'

# c = MyCarWithMethods('red', 80)
# print(c.hexcolor())
# #
# # output: #ff0000

###############################################

# Car = namedtuple('Car', 'color speed')
# print(Car._fields)
# #
# # output: ('color', 'speed')

# # add 'charge' as tuple, to fields!!!
# ElectircCar = namedtuple('ElectricCar', Car._fields + ('charge',))
# my_eleccar = ElectircCar('blue', 60, 4000)
# print(my_eleccar)
# #
# # output: ElectricCar(color='blue', speed=60, charge=4000)

###############################################

Car = namedtuple("car", "color speed")
my_car = Car('red', 100)
print(type(my_car._asdict()))
print(my_car._asdict())
#
# output: <class 'dict'>
# output: {'color': 'red', 'speed': 100}

# ###########

new_car = my_car._replace(color='green')
print(new_car)
#
# output: car(color='green', speed=100)

# ###########

second_car = Car._make(['yellow', 160])     # it take iterable args!
print(second_car)
#
# output: car(color='yellow', speed=160)
