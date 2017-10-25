import pygame, sys, math, random
from pygame.locals import *
pygame.init()
screen_1 = pygame.display.set_mode((1200,800))
myfont=pygame.font.Font(None,60)
white=(255,255,255)
blue=(0,0,255)

#textImage=myfont.render("Bouncy Rectangle", True, (0,250,10))

#pygame.display.set_caption("Ridiculously simple model")

pygame.display.set_caption("Inverse Square Law")

timecounter = 0

def dotprod( (a, b),(c,d)):
    return a * c + b * d

def reflection ((x,y),(w,z)):
    """Reflection of (x,y) off surface with unit normal vector (w,z)"""
    twodot = 2*dotprod((x,y),(w,z))
    a, b = x - twodot* w, y - twodot*z
    return (a,b)

def refdelta ((x,y),(w,z)):
        twodot = 2*dotprod((x,y),(w,z))
        return (- twodot* w, - twodot*z)


class Ball:
    def __init__(self, pos_x = 300, pos_y = 250, vel_x = 0,vel_y = 0, density = 1, radius = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.delta_velx = 0
        self.delta_vely = 0
        self.density = density
        self.colour = arc_colour
        self.radius = radius
    def dist(self, otherball):
        return ((self.pos_x - otherball.pos_x)**2 + (self.pos_y - otherball.pos_y)**2)**.5
    
    def balltrack(self, ball_list):
        from math import sin, cos, acos
        for otherball in ball_list:
            distanceto = self.dist(otherball)
##            if distanceto == 0 and otherball != self:
##                ind = ball_list.index(otherball)
##                self.density += otherball.density
##                del ball_list[ind]
##             Originally tried just absorbing one ball into another. Now will try bouncing.
            if distanceto <= self.radius + otherball.radius and otherball != self:
                #normalizefactor = math.sqrt(dotprod((otherball.vel_x),(otherball.vel_y), (otherball.vel_x),(otherball.vel_y)))
                #we don't actually want to normalize here. The magnitude of the reflection should depend on the velocity of the other particle to mimic conservation
                #momentum. Pathological case when other ball is going in the same direction? Maybe. Account for mass? Yes. Later.
                #okay, now.
                weighting = float(otherball.density)/self.density
                (self.delta_velx, self.delta_vely) = refdelta((self.delta_velx, self.delta_vely), (otherball.delta_velx*weighting, otherball.delta_vely*weighting))
            elif otherball != self:
                
                angleto = acos((float(otherball.pos_x) - self.pos_x)/distanceto)
                if otherball.pos_y > self.pos_y:
                    angleto = -angleto
                xdistanceto = distanceto*cos(angleto)
                ydistanceto = distanceto*sin(angleto)
                self.delta_velx += (float(otherball.density))*cos(angleto)/distanceto
                self.delta_velx /= distanceto
                self.delta_vely += -(float(otherball.density))*sin(angleto)/distanceto
                self.delta_vely /= distanceto
            self.vel_y +=  self.delta_vely
            self.vel_x += self.delta_velx
            self.delta_velx, self.delta_vely = 0, 0

    zoomexponent = 0
    zoomlevel = 10.0**zoomexponent
    def ballrender(self):
        pygame.draw.circle(screen_1, self.colour, (int ((self.pos_x - 600.0)/float(self.zoomlevel) + 600),int((self.pos_y-400.0)/float(self.zoomlevel) +400)), 5, 2)
##        for event in pygame.event.get():

        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
##        if abs(self.vel_x) < 1:
##            if random.random() < abs(self.vel_x):
##                self.pos_x += -1*(not self.vel_x >0)
##        else:
##            self.pos_x += int (self.vel_x)
##        
##        if abs(self.vel_y) < 1:
##            if random.random() < abs(self.vel_y):
##                self.pos_y += -1*(not self.vel_y >0)
##        else:
##            self.pos_y += int (self.vel_y)
##        if self.pos_x >100000:
##            self.pos_x = self.pos_x % 100000
##        if self.pos_x <0:
##            self.pos_x = 100000 -self.pos_x
##        if self.pos_y >=100000:
##            self.pos_y = self.pos_y % 100000
##        if self.pos_y < 0:
##            self.pos_y = 100000 - self.pos_y

universal_ball_list = []
SCREEN_COLOUR_list = [12, 200, 100]
arc_colour = 25, 25, 250



def ballarc(number, portion, radius):
    ball_list = []
    for x in range(int(portion*number)):
        newball = Ball(600 + int (radius*math.cos(2*x*math.pi/number)),400 + int (radius * math.sin(2*x*math.pi/number)))
        ball_list.append(newball)
    return ball_list

def ballvortex(number, portion, radius, angvel):
    ball_list = []
    for x in range(int(portion*number)):
        newball = Ball(600 + int (radius*math.cos(2*x*math.pi/number)),400 + int (radius * math.sin(2*x*math.pi/number)))
        linearvel = 2*math.pi*radius*angvel
        #ang = 2*math.pi*angvel
        newball.vel_y = linearvel * (newball.pos_y-400)/radius
        newball.vel_x = linearvel * (newball.pos_x-600)/radius
        ball_list.append(newball)
    return ball_list
#universal_ball_list = ballarc(100, 1, 100)

universal_ball_list = []

##for x in range (10):
##    for y in range(10):
##        if random.random() < 0.5:
##            mass = int(math.ceil(1000000*random.random()))
##            newball = Ball(120*x, 80*y,0, 0, mass, math.ceil(mass/1000))
##            universal_ball_list.append(newball)

##for x in range (5):
##    for y in range(5):
##        newball = Ball(100 + x, 100 + y)
##        universal_ball_list.append(newball)

#universal_ball_list=[]


##for x in range(10):
##    for y in range(10):
##        if random.random()<0.1:
##            mass = math.ceil(int (1000000*random.random()))
##            newball = Ball(550 + 1000*x, 350 + 1000 * y, 0, 0, mass, math.ceil(abs(int(mass/1000))))
##            universal_ball_list.append(newball)
for n in range(10):
    #universal_ball_list += ballvortex(10,1,  10 + 2*n, 0)
    for y in range(10):
        ball = Ball(550 + 10*n, 350 + 10*y, 0, 0, 1, 1)
        universal_ball_list.append(ball)



##ball = Ball(10600, 400, -50, 0, 100000000)
##universal_ball_list.append(ball)
##ball = Ball(-10400, 400, 50, 0, 10000000)
#universal_ball_list.append(ball)


##for x in range (0):
##newball = Ball(600, 400, 0, 0, 100)
##universal_ball_list.append(newball)
##newball = Ball(600, 400 , 0, 0, 100)
##universal_ball_list.append(newball)
##
##newball =Ball(600, 475, -2,0)
##universal_ball_list.append(newball)
##
##newball =Ball(600, 325, 2,0)
##universal_ball_list.append(newball)
##
##newball =Ball(525, 400, 0,-100, 1000000)
##universal_ball_list.append(newball)
##
##newball =Ball(675, 400, 0 ,100, 1000000)
##universal_ball_list.append(newball)

##newball =Ball(600, 1000000, 0,500, 10000000000000)
##universal_ball_list.append(newball)
##
##newball =Ball(600, -1000000, 0,500, 10000000000000)
##universal_ball_list.append(newball)
##universal_ball_list = []
##for x in range (10, 50, 10):
##    universal_ball_list += ballarc(5,  1, 10*x)
##
####for x in range (100):
####    newball = Ball (550 + x, 450 -x)
####    universal_ball_list.append(newball)
##
##for ball in universal_ball_list:
##    ball.vel_y = 2
print(len(universal_ball_list))
##

##universal_ball_list=[]
##for x in range (10):
##    for y in range(10):
##        newball = Ball(555 + 10*x, 355 + 10*y, 0, 0, 0.02)
##        universal_ball_list.append(newball)

##universal_ball_list += ballvortex(100, 1, 10, 0.2)

##universal_ball_list = ballvortex(49, .5, 100, 0.0000001)
##for ball in universal_ball_list:
##    ball.density = 1
##
##universal_ball_list += ballvortex(10, 1, 15, -0.05)

##universal_ball_list = ballvortex(10, 1, 100, 0.0001)
             
##
##newball2 = Ball(600, 500, -3, 0, 10000)
##newball2.colour = (20,20,20)
##universal_ball_list.append(newball2)
##
##newball3 = Ball(600, 300, 3, 0, 10000)
##newball3.colour = (20,20,20)
##universal_ball_list.append(newball3)
##universal_ball_list[-1].vel_y = 10000
##universal_ball_list[-1].density = 100
#universal_ball_list[0].vel_y = 1

##for x in range (10):
##    newball = Ball(600 + x, 700 + x, 3, 2, 2)
##    universal_ball_list.append(newball)
##outsideball = Ball(100, 400, 0, 0.001)

##for x in range (200):
##    newball = Ball (700 -100*x ,400,0, 0.5)
##    universal_ball_list.append(newball)
#universal_ball_list.append(outsideball)
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        print event
        if event.type == KEYDOWN:
            if event.key==273:
                Ball.zoomexponent +=1
                Ball.zoomlevel *=10
                print (Ball.zoomexponent)
                print(Ball.zoomlevel)
                print(universal_ball_list[0].zoomlevel)
            if event.key==274:
                Ball.zoomexponent -=1
                Ball.zoomlevel /= 10
            if event.key==276:
                pass
            if event.key==275:
                pass
##        if event.type in (KEYDOWN, None):
##            if not keyflag:
##                keyflag = True
##            else:
##                keyflag = False
    screen_1.fill((SCREEN_COLOUR_list[0], SCREEN_COLOUR_list[1], SCREEN_COLOUR_list[2]))


    for ball in universal_ball_list:
        ball.balltrack(universal_ball_list)
    for ball in universal_ball_list:
        ball.ballrender()

##    if timecounter % 100 == 0:
##        print(newball.pos_x, newball.pos_y, newball.vel_x, newball.vel_y)
##    timecounter +=1




    pygame.display.update( )
##    if keyflag:
##        for ball in balllist:
##            ball.balltrac()
##    #drawing an arc
##    arc_colour = 250, 0, 250
##    arc_position = 200, 150, 200, 200
##    start_angle= 0
##    end_angle = math.pi
##    width=8
##    pygame.draw.arc(screen_1,arc_colour, arc_position, math.pi, math.pi*2, width)
##    pygame.draw.circle(screen_1,arc_colour, (pos_x,pos_y), 10, 8)
##    pos_x +=vel_x
##    pos_y +=vel_y
##    if pos_x >=500 or pos_x <= 0:
##        if random.random()< 0.51:
##            vel_x = int(-(1 + random.random())*vel_x)
##        else:
##            vel_x = int(-(random.random())*vel_x)
##    if pos_y >=500 or pos_y <= 0:
##        if random.random()< 0.51:
##            vel_y = int(-(1 + random.random())*vel_y)
##        else:
##            vel_y = int(-(random.random())*vel_y)
## #   if vel_y > 50 and pos_y > 0 and pos_y < 500:
## #      vel_y = int(random.random()*vel_y)
## #   if vel_x > 50 and pos_x > 0 and pos_x < 500:
## #       vel_x = int(random.random()*vel_x)
## #   if vel_y < -50 and pos_y > 0 and pos_y < 500:
## #       vel_y = int(random.random()*vel_y)
## #   if vel_x < -50 and pos_x > 0 and pos_x < 500:
## #       vel_x = int(random.random()*vel_x)
##    if vel_y == 0 and pos_y >= 500:
##        vel_y = -2
##    if vel_y == 0 and pos_y <= 500:
##        vel_y = 2
##    if vel_x == 0 and pos_x  <= 500:
##        vel_x = 2
##    if vel_x == 0 and pos_x >= 500:
##        vel_x = -2
##    if random.random() < 0.001:
##        vel_x = int(-vel_x*random.random())
##        vel_y = int(-vel_y*random.random())
##        #SCREEN_COLOUR_list[0], SCREEN_COLOUR_list[1], SCREEN_COLOUR_list[2] = SCREEN_COLOUR_list[1], SCREEN_COLOUR_list[2], SCREEN_COLOUR_list[0]
##        SCREEN_COLOUR_list[0], SCREEN_COLOUR_list[1], SCREEN_COLOUR_list[2] = random.randint(0,255), random.randint(0,255), random.randint(0,255)
## #   if abs (int(((pos_x - 300)**2 + (pos_y - 250)**2)**.5) - 100) <= 20 and y >250:
## #       vel_y = -vel_y
##        #pos_y = pos_y + 3
##
##    if bigarc_flag == True:
##        stuckcount +=1
##    else:
##        stuckcount -=1
##    if stuckcount <0:
##        stuckcount = 0
##    if stuckcount >10:
##        pos_y-=vel_y*10
##        pos_x-=vel_x*10
##        stuckcount = 0
##    if abs(((pos_x-300.0)**2+(pos_y-250)**2) - 10000)<=900 and pos_y > 250 and not bigarc_flag and abs(pos_x-X_C)<=100 and abs(pos_y-Y_C <=100):
##        normal_x = (pos_x - X_C)/100.0
##        normal_y = (pos_y - Y_C)/100.0
##        reftuple = reflection((vel_x,vel_y),(normal_x, normal_y))
##        vel_x, vel_y =reftuple[0], reftuple[1]
##        vel_x, vel_y = int(vel_x), int(vel_y)
##
##        stuckcount += 1
##    else:
##        bigarc_flag = False
##
##    for point in littlecirclelist:
##        screen_1.set_at(point,blue)
##
###    for point in bigarclist:
###        screen_1.set_at(point, white)

##littlecirclelist = []
##list1 = range(1,20)
##list2 = range(1,20)
##for x in list1:
##    for y in list2:
##        if abs(((x-10.0)**2+(y-10.0)**2)**.5 - 5)<=1:
##            littlecirclelist.append((x,y))
##
##
##list1 = range(200, 400)
##list2 = range(250, 350)
##bigarclist = []
##for x in list1:
##    for y in list2:
##        if abs(((x-300.0)**2+(y-250)**2) - 10000)<=900:
##            bigarclist.append((x,y))
##bigarc_flag = True  
##X_C = 300
##Y_C = 250
##
##arc_colour = 250, 0, 250
##arc_position = 200, 150, 200, 200
##start_angle= 0
##end_angle = math.pi
##width=8
##class Ball:
##    def __init__(self):
##        self.pos_x = 300
##        self.pos_y = 250
##        self.vel_x = 2
##        self.vel_y = 5
##        self.bigarc_flag = False
##    def balltrac(self):
##            pygame.draw.circle(screen_1,arc_colour, (self.pos_x,self.pos_y), 10, 8)
##            self.pos_x +=self.vel_x
##            self.pos_y +=self.vel_y
##            if self.pos_x >=500 or self.pos_x <= 0:
##                if random.random()< 0.51:
##                    self.vel_x = int(-(1 + random.random())*self.vel_x)
##                else:
##                    self.vel_x = int(-(random.random())*self.vel_x)
##            if self.pos_y >=500 or self.pos_y <= 0:
##                if random.random()< 0.51:
##                    self.vel_y = int(-(1 + random.random())*self.vel_y)
##                else:
##                    self.vel_y = int(-(random.random())*self.vel_y)
## #   if vel_y > 50and pos_y > 0 and pos_y < 500:
## #      vel_y = int(random.random()*vel_y)
## #   if vel_x > 50 and pos_x > 0 and pos_x < 500:
## #       vel_x = int(random.random()*vel_x)
## #   if vel_y < -50 and pos_y > 0 and pos_y < 500:
## #       vel_y = int(random.random()*vel_y)
## #   if vel_x < -50 and pos_x > 0 and pos_x < 500:
## #       vel_x = int(random.random()*vel_x)
##            if self.vel_y == 0 and self.pos_y >=500:
##                self.vel_y = -2 #-abs (self.vel_x)
##            if self.vel_x == 0 and self.pos_x<= 0:
##                self.vel_x = 2 #abs(self.vel_x)
##            if self.vel_y == 0 and self.pos_y <500:
##                self.vel_y = 2 #abs (self.vel_y)
##            if self.vel_x == 0 and self.pos_x> 0:
##                self.vel_x = -2 #-abs (self.vel_x)
##            if random.random() < 0.001:
##                self.vel_x = int(-self.vel_x*random.random())
##                self.vel_y = int(-self.vel_y*random.random())
##
## #   if abs (int(((pos_x - 300)**2 + (pos_y - 250)**2)**.5) - 100) <= 20 and y >250:
## #       vel_y = -vel_y
##        #pos_y = pos_y + 3
##
##
##            if abs(((self.pos_x-300.0)**2+(self.pos_y-250)**2) - 10000)<=900 and self.pos_y > 250 and not self.bigarc_flag and abs(self.pos_x-X_C)<=100 and abs(self.pos_y-Y_C <=100):
##                normal_x = (self.pos_x - X_C)/100.0
##                normal_y = (self.pos_y - Y_C)/100.0
##                reftuple = reflection((self.vel_x,self.vel_y),(normal_x, normal_y))
##                self.vel_x, self.vel_y =reftuple[0], reftuple[1]
##                self.vel_x, self.vel_y = int(self.vel_x), int(self.vel_y)
##
##                
        
#        dotprod = vel_x*(pos_x - X_C)+vel_y*(pos_y - Y_C)
#        cosang = dotprod/((pos_x**2 + pos_y**2)**0.5 *((pos_x - X_C)**2 + (pos_y - Y_C)**2)**0.5)
#        ang = math.acos(cosang)
 #       vel_y = -vel_y
 #       vel_x = -vel_x
#        vel_x = int(-vel_x*random.random())
#        vel_y = int(-vel_y*random.random())
 #               theta = -math.acos((self.pos_x - X_C)/100.0)
#                tangent = self.vel_x*math.sin(theta) + self.vel_y*math.sin(theta)
  #              normal = self.vel_x*math.cos(theta) - self.vel_y*math.sin(theta)
  #              self.vel_x= int(-normal*math.cos(-theta) - tangent*math.sin(-theta))
  #              self.vel_y= int(-normal*math.sin(-theta) + tangent*math.cos(-theta))
  #              self.bigarc_flag = True
 #           else:
  #              self.bigarc_flag = False
                


##balllist = []
##for n in range(10):
##    ball=Ball()
##    balllist.append(ball)
##    
##
##pos_x = 300
##pos_y = 250
##vel_x = 2
##vel_y = 5
SCREEN_COLOUR_list = [12, 200, 100]
#line_colour = 100, 255,200
#line_width = 8

##print(len(balllist))
##print(balllist[5].vel_x)
##
##keyflag = False
##stuckcount = 0


        

