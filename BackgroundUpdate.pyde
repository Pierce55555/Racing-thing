import random
x = 0
y = 0
car_move_x = 420
car_move_y = 430
keys_pressed = [False for key_code in range(256)]

def setup():
    size(640,480)
    
def road():
    fill(115,115,115)
    rect(280,0,50,height)
    fill(128,128,128)
    rect(330,0,50,height)
    fill(139,139,139)
    rect(380,0,80,height)
    fill(139,139,139)
    rect(380+50,0,80,height)
    fill(128,128,128)
    rect(380+100,0,50,height)
    fill(115,115,115)
    rect(380+150,0,50,height)
    

def ocean():
    global x
    for i in range (-600, 750, 80):
        fill(30,144,255)
        rect(580,i+x,100,100)
        fill(170,170,170)
        rect(582,i+x,6,90)
        fill(211,211,211)
        rect(580,i+x,10,50)
       
        
    if x >= 600:
        x = -200
        
        
    
    
def yellow_lines():
    global x   
    fill(255, 174, 66)
    for i in range (-600, 750, 80):
        rect(420,i+x,20,60)
    if x >= 600:
        x = -200
    x += 10

def car():
    global car_move_x
    global car_move_y
    fill(0)
    rect(car_move_x-3, car_move_y+3,5,15)
    fill(0)
    rect(car_move_x+37, car_move_y+3,5,15)
    fill(0)
    rect(car_move_x-3, car_move_y+40,5,15)
    fill(0)
    rect(car_move_x+37, car_move_y+40,5,15)
    fill (200, 0, 0)
    rect(car_move_x,car_move_y,40,60)
    fill (150, 0, 0)
    rect(car_move_x, car_move_y+20,40,30)
    if car_move_x <= 100:
        car_move_x == 279
    
    
def keyPressed():
    global keys_pressed
    keys_pressed[keyCode] = True
    
def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False

    
def draw():
    background(124, 252, 0)
    noStroke()
    global y
    global car_move_x
    global car_move_y
    road()
    yellow_lines()
    car()
    ocean()
    fill(0)
    ellipse(350, 0+y, 25, 25)
    ellipse(310, 150+y, 25, 25)
    ellipse(380, 300+y, 25, 25)
    ellipse(330, 450+y, 25, 25)
    if y >= 600:
        y = -500
    y += 10
    
    if keys_pressed[37]:
        if car_move_x <= 282 and car_move_y > -60 and car_move_y < 490:
            car_move_x -= 0
        else:
            car_move_x -= 5
    if keys_pressed[38]:
        if car_move_y <= 0 and car_move_x > 250 and car_move_x < 560:
            car_move_y -= 0
        else:
            car_move_y -= 5
    if keys_pressed[39]:
        if car_move_x >= 538 and car_move_y > -60 and car_move_y < 490:
            car_move_x += 0
        else:
            car_move_x += 5
    if keys_pressed[40]:
        if car_move_y >= 420 and car_move_x > 250 and car_move_x < 560:
            car_move_x += 0
        else:
            car_move_y += 5

    
