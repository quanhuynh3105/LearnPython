import turtle as t
import random as rn
global lastX
global lastY
def getPos(x,y):
    global lastX
    global lastY
    global br_clicked
    global bt_clicked
    global bc_clicked
    global bu_clicked
    if y <= -280 and x <= -200:
        x = -200
        y = -280
        print("! Không được vẽ vào khu này!")
    lastX = x
    lastY = y
    # Neu click vao circle thi chuyen mau do
    print("")
    print("----------------")
    print("  Báo cáo ")
    print("")
    print("| Pos: ",int(lastX),int(lastY))

    #---------------------------------------
    if colorrandom == 1:
        randomcolor()
    
    if up == 1:
        t.penup()
        print("| Pen: up")
    else:
        t.pendown()
        print("| Pen: down")
    
    if auto == 1:
        print("| Mode: auto")
        repeat = int(input("Di chuyển ngẫu nhiên mấy lần?"))
        for i in range(repeat):
            randomcolor()
            maxX = rn.randint(5,320)
            maxY = rn.randint(5,320)
            t.goto(rn.randint(-maxX,maxX),rn.randint(-maxY,maxY))
        print("Máy tính suy nghĩ...:",rn.choice(rating))
    else:
        print("| Mode: normal")
    
    if undo == 1:
        t.pencolor('white')
        t.pensize(10)
        print("| Cleaning: True")
    else:
        t.pencolor(prevcolor)
        t.pensize(pensize)
        print("| Cleaning: false")
      
    if bt_clicked == 0 and bc_clicked == 0 and bu_clicked == 0 and br_clicked == 0: # neu bt_clicked = 1 nghia la dang click hinh vuong
        t.goto(x,y) 
    else:
        bt_clicked = 0
        bc_clicked = 0
        br_clicked = 0
        bu_clicked = 0
    return

def button_color():
    bc=t.Turtle()
    #bt.hideturtle()
    bc.penup()
    bc.goto(-320,-320)
    bc.pendown()
    bc.shape("circle")
    bc.shapesize(2)
    bc.color("blue")
    return bc

def bcolor_clicked(clickx,clicky):
    global ucolor
    global lastX
    global lastY
    global bc_clicked
    rncolor()
    t.goto(lastX,lastY)
    bc_clicked = 1
    
def button_clicked(clickx,clicky):
    global up
    global lastX
    global lastY
    global bt_clicked
    if up == 1: #dang la up --> down
        up = 0  # --> down
    else:
        up = 1  # penup
    t.goto(lastX,lastY)
    bt_clicked = 1
    
def buttonUpDown():
    bt=t.Turtle()
    #bt.hideturtle()
    bt.penup()
    bt.goto(-270,-320)
    bt.pendown()
    bt.shape("circle")
    bt.shapesize(2)
    bt.color("red")
    return bt

def buttonWandering():
    br=t.Turtle()
    #bt.hideturtle()
    br.penup()
    br.goto(-170,-320)
    br.pendown()
    br.shape("circle")
    br.shapesize(2)
    br.color("pink")
    return br
 
def random_clicked(clickx,clicky):
    global auto
    global lastX
    global lastY
    global br_clicked
    if auto == 1: #dang la normal --> random
        auto = 0  # --> random
    else:
        auto = 1  # normal
    t.goto(lastX,lastY)
    br_clicked = 1


def undoing():
    bu=t.Turtle()
    #bt.hideturtle()
    bu.penup()
    bu.goto(-220,-320)
    bu.pendown()
    bu.shape("circle")
    bu.shapesize(2)
    bu.color("black")
    return bu
 
def undo_clicked(clickx,clicky):
    global undo
    global lastX
    global lastY
    global bu_clicked
    if undo == 1: #dang la normal --> random
        undo = 0  # --> random
    else:
        undo = 1  # normal
    t.goto(lastX,lastY)
    bu_clicked = 1
    
def randomcolor():
    r = rn.randint(0,255)
    g = rn.randint(0,255)
    b = rn.randint(0,255)
    t.pencolor(r,g,b)
    global prevcolor
    prevcolor = [r,g,b]

def rncolor():
    global prevcolor
    newcolor = input("> Input color:")
    if newcolor == "theme":
        newcolor = input("> Background color:")
        t.bgcolor(newcolor)
        print("| Background set to",newcolor)
    elif newcolor == "pensize":
        global pensize
        pensize= input("> Pen size:")
        t.pensize(pensize)
        print("| Pensize set to",pensize)
    elif newcolor == "colorrandom":
        global colorrandom
        if colorrandom == 0:
            colorrandom = 1
            randomcolor()
            print("| Randomized colormode")
        else:
            t.pencolor('black')
            global prevcolor
            prevcolor = 'black'
            colorrandom = 0
            print("| Fixed colormode")
    
    elif newcolor == "clear":
        t.clear()
        t.bgcolor('white')
        print("| CLEARED ALL")
    else:
        prevcolor = newcolor

def main():
    s = t.getscreen()
    br = buttonWandering()
    bt = buttonUpDown()
    bc = button_color()
    bu = undoing()
    s.onclick(getPos)
    # YELLOW
    br.onclick(random_clicked)
    # RED
    bt.onclick(button_clicked) #button_clicked: function
    # BLUE
    bc.onclick(bcolor_clicked) # bcolor_clicked : function
    # BLACK
    bu.onclick(undo_clicked)
    t.shape('turtle')
    t.mainloop()

if __name__ == '__main__':
    print("BLUE: Tùy chỉnh pen")
    print("| Theme: chỉnh background color")
    print("| Colorrandom: on/off chế độ màu tự động")
    print("| Pensize: chỉnh độ dày của pen")
    print("| Clear: xóa sạch, reset background")
    print("RED: Pen up/down")
    print("BLACK: Undo")
    print("PINK: Tự động làm nát bét trang vẽ")
    up = 0 #button dang la down
    prevcolor = 'black'
    pensize = 2
    colorrandom = 0
    t.setup(700,700)
    t.pensize(2)
    t.speed(0)
    t.colormode(255)
    ucolor = 0
    auto = 0
    undo = 0
    bt_clicked = 0
    bc_clicked = 0  #int
    br_clicked = 0
    bu_clicked = 0
    lastX = 0
    lastY = 0
    rating = ["Quá xấu :(","Đẹp :)","Bình thường -_-","Một tác phẩm nghệ thuật :))","Một siêu phẩm :D","Rất hay :D"]
    main()
