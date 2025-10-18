  
import turtle

t = turtle.Turtle()
t.color("black")
t.width(2)

# تحديد نقطة البداية
t.penup()
t.goto(-100, 50)
t.pendown()

t.begin_fill()  # بداية التعبئة للمستطيل 
t.fillcolor("black")  # لون المستطيل
for side in range(2):
    t.forward(200)
    t.right(90)
    t.forward(35)
    t.right(90)
t.end_fill()  # إنهاء التعبئة

t.penup()
t.goto(-100,15)
t.pendown()

t.begin_fill() 
t.fillcolor("white")  # لون المستطيل
for side in range(2):
    t.forward(200)
    t.right(90)
    t.forward(35)
    t.right(90)
t.end_fill()  # إنهاء التعبئة

t.penup()
t.goto(-100,-20)
t.pendown()

t.begin_fill()
t.fillcolor("green")  # لون المستطيل
for side in range(2):
    t.forward(200)
    t.right(90)
    t.forward(35)
    t.right(90)
t.end_fill()

# رسم المثلث وتعبئته
t.penup()
t.goto(-100, 50)
t.pendown()

t.begin_fill()
t.fillcolor("red")
t.goto(-100, -50)
t.goto(0, 0)
t.goto(-100, 50)
t.end_fill()

t.hideturtle()
turtle.done()