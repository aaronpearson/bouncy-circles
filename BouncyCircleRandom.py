import pygame, sys, math, random
from pygame.locals import *
pygame.init()
screen_1 = pygame.display.set_mode((500,500))
myfont=pygame.font.Font(None,60)
white=(255,255,255)
blue=(0,0,255)
#textImage=myfont.render("Bouncy Rectangle", True, (0,250,10))

pygame.display.set_caption("Random Bouncy Circle")

littlecirclelist = []
list1 = range(1,20)
list2 = range(1,20)
for x in list1:
    for y in list2:
        if abs(((x-10.0)**2+(y-10.0)**2)**.5 - 5)<=1:
            littlecirclelist.append((x,y))


list1 = range(200, 400)
list2 = range(250, 350)
bigarclist = []
for x in list1:
    for y in list2:
        if abs(((x-300.0)**2+(y-250)**2) - 10000)<=900:
            bigarclist.append((x,y))
bigarc_flag = True  
X_C = 300
Y_C = 250

arc_colour = 250, 0, 250
arc_position = 200, 150, 200, 200
start_angle= 0
end_angle = math.pi
width=8
class Ball:
    def __init__(self):
        self.pos_x = 300
        self.pos_y = 250
        self.vel_x = 2
        self.vel_y = 5
        self.bigarc_flag = False
    def balltrac(self):
            pygame.draw.circle(screen_1,arc_colour, (self.pos_x,self.pos_y), 10, 8)
            self.pos_x +=self.vel_x
            self.pos_y +=self.vel_y
            if self.pos_x >=500 or self.pos_x <= 0:
                if random.random()< 0.51:
                    self.vel_x = int(-(1 + random.random())*self.vel_x)
                else:
                    self.vel_x = int(-(random.random())*self.vel_x)
            if self.pos_y >=500 or self.pos_y <= 0:
                if random.random()< 0.51:
                    self.vel_y = int(-(1 + random.random())*self.vel_y)
                else:
                    self.vel_y = int(-(random.random())*self.vel_y)
 #   if vel_y > 50and pos_y > 0 and pos_y < 500:
 #      vel_y = int(random.random()*vel_y)
 #   if vel_x > 50 and pos_x > 0 and pos_x < 500:
 #       vel_x = int(random.random()*vel_x)
 #   if vel_y < -50 and pos_y > 0 and pos_y < 500:
 #       vel_y = int(random.random()*vel_y)
 #   if vel_x < -50 and pos_x > 0 and pos_x < 500:
 #       vel_x = int(random.random()*vel_x)
            if self.vel_y == 0 and self.pos_y >=500:
                self.vel_y = -2 #-abs (self.vel_x)
            if self.vel_x == 0 and self.pos_x<= 0:
                self.vel_x = 2 #abs(self.vel_x)
            if self.vel_y == 0 and self.pos_y <500:
                self.vel_y = 2 #abs (self.vel_y)
            if self.vel_x == 0 and self.pos_x> 0:
                self.vel_x = -2 #-abs (self.vel_x)
            if random.random() < 0.001:
                self.vel_x = int(-self.vel_x*random.random())
                self.vel_y = int(-self.vel_y*random.random())

 #   if abs (int(((pos_x - 300)**2 + (pos_y - 250)**2)**.5) - 100) <= 20 and y >250:
 #       vel_y = -vel_y
        #pos_y = pos_y + 3


            if abs(((self.pos_x-300.0)**2+(self.pos_y-250)**2) - 10000)<=900 and self.pos_y > 250 and not self.bigarc_flag and abs(self.pos_x-X_C)<=100 and abs(self.pos_y-Y_C <=100):
        
#        dotprod = vel_x*(pos_x - X_C)+vel_y*(pos_y - Y_C)
#        cosang = dotprod/((pos_x**2 + pos_y**2)**0.5 *((pos_x - X_C)**2 + (pos_y - Y_C)**2)**0.5)
#        ang = math.acos(cosang)
 #       vel_y = -vel_y
 #       vel_x = -vel_x
#        vel_x = int(-vel_x*random.random())
#        vel_y = int(-vel_y*random.random())
                theta = -math.acos((self.pos_x - X_C)/100.0)
                tangent = self.vel_x*math.sin(theta) + self.vel_y*math.sin(theta)
                normal = self.vel_x*math.cos(theta) - self.vel_y*math.sin(theta)
                self.vel_x= int(-normal*math.cos(-theta) - tangent*math.sin(-theta))
                self.vel_y= int(-normal*math.sin(-theta) + tangent*math.cos(-theta))
                self.bigarc_flag = True
            else:
                self.bigarc_flag = False



