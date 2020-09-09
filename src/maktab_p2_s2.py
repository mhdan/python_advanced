# numbers = [(1, 5), (4, 2), (5, 3), (7, 9), (3, 6), (2, 8)]
# numbers.sort()
# print(numbers)
# # output: [(1, 5), (2, 8), (3, 6), (4, 2), (5, 3), (7, 9)]

###############################################

##**** lambda function is anounymous func in python!!!
##**** we use it in some case like key functions!!

# numbers = [(1, 5), (4, 2), (5, 3), (7, 9), (3, 6), (2, 8)]
# print(sorted(numbers, key=lambda x: x[1]))
# # output: [(4, 2), (5, 3), (1, 5), (3, 6), (2, 8), (7, 9)]

###############################################

##**** map(func, iterable)
##**** the map function execute given function on given iterable
##**** it return one map object, for showing it we shoule cast it to list!!!

##**** in lambda func we can use 'if' in short form like this!!!
##**** lambda z: x if 'condition else y

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

##**** filter(func, iterable)
##**** the filter function execute function on given iterable
##**** the filter pass the items that the condition on them return True!!! (mesl <qhif> amal mikoneh!!!)
##**** it return one filter object, for showing it we should cast it to list !!!

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

##**** generatore functions in python with "yield"
##**** "yield" is same as "return", but the fuction will be generator function!
##**** it remember the previous state and continue to next "yield"
##**** it is good for case tha we work with huge data or call with unlimited or unknown args!!!

def firstTon(n):
    # i = 0
    # while i < n:
    #     yield i
    #     i += 1
    for num in range(0, 10):
        yield num

# for i in firstTon(10):
#     print(i)

print(firstTon(10))
print(firstTon(10))
for i in firstTon(10):
    print(i)














