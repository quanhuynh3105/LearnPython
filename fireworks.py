import turtle
import random
import time

turtle.colormode(255)
s = turtle.Screen()
s.bgcolor("black")
s.setup(700,700)
t = turtle.Turtle()
#turtle.tracer(0,0)
t.speed(0)
t.left(90)
t.ht()

def star(nstars):
    t.color("white")
    for i in range(nstars):
        x = random.randint(-330,330)
        y = random.randint(-330,330)
        t.penup()
        t.goto(x,y)
        t.pendown()
    
        size = random.randint(2, 7)
        for i in range(5):
            t.forward(size)
            t.backward(size)
            t.left(72)

def firework(nfireworks,colors):
    for i in range(nfireworks):
        x = random.randint(-300,300)
        # Pháo bông bắt đầu ở y -300, từ từ lại vị trí random rồi mới nổ
        target_y = random.randint(-250,300)
        t.penup()
        t.goto(x,-350)
        t.pendown()

        t.pencolor(random.choice(colors))
        
        size = random.randint(50, 90)
        turn = random.randint(14,20)
        t.speed(6)
        t.pensize(1)
        t.pencolor(random.choice(colors))
        for i in range(10):
            t.forward((target_y+350)/10)
        t.speed(0)
        t.pensize(2)
        for i in range(turn):
            t.forward(size)
            t.backward(size)
            t.left(360/turn)

        t.pencolor("white")
        t.write("Bùm!",font=("Calibri",16,"bold"))

        t.pencolor("black")
        for i in range(10):
            t.forward((target_y+350)/10)

def fallingstar(nfalls):
    t.right(180)
    for i in range(nfalls):
        x = random.randint(-250,250)
        y = random.randint(-50,330)
        t.penup()
        t.goto(x,y)
        t.pendown()
    
        size = random.randint(4, 7)
        fally=0
        for i in range(10):
            t.penup()
            t.right(random.randint(-10,10))
            t.forward(12+fally)
            t.pendown()
            fally+=5
            t.color("white")
            for j in range(4):
                t.forward(size)
                t.backward(size)
                t.left(90)
            time.sleep(0.2)
            t.color("black")
            t.pensize(20)
            t.forward(0)
            t.pensize(4)
def endofworld():
    size = 10
    t.goto(0,0)
    t.pencolor('white')
    t.pendown()
    for j in range(30):
        t.forward(0)
        t.pensize(size)
        size+= 10 * ((size/80)+1)
    t.pencolor('black')
    t.pensize(5)
    t.write("Mọi thứ xóa sạch, hết phim",font=("Calibri",12,"normal"))
def launch(nstars, nfireworks, colors, nfalls):
    star(nstars)
    firework(nfireworks,colors)
    fallingstar(nfalls)


if __name__ == '__main__':
    nstars = random.randint(30,40)
    nfireworks = random.randint(12,20)
    #nfalls = random.randint(3,6)
    
    colors= ['red','green','blue','yellow','lime','gray','white','cyan','pink','purple','orange']
    launch(nstars,nfireworks,colors,0)

    time.sleep(1)
    endofworld()
