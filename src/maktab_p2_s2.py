# numbers = [(1, 5), (4, 2), (5, 3), (7, 9), (3, 6), (2, 8)]
# numbers.sort()
# print(numbers)
# # output: [(1, 5), (2, 8), (3, 6), (4, 2), (5, 3), (7, 9)]

###############################################

# **** lambda function is anounymous func in python!!!
# **** we use it in some case like key functions!!

# numbers = [(1, 5), (4, 2), (5, 3), (7, 9), (3, 6), (2, 8)]
# print(sorted(numbers, key=lambda x: x[1]))
# # output: [(4, 2), (5, 3), (1, 5), (3, 6), (2, 8), (7, 9)]

###############################################

# **** map(func, iterable)
# **** the map function execute given function on given iterable
# **** it return one map object, for showing it we shoule cast it to list!!!

# **** in lambda func we can use 'if' in short form like this!!!
# **** lambda z: x if 'condition else y

# numbers = [(1, 5), (4, 2), (5, 3), (7, 9), (3, 6), (2, 8)]
# temp1 = map(lambda x: 'big' if x[1]>5 else 'small', numbers)
# print(temp1)
# temp1_list = list(temp1)
# print(temp1_list)
# print(numbers)  # the orginal list keep safe!
# #
# # output: <map object at 0x7f1885689c40>
# # output: ['small', 'small', 'small', 'big', 'big', 'big']
# # output: [(1, 5), (4, 2), (5, 3), (7, 9), (3, 6), (2, 8)]

###############################################

# **** filter(func, iterable)
# **** the filter function execute function on given iterable
# **** the filter pass the items that the condition on them return True!!! (mesl <qhif> amal mikoneh!!!)
# **** it return one filter object, for showing it we should cast it to list !!!

# numbers = [(1, 5), (4, 2), (5, 3), (7, 9), (3, 6), (2, 8)]
# temp1 = filter(lambda x: x[1] % 2 == 0, numbers)
# print(temp1)
# temp1_list = list(temp1)
# print(temp1_list)
# print(numbers)  # the orginal list keep safe!
# # #
# # # output: <filter object at 0x7fb450269c40>
# # # output: [(4, 2), (3, 6), (2, 8)]
# # # output: [(1, 5), (4, 2), (5, 3), (7, 9), (3, 6), (2, 8)]

###############################################

# **** generatore functions in python with "yield"
# **** "yield" is same as "return", but the fuction will be generator function!
# **** it remember the previous state and continue to next "yield"
# **** it is good for case tha we work with huge data or call with unlimited or unknown args!!!

# def firstTon(n):
#     # i = 0
#     # while i < n:
#     #     yield i
#     #     i += 1
#     for num in range(0, 10):
#         yield num

# print(firstTon(10))
# # output : <generator object firstTon at 0x7ff7c4356eb0>

# # we can use func generatore only with iterables
# for i in firstTon(10):
#     print(i)

###############################################

# class Person:
#     count = 0   # this is static variable!!! (class variable)

#     # constructor of this calss (in python it defines with "__init__")
#     # all class methodes in python get "self" parameter!!!
#     def __init__(self, name, age):
#         # instance variable should refrence with "self."
#         self.name = name
#         self.age = age
#         # static variable should refrence with "class name."
#         Person.count += 1

#     # this is static method in python and it doesn't get "self" parameter!!!
#     # the "@..." is anotating and it is optional!!
#     @staticmethod
#     def get_count():
#         return Person.count

#     # all class methodes in python get "self" parameter!!!
#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     def info(self):
#         print("the name is %s and age is %i"
#               % (self.get_name(), self.get_age()))


# jadi = Person("jadi mirmirani", 40)
# print("age -> %i" % (jadi.get_age()))
# jadi.info()
# print(Person.get_count())

# mohammad = Person("mohammad ziaei", 22)
# print("this person is me and my name is %s and age is %i"
#       % (mohammad.get_name(), mohammad.get_age()))
# mohammad.info()

###############################################

# class Computer:
#     counter = 0

#     def __init__(self, cpu, ram, hard):
#         Computer.counter += 1
#         self.cpu = cpu
#         self.ram = ram
#         self.hard = hard

#     def get_value(self):
#         return self.cpu + self.ram + self.hard

#     # "__del__(self)" function will call automaticly when we use "del" on something!!!
#     # alse python garbage collectore always when the program finished, call "__del__" for each instance!!
#     def __del__(self):
#         Computer.counter -= 1
#         print("this computer deleted!!!")


# # with this syntax we can use inheritance
# class Laptop(Computer):
#     def __init__(self, cpu, ram, hard, vazn):
#         # now with this syntax we first call super constructore (yadet nare constructor super())
#         # second we can add some additional paramerters to it.
#         super().__init__(cpu, ram, hard)
#         self.vazn = vazn

#     def get_value(self):
#         return (self.cpu + self.ram + self.hard + self.vazn) * 1.5


# pc1 = Computer(5, 6, 1)
# print(pc1.get_value())

# notebook1 = Laptop(7, 16, 0.5, 2)
# print(notebook1.get_value())
# print(Computer.counter)
# del notebook1
# print(Computer.counter)
# # after the program finished, garbage collectore run "__del__" for pc1 instance too!!!

###############################################

# **** this code has Pseudo code and it is just useful example for OOP !!!
class Device:
    counter = 0

    def __init__(self, name, ip, mac):
        self.name = name
        self.ip_address = ip
        self.mac = mac
        Device.counter += 1
        # result = ping to the self.ip_address to check the status
        if result:
            self.status = 'active'
        else:
            self.status = 'unknown'

    def get_status(self):
        # return the status base on the ping and accessbility
        pass


class Tv(Device):
    counter = 0

    def __init__(self, name, ip, mac):
        super().__init__(name, ip, mac)
        Tv.counter += 1

    def turn_on(self):
        # connect to the self.ip_address and turn it on !!!
        pass

    def turn_off(self):
        # connect to the self.ip_address and turn it off !!!
        pass


class Thermo(Device):
    counter = 0

    def __init__(self, name, ip, mac):
        super().__init__(name, ip, mac)
        Thermo.counter += 1

    def get_temperature(self):
        # read temperature and return it's result!!!
        pass


class Smart_Tv(Tv):
    counter = 0

    def __init__(self, name, ip, mac, os):
        super().__init__(name, ip, mac)
        self.os = os
        Smart_Tv.counter += 1

    def update_os(self):
        # update the os and return the result!!!
        pass


my_tv = Smart_Tv("sony", 198168001, "adfeXXh", "android")
my_tv.update_os()
