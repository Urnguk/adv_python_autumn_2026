# class Student:
#     name = "Vasya"
#     balance = 0
#     subjects = []
#
#     def scholarship(self):
#         self.balance += 5600
#
# a = Student()
# b = Student()
# c = Student()
# # print(a.name, a.balance)
# # a.name = "Ivan"
# # print(a.name)
# #
# # print(b.name)
# a.subjects = ["math", "biology"]
# b.subjects.append("physics")
# print(a.subjects, b.subjects, c.subjects)


# class X:
#     cnt = 0
#     def __init__(self):
#         X.cnt += 1
#
#     def active_instances(self):
#         return self.cnt
#
# a = X()
# print(a.active_instances())
# b = X()
# print(a.active_instances())
# print(b.active_instances())


# class Tree:
#     def __init__(self, tree_type, height, leaves=True, evergreen=True):
#         self.tree_type = tree_type
#         self.height = height
#         self.leaves = leaves
#         self.evergreen = evergreen
#
#     def grow(self):
#         self.height += 1
#
#     def winter(self):
#         if self.leaves and not self.evergreen:
#             self.leaves = False
#
#     def __str__(self):
#         return (f"This is tree of {self.tree_type} type with height = {self.height}, "
#                 f"currently leaves are {'on' if self.leaves else 'off'}")
#
# a = Tree("birch", 1, evergreen=False)
# b = Tree("fir", 5, False)
#
# a.grow()
# print(a.leaves)
# a.winter()
# print(a.leaves)
# print(a)

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self._len = 0
#
#     def append(self, value):
#         x = Node(value)
#         self._len += 1
#         if self.head is None:
#             self.head = x
#             self.tail = x
#             return
#         self.tail.next = x
#         self.tail = x
#
#     def __len__(self):
#         return self._len
#
#     def __getitem__(self, item):
#         curr = self.head
#         for i in range(item):
#             curr = curr.next
#         return curr.value
#
#     def __str__(self):
#         return f"[{', '.join(str(self[i]) for i in range(len(self)))}]"
#
#     def __add__(self, other):
#         if isinstance(other, LinkedList):
#             res = LinkedList()
#             for i in range(len(self)):
#                 res.append(self[i])
#             for i in range(len(other)):
#                 res.append(other[i])
#         elif isinstance(other, int):
#             res = LinkedList()
#             for i in range(len(self)):
#                 res.append(self[i])
#             res.append(other)
#         else:
#             raise TypeError(f"{other} is not of type LinkedList")
#         return res
#
#     def __radd__(self, other):
#         if isinstance(other, LinkedList):
#             res = LinkedList()
#             for i in range(len(other)):
#                 res.append(self[i])
#             for i in range(len(self)):
#                 res.append(other[i])
#         elif isinstance(other, int):
#             res = LinkedList()
#             res.append(other)
#             for i in range(len(self)):
#                 res.append(self[i])
#         else:
#             raise TypeError(f"{other} is not of type LinkedList")
#         return res
#
#
# A = LinkedList()
# A.append(1)
# A.append(3)
# A.append(-2)
# B = LinkedList()
# B.append(4)
# C = A + B
# print(C)
# C = C + 3
# C = 5 + C
# print(C)


class Base:
    def __init__(self):
        pass

    def func1(self):
        return 1

    def func2(self):
        return 2

    def __str__(self):
        return "база"


class Derived(Base):
    def func1(self):
        return 0

    def __str__(self):
        return "это " + super().__str__()

a = Derived()
print(a.func1(), a.func2(), a)




