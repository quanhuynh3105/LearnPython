import turtle as t
global lastX
global lastY
def getPos(x,y):
    global lastX
    global lastY
    global bt_clicked
    global bc_clicked
    lastX = x
    lastY = y
    print("(", lastX, "," ,lastY,")")
    # Neu click vao circle thi chuyen mau do
    if ucolor == 1:
      t.pencolor('red')
    else:
      t.pencolor('blue')

    #---------------------------------------
    if up == 1:
      t.penup()
    else:
      t.pendown()
    if bt_clicked == 0 and bc_clicked == 0: # neu bt_clicked = 1 nghia la dang click hinh vuong
        t.goto(x,y) 
    else:
        bt_clicked = 0
        bc_clicked = 0
    return
def button_color():
    bc=t.Turtle()
    #bt.hideturtle()
    bc.penup()
    bc.goto(100,-220)
    bc.pendown()
    bc.shape("circle")
    bc.shapesize(3)
    bc.color("blue")
    return bc
def bcolor_clicked(clickx,clicky):
    global ucolor
    global lastX
    global lastY
    global bc_clicked
    if ucolor == 1: #dang la up --> down
        ucolor = 0  # --> down
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
    bt=t.Turtle()
    #bt.hideturtle()
    bt.penup()
    bt.goto(10,-220)
    bt.pendown()
    bt.shape("square")
    bt.shapesize(3,3,3)
    bt.color("red")
    return bt
def main():
    s = t.getscreen()
    bt = buttonUpDown()
    bc = button_color()
    s.onclick(getPos)
    bt.onclick(button_clicked) #button_clicked: function
    bc.onclick(bcolor_clicked) # bcolor_clicked : function
    t.shape('turtle')
    t.mainloop()

if __name__ == '__main__':
    up = 0 #button dang la down
    ucolor = 0
    bt_clicked = 0
    bc_clicked = 0  #int
    lastX = 0
    lastY = 0
    main()