balllist = []
for n in range(10):
    ball=Ball()
    balllist.append(ball)
    

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 5
SCREEN_COLOUR_list = [12, 200, 100]
#line_colour = 100, 255,200
#line_width = 8

print(len(balllist))
print(balllist[5].vel_x)

keyflag = False
stuckcount = 0
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, None):
            sys.exit()
        if event.type in (KEYDOWN, None):
            if not keyflag:
                keyflag = True
            else:
                keyflag = False
    screen_1.fill((SCREEN_COLOUR_list[0], SCREEN_COLOUR_list[1], SCREEN_COLOUR_list[2]))

    if keyflag:
        for ball in balllist:
            ball.balltrac()
    #drawing an arc
    arc_colour = 250, 0, 250
    arc_position = 200, 150, 200, 200
    start_angle= 0
    end_angle = math.pi
    width=8
    pygame.draw.arc(screen_1,arc_colour, arc_position, math.pi, math.pi*2, width)
    pygame.draw.circle(screen_1,arc_colour, (pos_x,pos_y), 10, 8)
    pos_x +=vel_x
    pos_y +=vel_y
    if pos_x >=500 or pos_x <= 0:
        if random.random()< 0.51:
            vel_x = int(-(1 + random.random())*vel_x)
        else:
            vel_x = int(-(random.random())*vel_x)
    if pos_y >=500 or pos_y <= 0:
        if random.random()< 0.51:
            vel_y = int(-(1 + random.random())*vel_y)
        else:
            vel_y = int(-(random.random())*vel_y)
 #   if vel_y > 50 and pos_y > 0 and pos_y < 500:
 #      vel_y = int(random.random()*vel_y)
 #   if vel_x > 50 and pos_x > 0 and pos_x < 500:
 #       vel_x = int(random.random()*vel_x)
 #   if vel_y < -50 and pos_y > 0 and pos_y < 500:
 #       vel_y = int(random.random()*vel_y)
 #   if vel_x < -50 and pos_x > 0 and pos_x < 500:
 #       vel_x = int(random.random()*vel_x)
    if vel_y == 0 and pos_y >= 500:
        vel_y = -2
    if vel_y == 0 and pos_y <= 500:
        vel_y = 2
    if vel_x == 0 and pos_x  <= 500:
        vel_x = 2
    if vel_x == 0 and pos_x >= 500:
        vel_x = -2
    if random.random() < 0.001:
        vel_x = int(-vel_x*random.random())
        vel_y = int(-vel_y*random.random())
        #SCREEN_COLOUR_list[0], SCREEN_COLOUR_list[1], SCREEN_COLOUR_list[2] = SCREEN_COLOUR_list[1], SCREEN_COLOUR_list[2], SCREEN_COLOUR_list[0]
        SCREEN_COLOUR_list[0], SCREEN_COLOUR_list[1], SCREEN_COLOUR_list[2] = random.randint(0,255), random.randint(0,255), random.randint(0,255)
 #   if abs (int(((pos_x - 300)**2 + (pos_y - 250)**2)**.5) - 100) <= 20 and y >250:
 #       vel_y = -vel_y
        #pos_y = pos_y + 3

    if bigarc_flag == True:
        stuckcount +=1
    else:
        stuckcount -=1
    if stuckcount <0:
        stuckcount = 0
    if stuckcount >10:
        pos_y-=vel_y*10
        pos_x-=vel_x*10
        stuckcount = 0
    if abs(((pos_x-300.0)**2+(pos_y-250)**2) - 10000)<=900 and pos_y > 250 and not bigarc_flag and abs(pos_x-X_C)<=100 and abs(pos_y-Y_C <=100):
        
#        dotprod = vel_x*(pos_x - X_C)+vel_y*(pos_y - Y_C)
#        cosang = dotprod/((pos_x**2 + pos_y**2)**0.5 *((pos_x - X_C)**2 + (pos_y - Y_C)**2)**0.5)
#        ang = math.acos(cosang)
 #       vel_y = -vel_y
 #       vel_x = -vel_x
#        vel_x = int(-vel_x*random.random())
#        vel_y = int(-vel_y*random.random())
        theta = -math.acos((pos_x - X_C)/100.0)
        tangent = vel_x*math.sin(theta) + vel_y*math.sin(theta)
        normal = vel_x*math.cos(theta) - vel_y*math.sin(theta)
        vel_x= int(-normal*math.cos(-theta) - tangent*math.sin(-theta))
        vel_y= int(-normal*math.sin(-theta) + tangent*math.cos(-theta))
        bigarc_flag = True
        stuckcount += 1
    else:
        bigarc_flag = False

    for point in littlecirclelist:
        screen_1.set_at(point,blue)

#    for point in bigarclist:
#        screen_1.set_at(point, white)


        
    pygame.display.update( )
