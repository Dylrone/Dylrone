from graphics import *
# Lab 3: Sudoku Boogaloo
def Sudoku():
    rows = 9
    cols = 9
    size = 45
    margin = 20
    locat = margin + size
    # Window
    win = GraphWin("Sudoku", rows*size+(margin*2),rows*size+(margin*2) )
    win.setBackground(color_rgb(255,255,255))
    # All of the individual boxes
    num1 = Rectangle(Point(margin,margin), Point(margin+size,margin+size))
    num1.setFill(color_rgb(230,230,230))
    num1.setWidth(0)
    txt1= Text(Point(margin+(size/2),margin+(size/2)), "6")
    txt1.setSize(32)
    num1.draw(win)
    txt1.draw(win)
    num2= num1.clone()
    num2.move(size,0)
    txt2= txt1.clone()
    txt2.move(size,0)
    txt2.setText("4")
    num2.draw(win)
    txt2.draw(win)
    num3= num1.clone()
    num3.move(0,size)
    txt3= txt1.clone()
    txt3.move(0,size)
    txt3.setText("3")
    num3.draw(win)
    txt3.draw(win)
    num4= num1.clone()
    num4.move(size*2,0)
    txt4= txt1.clone()
    txt4.move(size*2,0)
    txt4.setText("1")
    num4.draw(win)
    txt4.draw(win)
    num5= num1.clone()
    num5.move(size*3,0)
    txt5= txt1.clone()
    txt5.move(size*3,0)
    txt5.setText("8")
    num5.draw(win)
    txt5.draw(win)
    
    # Big Lines Vertically
    for i in range(2,0,-1):
        point1=Point(margin+(size*3*i),margin)
        point2=Point(margin+(size*3*i),rows*size+margin)
        line=Line(point1,point2)
        line.setWidth(5)
        line.setOutline(color_rgb(149,149,149))
        line.draw(win)
        
    # Big Lines Horizontallu
    for i in range(2,0,-1):
        point3=Point(margin,margin+size*3*i)
        point4=Point(rows*size+margin,margin+size*3*i)
        line2=Line(point3,point4)
        line2.setWidth(5)
        line2.setOutline(color_rgb(149,149,149))
        line2.draw(win)
        
    # Small lines Vertical
    for i in range(8,0,-1):
        point5=Point(margin+size*i,margin)
        point6=Point(margin+size*i,rows*size+margin)
        line3=Line(point5,point6)
        line3.setWidth(1)
        line3.setOutline(color_rgb(149,149,149))
        line3.draw(win)
    # Small Lines Horizontal
    for i in range(8,0,-1):
        point7=Point(margin,margin+size*i)
        point8=Point(rows*size+margin,margin+size*i)
        line4=Line(point7,point8)
        line4.setWidth(1)
        line4.setOutline(color_rgb(149,149,149))
        line4.draw(win)

    # Rectangle Object
    p1=Point(margin,margin)
    p2=Point(rows*size+margin,rows*size+margin)
    rect=Rectangle(p1,p2)
    rect.setWidth(5)
    rect.draw(win)
Sudoku()
