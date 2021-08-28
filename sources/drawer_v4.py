import turtle as t
global lastX
global lastY
def getPos(x,y):
    global lastX
    global lastY
    global lastColor
    global bt_clicked
    global bc_clicked
    global bd_clicked
    if y <-150:
        y = -150
        print('Can not draw here!!')
    lastX = x
    lastY = y
    print("(", lastX, "," ,lastY,")")
    #-------------------------------------
    if ucolor == 1:
      t.pencolor('red')
      lastColor ='red'
    else:
      t.pencolor('blue')
      lastColor ='blue'
    #---------------------------------------
    if udelete == 1:
      t.pencolor('white')
      t.pensize(10)
    else:
      t.pencolor(lastColor)
      t.pensize(1)
    #---------------------------------------
    if up == 1:
      t.penup()
    else:
      t.pendown()
    if bt_clicked == 0 and bc_clicked == 0 and bd_clicked == 0: # neu bt_clicked = 1 nghia la dang click hinh vuong
        t.goto(x,y) 
    else:
        bt_clicked = 0
        bc_clicked = 0
        bd_clicked = 0
    return
def bdelete_clicked(clickx,clicky):
    global udelete
    global lastX
    global lastY
    global bd_clicked
    if udelete == 1: 
        udelete = 0  
    else:
        udelete = 1 
    t.goto(lastX,lastY)
    bd_clicked = 1
def square():
    sq = t.Turtle()
    sq.penup()
    sq.goto(50,-220)
    sq.pendown()
    sq.shape("square")
    sq.shapesize(6,20,10)
    sq.color('lime')
    return sq
def button_color(x,y,color):
    bc=t.Turtle()
    #bt.hideturtle()
    bc.penup()
    bc.goto(x,y-10)
    bc.pendown
    bc.penup()
    bc.goto(x,y)
    bc.pendown()
    bc.shape('circle')
    bc.shapesize(3)
    bc.color(color)
    return bc
def bcolor_clicked(clickx,clicky):
    global ucolor
    global lastX
    global lastY
    global bc_clicked
    if ucolor == 1: 
        ucolor = 0  
    else:
        ucolor = 1  # penup
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
    square()
    bt=t.Turtle()
    bt.penup()
    bt.goto(-15,-266)
    bt.pendown
    #bt.hideturtle()
    bt.penup()
    bt.goto(10,-220)
    bt.pendown()
    bt.shape("square")
    bt.shapesize(3,3,3)
    bt.color("red")
    return bt
def main():
    print ('Drawer create by Quanhuynh')
    print ('Red button : pen up + down')
    print ('Blue button : change color blue and red')
    print ('Green button : delete')
    print ('dont click two button a same time')
    s = t.getscreen()
    bt = buttonUpDown()
    bblue = button_color(100,-220,'blue')
    bgreen = button_color(170,-220,'green')
    s.onclick(getPos)
    bt.onclick(button_clicked) #button_clicked: function
    bblue.onclick(bcolor_clicked) # bcolor_clicked : function
    bgreen.onclick(bdelete_clicked)
    t.shape('turtle')
    t.mainloop()

if __name__ == '__main__':
    #status flag up n
    up = 0
    ucolor = 0
    udelete = 0
    bt_clicked = 0
    bc_clicked = 0  #int
    bd_clicked = 0
    lastX = 0
    lastY = 0
    lastColor = 'blue'
    main()
