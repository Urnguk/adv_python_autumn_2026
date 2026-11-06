import turtle

# t = turtle.Turtle()
# t.speed(0)
# t.shape("turtle")
# t.fd(100)
# t.lt(90)
# t.fd(50)
# t.rt(45)
# t.color("#00a9a6")
# t.fd(200)
# t.pu()
# t.goto(0,0)
# t.right(180)
# t.pd()
# t.fd(30)
#
# turtle.done()

# colors = [
#     "#FF0000",
#     "#FFA500",
#     "#FFFF00",
#     "#00FF00",
#     "#00BFFF",
#     "#0000FF",
#     "#8B00FF"
# ]
# R = 200
# r = 10
# t = turtle.Turtle()
# t.width(r + 1)
# t.speed(0)
#
# for x in colors:
#     t.color(x)
#     t.pu()
#     t.goto(R, 0)
#     t.pd()
#     t.lt(90)
#     t.circle(R, 180)
#     t.lt(90)
#     R -= r
# t.pu()
# t.goto(1000, 0)
# t.color("white")
# t.pd()
# t.lt(180)
# t.forward(2000)
# turtle.done()


# def coh(t, l, n):
#     if n == 0:
#         t.forward(l)
#         return
#     coh(t, l / 3, n - 1)
#     t.lt(60)
#     coh(t, l / 3, n - 1)
#     t.rt(120)
#     coh(t, l / 3, n - 1)
#     t.lt(60)
#     coh(t, l / 3, n - 1)
#
# t = turtle.Turtle()
# t.speed(0)
# n = 5
#
# for i in range(3):
#     coh(t, 300, n)
#     t.rt(120)
#
# turtle.done()

A = []
n = 12
for i in range(n):
    A = A + [90] + [-x for x in A[::-1]]

t = turtle.Turtle()
t.speed(0)
l = 30000
h = l / 2 ** (n + 1)

t.fd(h)
for a in A:
    t.right(a)
    t.fd(h)

turtle.done()



