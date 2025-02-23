# from math import sin
# a = []
# b = []
# c = []
# read1 = 18025
# read2 = 36021
# for i in range(4):
#     print('vernier 1:')
#     tr = read1 - int(input())
#     a += [tr]
# for i in range(4):
#     print('vernier 2:')
#     tr = read2 - int(input())
#     b += [tr]
# for i in range(4):
#     c += [(a[i] + b[i])/2]
# print(c)
# from math import *
# a = []
# for i in range(4):
#     deg = int(input())
#     min = float(input())
#     a += [sin(radians((min / 60 + deg + 60)/2))*0.5]

# print(a)

a = int(input())
a = a<<2
print(a)
a = a>>2
print(a)
a = ~a
print(a)