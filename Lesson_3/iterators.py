class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def append(self, value):
        x = Node(value)
        self._len += 1
        if self.head is None:
            self.head = x
            self.tail = x
            return
        self.tail.next = x
        self.tail = x

    def __len__(self):
        return self._len

    def __getitem__(self, item):
        curr = self.head
        for i in range(item):
            curr = curr.next
        return curr.value

    def __str__(self):
        return f"[{', '.join(str(self[i]) for i in range(len(self)))}]"

    def __add__(self, other):
        if isinstance(other, LinkedList):
            res = LinkedList()
            for i in range(len(self)):
                res.append(self[i])
            for i in range(len(other)):
                res.append(other[i])
        elif isinstance(other, int):
            res = LinkedList()
            for i in range(len(self)):
                res.append(self[i])
            res.append(other)
        else:
            raise TypeError(f"{other} is not of type LinkedList")
        return res

    def __radd__(self, other):
        if isinstance(other, LinkedList):
            res = LinkedList()
            for i in range(len(other)):
                res.append(self[i])
            for i in range(len(self)):
                res.append(other[i])
        elif isinstance(other, int):
            res = LinkedList()
            res.append(other)
            for i in range(len(self)):
                res.append(self[i])
        else:
            raise TypeError(f"{other} is not of type LinkedList")
        return res

    def __iter__(self):
        return LinkedListIterator(self.head)


class LinkedListIterator:
    def __init__(self, head):
        self.curr = head

    def __next__(self):
        if self.curr is None:
            raise StopIteration
        res = self.curr.value
        self.curr = self.curr.next
        return res

A = LinkedList()
A.append(1)
A.append(2)
A.append(13)

# for x in A:
#     print(x)

# try:
#     it = iter(A)
#     while True:
#         x = next(it)
#         print(x)
# except StopIteration:
#     pass


# with open("tmp.txt") as file:
#     for line in file:
#         print(line.strip())


# def fib():
#     a, b = 0, 1
#     while True:
#         yield b
#         a, b = b, a + b

# for x in fib():
#     print(x)


# def cycle_3():
#     i = 0
#     cnt = 0
#     while True:
#         yield i
#         i += 1
#         i %= 3
#         cnt += 1
#         if cnt == 1000:
#             return

# for x in cycle_3():
#     print(x)
#
# t = cycle_3()
# print(t, type(t))


# def sum_list(A, B):
#     i = 0
#     for i in range(min(len(A), len(B))):
#         yield A[i] + B[i]
#
# for i in sum_list([3, 5, 7], [0, 2]):
#     print(i)




def double_cycle(n, m):
    for i in range(n):
        for j in range(m):
            yield i, j

for i, j in double_cycle(5, 2):
    print(i, j)
    if i + j == 5:
        break

