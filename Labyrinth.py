#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Labyrinth")
wn.setup(600,600)
wn.tracer(0)


# In[2]:


images = ["wall.gif","treasure.gif","player.gif","gold.gif","door.gif","water.gif"]

for image in images:
    turtle.register_shape(image)


# In[3]:


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        
class Water(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("water.gif")
        self.color("blue")
        self.penup()
        self.speed(0) 
        self.goto(x,y)
        
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("gold.gif")
        self.color("gold")
        self.penup()
        self.speed(0) 
        self.gold=100
        self.goto(x,y)
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
        
class Finish(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0) 
        self.goto(x,y)
        
class Teleport(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("door.gif")
        self.color("red")
        self.penup()
        self.speed(0)  
        self.goto(x,y)
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("player.gif")
        self.color("Yellow")
        self.penup()
        self.speed(0)  
        self.gold = 0
        
        
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()+24
        
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()-24
        
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_left(self):
        move_to_x = player.xcor()-24
        move_to_y = player.ycor()
        
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    
    def go_right(self):
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()
        
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            
    def is_collision(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))
        
        if distance <5:
            return True
        else:
            return False
            

walls = []
levels = [""]  
treasures = []
waters = []
Fin = []
Teleporter = []


# In[4]:


level_1 = [
"XXXX OXXXX",
"XP     TXX",
"XXX   WWWW",
" XX   XXXX",
"XT  PWXXXX",
"XX   WW  X",
"XXW   XXXX",
"X XW   WWX",
"XXT    XXX",
"XXXXP  FXX",
]

levels.append(level_1)


# In[5]:


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -120+(x*24)
            screen_y = 120-(y*24)
            
            if character =="X":
                pen.goto(screen_x,screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))
                
            if character =="W":
                waters.append(Water(screen_x,screen_y))
                
            if character =="P":
                Teleporter.append(Teleport(screen_x,screen_y))
                
            if character =="T":
                treasures.append(Treasure(screen_x,screen_y))
                
                
            if character =="O":
                player.goto(screen_x,screen_y)
                
             
            if character =="F":
                Fin.append(Finish(screen_x,screen_y))
                


# In[6]:


pen=Pen()
player = Player()



# In[7]:


setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
            
    for water in waters:
        if player.is_collision(water):
            print ("You drowned wait for help!")
            
    for finish in Fin:
        if player.is_collision(finish):
            print (".....Winner.......")   
            
    for Teleport in Teleporter:
        if player.is_collision(Teleport):
            print ("...You are being teleported...")         
     
    wn.update()   
    

            
      


# In[15]:


cd


# In[ ]:




