from turtle import *
import keyboard
import time

t1 = Turtle()
t2 = Turtle()

# Рисование арены
penup()
goto(-300, 100)
pendown()
speed(10000)
for i in range(2):
    forward(600)
    right(90)
    forward(300)
    right(90)
hideturtle()


# Создание и координаты черепашки
t1.penup()
t2.penup()
t1.shape('turtle')
t2.shape('turtle')

t1.color('red')
t2.color('green')
t1.shapesize(2)
t2.shapesize(2)
t1.goto(-300, -50)
t2.goto(300, -50)
t2.left(180)


# Границы арены
def check_border(t):
    x = t.xcor()
    y = t.ycor()
    if x > 300 or x < -300 or y > 93 or y < -210:
        t.goto(-300, -50) if x < 0 else t.goto(300, -50)


# полоска хп t1
penup()
showturtle()
goto(-400, 200)
pendown()
fillcolor("green")
begin_fill()
forward(300)
left(90)
forward(50)
left(90)
for i in range(10):
    forward(30)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
end_fill()

# полоска хп t2
penup()
goto(400, 200)
pendown()
fillcolor("green")
begin_fill()
forward(300)
right(90)
forward(50)
right(90)
for i in range(10):
    forward(30)
    right(90)
    forward(50)
    right(180)
    forward(50)
    right(90)
end_fill()
hideturtle()


# Управление черепашками
def key_event(event):
    global t1, t2
    # Управление t1
    if event.name == 'w':
        t1.forward(50)
    elif event.name == 'a':
        t1.left(45)
    elif event.name == 's':
        t1.backward(50)
    elif event.name == 'd':
        t1.right(45)
    check_border(t1)

    # Управление t2
    if event.name == 'up':
        t2.forward(50)
    elif event.name == 'down':
        t2.backward(50)
    elif event.name == 'left':
        t2.left(45)
    elif event.name == 'right':
        t2.right(45)
    check_border(t2)


# Атака t1
def attack_t1():
    global t1, t2
    t1.shapesize(2)
    t1.shape('circle')
    t1.penup()
    t1.forward(90)
    x1, y1 = t1.position()
    x2, y2 = t2.position()
    time.sleep(0.4)
    t1.backward(90)
    t1.shape('turtle')
    if round(x1) == round(x2 - 10) and round(y1) == round(y2):
        t2.hp -= 10
        print("-10 XP Зелёный")
        print("ХР у зелёного:", t2.hp)
        if t2.hp <= 0:
            print("Красный выиграл!")
            clear()
            t2.hideturtle()
            t1.shape('circle')
            t1.shapesize(6)
            t1.goto(-200, 0)
            t2.write("  WON!", align="left", font=("Arial", 50, "normal"))


# Атака t2
def attack_t2():
    global t1, t2
    t2.shapesize(2)
    t2.shape('circle')
    t2.penup()
    t2.forward(90)
    x1, y1 = t1.position()
    x2, y2 = t2.position()
    time.sleep(0.4)
    t2.backward(90)
    t2.shape('turtle')
    if round(x1) == round(x2 - 10) and round(y1) == round(y2):
        t1.hp -= 10
        print("-10 XP красный")
        print("ХР у красного:", t1.hp)
        if t1.hp <= 0:
            print("Зелёный победил!")
            clear()
            t1.hideturtle()
            t2.shape('circle')
            t2.shapesize(6)
            t2.goto(-200, 0)
            t1.write("  WON!", align="left", font=("Arial", 50, "normal"))


t1.hp = 100
t2.hp = 100

keyboard.on_press(key_event)
keyboard.add_hotkey('v', attack_t1)
keyboard.add_hotkey('right shift', attack_t2)

exitonclick()