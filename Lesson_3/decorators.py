# def time_decorator(func):
#     import time
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         return result, end_time - start_time
#     return wrapper
#
# @time_decorator
# def prime(value):
#     div = 2
#     while div ** 2 <= value:
#          if value % div == 0:
#              return False
#          div += 1
#     return True
#
#
# print(prime(120000001))


# from functools import cache
#
# @cache
# def fib(n):
#     if n in (0, 1):
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(500))


class Vector_3d:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self.y = y
        self.z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        self._x = value

    def __len__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    @staticmethod
    def dist(vector_1, vector_2):
        return ((vector_1.x - vector_2.x) ** 2 + (vector_1.y - vector_2.y) ** 2 + (vector_1.z - vector_2.z) ** 2) ** 0.5

# def distance(a, b):
#     ...

# a = Vector_3d(1, 2, 3)
# b = Vector_3d(4, 5, 6)
# print(a.dist(b))

a = Vector_3d(1, 2, 3)
print(a.x)
a.x = "and"



