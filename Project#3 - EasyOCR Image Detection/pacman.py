'''
Libraries Used: Pygame
'''
import pygame as pg
pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

#Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
grey = (127,127,127)
teal = (0,255,255)
yellow = (255,255,0)
purple = (255,0,255)

#Functions
def printToScreen(x,y,text,colour, size):
    timesnewroman = pg.font.SysFont('TimesNewRoman', size) #fontType, size
    text = str(text)
    label = timesnewroman.render(text, False, colour)
    screen.blit(label,(x,y))

#Game objects
pipe1 = pg.Rect(500,0,80,250)
pipe2 = pg.Rect(500,450,80,350)
pipe3 = pg.Rect(900,0,80,300)
pipe4 = pg.Rect(900,450,80,425)
bird = pg.Rect(80,400,50,50)


#homescreen objects
box1 = pg.Rect(400,400,100,150)

box2_color = green


#variables
gravity = 3
pipespeed = 4
jump = 10
score = 0

state = 0 #State variable

game_running = False

#Homescreen
def homescreen():
    global state
    screen_color = black
    box1_color = green
    game_running = True
    #INPUTS
    while game_running == True:
        pg.event.pump()
        buttons = pg.mouse.get_pressed()
        LMB,MMB,RMB = buttons
        mx, my = pg.mouse.get_pos()
        screen.fill(screen_color)
        pg.draw.rect(screen, box1_color, box1)
        pg.display.flip()
        clock.tick(30)
        if LMB == 1 and box1.collidepoint(mx, my):
            state = 1
            break
    
#Main Loop
def gamerunning():
    global state
    global score
    game_running = True
    wallslist = [pg.Rect(0,320,20,20),pg.Rect(0,300,20,20),pg.Rect(0,280,20,20),pg.Rect(0,260,20,20),pg.Rect(0,240,20,20),pg.Rect(0,220,20,20),pg.Rect(0,200,20,20),pg.Rect(0,180,20,20),pg.Rect(0,160,20,20),pg.Rect(20,140,20,20),pg.Rect(20,120,20,20),pg.Rect(20,80,20,20),pg.Rect(20,60,20,20),pg.Rect(20,40,20,20),pg.Rect(20,20,20,20),pg.Rect(0,60,20,20),pg.Rect(0,80,20,20),pg.Rect(0,100,20,20),pg.Rect(0,120,20,20),pg.Rect(20,100,20,20),pg.Rect(0,140,20,20),pg.Rect(0,40,20,20),pg.Rect(0,20,20,20),pg.Rect(0,0,20,20),pg.Rect(20,0,20,20),pg.Rect(20,160,20,20),pg.Rect(20,180,20,20),pg.Rect(20,200,20,20),pg.Rect(20,220,20,20),pg.Rect(20,240,20,20),pg.Rect(20,260,20,20),pg.Rect(20,280,20,20),pg.Rect(20,300,20,20),pg.Rect(20,320,20,20),pg.Rect(20,400,20,20),pg.Rect(20,440,20,20),pg.Rect(0,440,20,20),pg.Rect(0,460,20,20),pg.Rect(0,480,20,20),pg.Rect(0,500,20,20),pg.Rect(0,520,20,20),pg.Rect(0,540,20,20),pg.Rect(0,580,20,20),pg.Rect(0,560,20,20),pg.Rect(0,600,20,20),pg.Rect(0,620,20,20),pg.Rect(0,640,20,20),pg.Rect(0,660,20,20),pg.Rect(0,680,20,20),pg.Rect(0,700,20,20),pg.Rect(0,720,20,20),pg.Rect(0,740,20,20),pg.Rect(0,760,20,20),pg.Rect(0,780,20,20),pg.Rect(20,780,20,20),pg.Rect(20,760,20,20),pg.Rect(20,740,20,20),pg.Rect(20,720,20,20),pg.Rect(20,700,20,20),pg.Rect(20,680,20,20),pg.Rect(20,660,20,20),pg.Rect(20,640,20,20),pg.Rect(20,620,20,20),pg.Rect(20,600,20,20),pg.Rect(20,580,20,20),pg.Rect(20,560,20,20),pg.Rect(20,540,20,20),pg.Rect(20,520,20,20),pg.Rect(20,500,20,20),pg.Rect(20,480,20,20),pg.Rect(20,460,20,20),pg.Rect(0,420,20,20),pg.Rect(0,400,20,20),pg.Rect(40,0,20,20),pg.Rect(60,0,20,20),pg.Rect(100,0,20,20),pg.Rect(120,0,20,20),pg.Rect(140,0,20,20),pg.Rect(160,0,20,20),pg.Rect(200,0,20,20),pg.Rect(220,0,20,20),pg.Rect(240,0,20,20),pg.Rect(320,0,20,20),pg.Rect(360,0,20,20),pg.Rect(380,0,20,20),pg.Rect(400,0,20,20),pg.Rect(420,20,20,20),pg.Rect(460,20,20,20),pg.Rect(480,20,20,20),pg.Rect(500,20,20,20),pg.Rect(540,20,20,20),pg.Rect(580,20,20,20),pg.Rect(600,20,20,20),pg.Rect(620,20,20,20),pg.Rect(640,20,20,20),pg.Rect(660,20,20,20),pg.Rect(680,0,20,20),pg.Rect(700,0,20,20),pg.Rect(740,0,20,20),pg.Rect(760,0,20,20),pg.Rect(780,0,20,20),pg.Rect(720,0,20,20),pg.Rect(660,0,20,20),pg.Rect(640,0,20,20),pg.Rect(620,0,20,20),pg.Rect(580,0,20,20),pg.Rect(560,0,20,20),pg.Rect(540,0,20,20),pg.Rect(520,20,20,20),pg.Rect(440,20,20,20),pg.Rect(420,0,20,20),pg.Rect(340,0,20,20),pg.Rect(300,0,20,20),pg.Rect(280,0,20,20),pg.Rect(80,0,20,20),pg.Rect(180,0,20,20),pg.Rect(260,0,20,20),pg.Rect(440,0,20,20),pg.Rect(460,0,20,20),pg.Rect(480,0,20,20),pg.Rect(500,0,20,20),pg.Rect(520,0,20,20),pg.Rect(600,0,20,20),pg.Rect(680,20,20,20),pg.Rect(700,20,20,20),pg.Rect(720,20,20,20),pg.Rect(740,20,20,20),pg.Rect(760,20,20,20),pg.Rect(780,20,20,20),pg.Rect(800,20,20,20),pg.Rect(560,20,20,20),pg.Rect(400,20,20,20),pg.Rect(380,20,20,20),pg.Rect(360,20,20,20),pg.Rect(340,20,20,20),pg.Rect(300,20,20,20),pg.Rect(280,20,20,20),pg.Rect(260,20,20,20),pg.Rect(240,20,20,20),pg.Rect(220,20,20,20),pg.Rect(200,20,20,20),pg.Rect(180,20,20,20),pg.Rect(160,20,20,20),pg.Rect(140,20,20,20),pg.Rect(120,20,20,20),pg.Rect(80,20,20,20),pg.Rect(60,20,20,20),pg.Rect(40,20,20,20),pg.Rect(100,20,20,20),pg.Rect(320,20,20,20),pg.Rect(760,40,20,20),pg.Rect(760,60,20,20),pg.Rect(780,60,20,20),pg.Rect(780,80,20,20),pg.Rect(780,100,20,20),pg.Rect(780,120,20,20),pg.Rect(780,140,20,20),pg.Rect(780,160,20,20),pg.Rect(780,180,20,20),pg.Rect(780,200,20,20),pg.Rect(780,240,20,20),pg.Rect(780,260,20,20),pg.Rect(780,280,20,20),pg.Rect(780,300,20,20),pg.Rect(780,320,20,20),pg.Rect(760,320,20,20),pg.Rect(760,300,20,20),pg.Rect(780,40,20,20),pg.Rect(760,80,20,20),pg.Rect(760,100,20,20),pg.Rect(760,120,20,20),pg.Rect(760,140,20,20),pg.Rect(760,160,20,20),pg.Rect(760,180,20,20),pg.Rect(760,200,20,20),pg.Rect(760,220,20,20),pg.Rect(760,240,20,20),pg.Rect(760,260,20,20),pg.Rect(760,280,20,20),pg.Rect(780,220,20,20),pg.Rect(780,400,20,20),pg.Rect(780,420,20,20),pg.Rect(780,440,20,20),pg.Rect(780,460,20,20),pg.Rect(780,480,20,20),pg.Rect(780,500,20,20),pg.Rect(780,520,20,20),pg.Rect(780,540,20,20),pg.Rect(780,560,20,20),pg.Rect(780,580,20,20),pg.Rect(780,600,20,20),pg.Rect(760,620,20,20),pg.Rect(760,640,20,20),pg.Rect(760,660,20,20),pg.Rect(760,680,20,20),pg.Rect(760,700,20,20),pg.Rect(760,720,20,20),pg.Rect(760,740,20,20),pg.Rect(760,800,20,20),pg.Rect(760,780,20,20),pg.Rect(780,780,20,20),pg.Rect(780,760,20,20),pg.Rect(780,740,20,20),pg.Rect(780,700,20,20),pg.Rect(780,680,20,20),pg.Rect(760,600,20,20),pg.Rect(780,620,20,20),pg.Rect(780,640,20,20),pg.Rect(780,660,20,20),pg.Rect(780,720,20,20),pg.Rect(760,580,20,20),pg.Rect(760,560,20,20),pg.Rect(760,540,20,20),pg.Rect(760,520,20,20),pg.Rect(760,500,20,20),pg.Rect(760,400,20,20),pg.Rect(760,420,20,20),pg.Rect(760,440,20,20),pg.Rect(760,460,20,20),pg.Rect(760,480,20,20),pg.Rect(760,340,20,20),pg.Rect(780,340,20,20),pg.Rect(0,340,20,20),pg.Rect(20,340,20,20),pg.Rect(380,40,20,20),pg.Rect(380,60,20,20),pg.Rect(380,80,20,20),pg.Rect(400,80,20,20),pg.Rect(400,100,20,20),pg.Rect(400,120,20,20),pg.Rect(380,120,20,20),pg.Rect(380,140,20,20),pg.Rect(380,160,20,20),pg.Rect(380,100,20,20),pg.Rect(400,140,20,20),pg.Rect(400,160,20,20),pg.Rect(400,40,20,20),pg.Rect(400,60,20,20),pg.Rect(40,780,20,20),pg.Rect(60,780,20,20),pg.Rect(80,780,20,20),pg.Rect(100,780,20,20),pg.Rect(120,780,20,20),pg.Rect(120,800,20,20),pg.Rect(140,800,20,20),pg.Rect(160,800,20,20),pg.Rect(180,800,20,20),pg.Rect(200,800,20,20),pg.Rect(200,780,20,20),pg.Rect(180,780,20,20),pg.Rect(160,780,20,20),pg.Rect(140,780,20,20),pg.Rect(220,800,20,20),pg.Rect(240,780,20,20),pg.Rect(220,780,20,20),pg.Rect(260,780,20,20),pg.Rect(340,780,20,20),pg.Rect(360,780,20,20),pg.Rect(380,780,20,20),pg.Rect(400,780,20,20),pg.Rect(420,780,20,20),pg.Rect(440,780,20,20),pg.Rect(460,780,20,20),pg.Rect(480,780,20,20),pg.Rect(500,780,20,20),pg.Rect(520,780,20,20),pg.Rect(540,780,20,20),pg.Rect(560,780,20,20),pg.Rect(580,780,20,20),pg.Rect(600,780,20,20),pg.Rect(620,780,20,20),pg.Rect(640,780,20,20),pg.Rect(660,780,20,20),pg.Rect(680,780,20,20),pg.Rect(740,780,20,20),pg.Rect(720,780,20,20),pg.Rect(700,780,20,20),pg.Rect(380,620,20,20),pg.Rect(400,620,20,20),pg.Rect(320,80,20,20),pg.Rect(320,100,20,20),pg.Rect(320,120,20,20),pg.Rect(320,140,20,20),pg.Rect(320,160,20,20),pg.Rect(300,160,20,20),pg.Rect(280,160,20,20),pg.Rect(260,160,20,20),pg.Rect(240,160,20,20),pg.Rect(220,160,20,20),pg.Rect(200,160,20,20),pg.Rect(200,140,20,20),pg.Rect(200,120,20,20),pg.Rect(200,100,20,20),pg.Rect(200,80,20,20),pg.Rect(220,80,20,20),pg.Rect(240,80,20,20),pg.Rect(260,80,20,20),pg.Rect(280,80,20,20),pg.Rect(300,80,20,20),pg.Rect(300,100,20,20),pg.Rect(300,120,20,20),pg.Rect(300,140,20,20),pg.Rect(280,140,20,20),pg.Rect(260,140,20,20),pg.Rect(240,140,20,20),pg.Rect(220,120,20,20),pg.Rect(220,140,20,20),pg.Rect(220,100,20,20),pg.Rect(240,100,20,20),pg.Rect(260,100,20,20),pg.Rect(280,100,20,20),pg.Rect(280,120,20,20),pg.Rect(260,120,20,20),pg.Rect(240,120,20,20),pg.Rect(80,80,20,20),pg.Rect(100,80,20,20),pg.Rect(120,80,20,20),pg.Rect(140,80,20,20),pg.Rect(140,100,20,20),pg.Rect(140,120,20,20),pg.Rect(140,140,20,20),pg.Rect(140,160,20,20),pg.Rect(120,160,20,20),pg.Rect(100,160,20,20),pg.Rect(80,160,20,20),pg.Rect(80,140,20,20),pg.Rect(80,120,20,20),pg.Rect(80,100,20,20),pg.Rect(100,100,20,20),pg.Rect(120,100,20,20),pg.Rect(120,120,20,20),pg.Rect(120,140,20,20),pg.Rect(100,140,20,20),pg.Rect(100,120,20,20),pg.Rect(460,80,20,20),pg.Rect(460,100,20,20),pg.Rect(460,120,20,20),pg.Rect(460,140,20,20),pg.Rect(460,160,20,20),pg.Rect(480,160,20,20),pg.Rect(500,160,20,20),pg.Rect(520,160,20,20),pg.Rect(540,160,20,20),pg.Rect(560,160,20,20),pg.Rect(580,160,20,20),pg.Rect(580,80,20,20),pg.Rect(560,80,20,20),pg.Rect(540,80,20,20),pg.Rect(520,80,20,20),pg.Rect(520,100,20,20),pg.Rect(500,100,20,20),pg.Rect(480,100,20,20),pg.Rect(480,80,20,20),pg.Rect(500,80,20,20),pg.Rect(560,100,20,20),pg.Rect(580,100,20,20),pg.Rect(580,140,20,20),pg.Rect(540,140,20,20),pg.Rect(520,140,20,20),pg.Rect(500,140,20,20),pg.Rect(480,140,20,20),pg.Rect(480,120,20,20),pg.Rect(540,100,20,20),pg.Rect(560,120,20,20),pg.Rect(500,120,20,20),pg.Rect(520,120,20,20),pg.Rect(540,120,20,20),pg.Rect(580,120,20,20),pg.Rect(560,140,20,20),pg.Rect(660,80,20,20),pg.Rect(660,100,20,20),pg.Rect(680,100,20,20),pg.Rect(680,120,20,20),pg.Rect(680,140,20,20),pg.Rect(680,160,20,20),pg.Rect(660,160,20,20),pg.Rect(680,80,20,20),pg.Rect(660,120,20,20),pg.Rect(660,140,20,20),pg.Rect(700,80,20,20),pg.Rect(700,100,20,20),pg.Rect(700,120,20,20),pg.Rect(700,140,20,20),pg.Rect(700,160,20,20),pg.Rect(640,160,20,20),pg.Rect(640,140,20,20),pg.Rect(640,120,20,20),pg.Rect(640,100,20,20),pg.Rect(640,80,20,20),pg.Rect(280,220,20,20),pg.Rect(280,240,20,20),pg.Rect(300,240,20,20),pg.Rect(320,240,20,20),pg.Rect(340,240,20,20),pg.Rect(360,240,20,20),pg.Rect(380,240,20,20),pg.Rect(400,240,20,20),pg.Rect(420,240,20,20),pg.Rect(440,240,20,20),pg.Rect(460,240,20,20),pg.Rect(480,240,20,20),pg.Rect(500,240,20,20),pg.Rect(500,220,20,20),pg.Rect(480,220,20,20),pg.Rect(460,220,20,20),pg.Rect(440,220,20,20),pg.Rect(420,220,20,20),pg.Rect(400,220,20,20),pg.Rect(380,220,20,20),pg.Rect(360,220,20,20),pg.Rect(340,220,20,20),pg.Rect(320,220,20,20),pg.Rect(300,220,20,20),pg.Rect(380,260,20,20),pg.Rect(380,300,20,20),pg.Rect(380,320,20,20),pg.Rect(380,280,20,20),pg.Rect(400,260,20,20),pg.Rect(400,280,20,20),pg.Rect(400,300,20,20),pg.Rect(400,320,20,20),pg.Rect(220,220,20,20),pg.Rect(200,220,20,20),pg.Rect(200,240,20,20),pg.Rect(200,260,20,20),pg.Rect(220,260,20,20),pg.Rect(220,240,20,20),pg.Rect(220,280,20,20),pg.Rect(220,300,20,20),pg.Rect(220,320,20,20),pg.Rect(240,300,20,20),pg.Rect(260,300,20,20),pg.Rect(280,300,20,20),pg.Rect(300,300,20,20),pg.Rect(320,300,20,20),pg.Rect(320,320,20,20),pg.Rect(300,320,20,20),pg.Rect(280,320,20,20),pg.Rect(260,320,20,20),pg.Rect(240,320,20,20),pg.Rect(200,280,20,20),pg.Rect(200,300,20,20),pg.Rect(200,320,20,20),pg.Rect(220,340,20,20),pg.Rect(200,340,20,20),pg.Rect(200,360,20,20),pg.Rect(200,380,20,20),pg.Rect(200,400,20,20),pg.Rect(220,400,20,20),pg.Rect(220,380,20,20),pg.Rect(220,360,20,20),pg.Rect(460,300,20,20),pg.Rect(460,320,20,20),pg.Rect(480,320,20,20),pg.Rect(500,320,20,20),pg.Rect(520,320,20,20),pg.Rect(520,300,20,20),pg.Rect(500,300,20,20),pg.Rect(480,300,20,20),pg.Rect(540,300,20,20),pg.Rect(540,320,20,20),pg.Rect(560,220,20,20),pg.Rect(560,240,20,20),pg.Rect(560,260,20,20),pg.Rect(560,280,20,20),pg.Rect(560,300,20,20),pg.Rect(560,320,20,20),pg.Rect(560,340,20,20),pg.Rect(560,360,20,20),pg.Rect(560,380,20,20),pg.Rect(560,400,20,20),pg.Rect(580,400,20,20),pg.Rect(580,380,20,20),pg.Rect(580,360,20,20),pg.Rect(580,340,20,20),pg.Rect(580,320,20,20),pg.Rect(580,300,20,20),pg.Rect(580,280,20,20),pg.Rect(580,260,20,20),pg.Rect(580,240,20,20),pg.Rect(580,220,20,20),pg.Rect(280,380,20,20),pg.Rect(300,380,20,20),pg.Rect(320,380,20,20),pg.Rect(340,380,20,20),pg.Rect(440,380,20,20),pg.Rect(460,380,20,20),pg.Rect(480,380,20,20),pg.Rect(500,380,20,20),pg.Rect(280,400,20,20),pg.Rect(280,420,20,20),pg.Rect(280,440,20,20),pg.Rect(280,460,20,20),pg.Rect(280,480,20,20),pg.Rect(300,480,20,20),pg.Rect(320,480,20,20),pg.Rect(340,480,20,20),pg.Rect(360,480,20,20),pg.Rect(400,480,20,20),pg.Rect(420,480,20,20),pg.Rect(440,480,20,20),pg.Rect(480,480,20,20),pg.Rect(500,480,20,20),pg.Rect(500,460,20,20),pg.Rect(500,400,20,20),pg.Rect(500,420,20,20),pg.Rect(500,440,20,20),pg.Rect(460,480,20,20),pg.Rect(380,480,20,20),pg.Rect(200,460,20,20),pg.Rect(220,460,20,20),pg.Rect(220,480,20,20),pg.Rect(220,500,20,20),pg.Rect(220,520,20,20),pg.Rect(220,540,20,20),pg.Rect(220,560,20,20),pg.Rect(200,560,20,20),pg.Rect(200,540,20,20),pg.Rect(200,520,20,20),pg.Rect(200,500,20,20),pg.Rect(200,480,20,20),pg.Rect(560,460,20,20),pg.Rect(560,480,20,20),pg.Rect(560,500,20,20),pg.Rect(560,520,20,20),pg.Rect(560,540,20,20),pg.Rect(560,560,20,20),pg.Rect(580,560,20,20),pg.Rect(580,540,20,20),pg.Rect(580,520,20,20),pg.Rect(580,500,20,20),pg.Rect(580,480,20,20),pg.Rect(580,460,20,20),pg.Rect(280,540,20,20),pg.Rect(300,540,20,20),pg.Rect(320,540,20,20),pg.Rect(340,540,20,20),pg.Rect(360,540,20,20),pg.Rect(380,540,20,20),pg.Rect(400,540,20,20),pg.Rect(420,540,20,20),pg.Rect(440,540,20,20),pg.Rect(460,540,20,20),pg.Rect(480,540,20,20),pg.Rect(500,540,20,20),pg.Rect(500,560,20,20),pg.Rect(480,560,20,20),pg.Rect(460,560,20,20),pg.Rect(400,560,20,20),pg.Rect(380,560,20,20),pg.Rect(360,560,20,20),pg.Rect(300,560,20,20),pg.Rect(320,560,20,20),pg.Rect(340,560,20,20),pg.Rect(420,560,20,20),pg.Rect(440,560,20,20),pg.Rect(280,560,20,20),pg.Rect(380,580,20,20),pg.Rect(380,600,20,20),pg.Rect(400,600,20,20),pg.Rect(400,580,20,20),pg.Rect(380,700,20,20),pg.Rect(400,700,20,20),pg.Rect(280,700,20,20),pg.Rect(300,700,20,20),pg.Rect(320,700,20,20),pg.Rect(340,700,20,20),pg.Rect(360,700,20,20),pg.Rect(420,700,20,20),pg.Rect(440,700,20,20),pg.Rect(460,700,20,20),pg.Rect(760,760,20,20),pg.Rect(280,780,20,20),pg.Rect(300,780,20,20),pg.Rect(320,780,20,20),pg.Rect(380,640,20,20),pg.Rect(400,640,20,20),pg.Rect(480,700,20,20),pg.Rect(500,700,20,20),pg.Rect(280,720,20,20),pg.Rect(300,720,20,20),pg.Rect(320,720,20,20),pg.Rect(340,720,20,20),pg.Rect(360,720,20,20),pg.Rect(380,720,20,20),pg.Rect(400,720,20,20),pg.Rect(420,720,20,20),pg.Rect(440,720,20,20),pg.Rect(460,720,20,20),pg.Rect(480,720,20,20),pg.Rect(500,720,20,20),pg.Rect(320,620,20,20),pg.Rect(320,640,20,20),pg.Rect(300,640,20,20),pg.Rect(280,640,20,20),pg.Rect(260,640,20,20),pg.Rect(240,640,20,20),pg.Rect(220,640,20,20),pg.Rect(200,640,20,20),pg.Rect(200,620,20,20),pg.Rect(220,620,20,20),pg.Rect(240,620,20,20),pg.Rect(260,620,20,20),pg.Rect(280,620,20,20),pg.Rect(300,620,20,20),pg.Rect(460,620,20,20),pg.Rect(460,640,20,20),pg.Rect(480,640,20,20),pg.Rect(500,640,20,20),pg.Rect(520,620,20,20),pg.Rect(540,620,20,20),pg.Rect(560,620,20,20),pg.Rect(580,620,20,20),pg.Rect(580,640,20,20),pg.Rect(560,640,20,20),pg.Rect(540,640,20,20),pg.Rect(520,640,20,20),pg.Rect(480,620,20,20),pg.Rect(500,620,20,20),pg.Rect(200,700,20,20),pg.Rect(200,720,20,20),pg.Rect(220,720,20,20),pg.Rect(220,700,20,20),pg.Rect(180,700,20,20),pg.Rect(160,700,20,20),pg.Rect(140,700,20,20),pg.Rect(140,680,20,20),pg.Rect(140,660,20,20),pg.Rect(140,620,20,20),pg.Rect(140,640,20,20),pg.Rect(120,620,20,20),pg.Rect(120,640,20,20),pg.Rect(120,660,20,20),pg.Rect(120,680,20,20),pg.Rect(120,700,20,20),pg.Rect(140,720,20,20),pg.Rect(160,720,20,20),pg.Rect(180,720,20,20),pg.Rect(100,700,20,20),pg.Rect(80,720,20,20),pg.Rect(100,720,20,20),pg.Rect(120,720,20,20),pg.Rect(80,700,20,20),pg.Rect(560,700,20,20),pg.Rect(560,720,20,20),pg.Rect(580,720,20,20),pg.Rect(600,720,20,20),pg.Rect(620,720,20,20),pg.Rect(640,720,20,20),pg.Rect(660,720,20,20),pg.Rect(680,720,20,20),pg.Rect(700,720,20,20),pg.Rect(700,700,20,20),pg.Rect(680,700,20,20),pg.Rect(660,700,20,20),pg.Rect(640,700,20,20),pg.Rect(620,700,20,20),pg.Rect(600,700,20,20),pg.Rect(580,700,20,20),pg.Rect(660,680,20,20),pg.Rect(660,660,20,20),pg.Rect(660,640,20,20),pg.Rect(660,620,20,20),pg.Rect(640,620,20,20),pg.Rect(640,680,20,20),pg.Rect(640,640,20,20),pg.Rect(640,660,20,20),pg.Rect(120,560,20,20),pg.Rect(140,560,20,20),pg.Rect(120,540,20,20),pg.Rect(120,520,20,20),pg.Rect(120,500,20,20),pg.Rect(120,480,20,20),pg.Rect(120,460,20,20),pg.Rect(100,460,20,20),pg.Rect(140,460,20,20),pg.Rect(140,480,20,20),pg.Rect(140,500,20,20),pg.Rect(140,520,20,20),pg.Rect(140,540,20,20),pg.Rect(100,480,20,20),pg.Rect(80,480,20,20),pg.Rect(80,460,20,20),pg.Rect(640,460,20,20),pg.Rect(640,480,20,20),pg.Rect(640,500,20,20),pg.Rect(640,520,20,20),pg.Rect(640,540,20,20),pg.Rect(640,560,20,20),pg.Rect(660,560,20,20),pg.Rect(660,540,20,20),pg.Rect(660,520,20,20),pg.Rect(660,500,20,20),pg.Rect(660,480,20,20),pg.Rect(680,480,20,20),pg.Rect(700,480,20,20),pg.Rect(700,460,20,20),pg.Rect(680,460,20,20),pg.Rect(660,460,20,20),pg.Rect(80,220,20,20),pg.Rect(100,220,20,20),pg.Rect(120,220,20,20),pg.Rect(140,220,20,20),pg.Rect(140,240,20,20),pg.Rect(120,240,20,20),pg.Rect(100,240,20,20),pg.Rect(80,240,20,20),pg.Rect(40,300,20,20),pg.Rect(60,300,20,20),pg.Rect(80,300,20,20),pg.Rect(100,300,20,20),pg.Rect(120,300,20,20),pg.Rect(140,300,20,20),pg.Rect(140,320,20,20),pg.Rect(140,340,20,20),pg.Rect(120,340,20,20),pg.Rect(100,340,20,20),pg.Rect(80,340,20,20),pg.Rect(60,340,20,20),pg.Rect(40,340,20,20),pg.Rect(40,320,20,20),pg.Rect(60,320,20,20),pg.Rect(80,320,20,20),pg.Rect(100,320,20,20),pg.Rect(120,320,20,20),pg.Rect(20,420,20,20),pg.Rect(640,300,20,20),pg.Rect(640,320,20,20),pg.Rect(660,320,20,20),pg.Rect(680,340,20,20),pg.Rect(700,340,20,20),pg.Rect(720,340,20,20),pg.Rect(740,340,20,20),pg.Rect(660,340,20,20),pg.Rect(640,340,20,20),pg.Rect(660,300,20,20),pg.Rect(680,300,20,20),pg.Rect(700,300,20,20),pg.Rect(720,300,20,20),pg.Rect(740,300,20,20),pg.Rect(740,320,20,20),pg.Rect(720,320,20,20),pg.Rect(700,320,20,20),pg.Rect(680,320,20,20),pg.Rect(640,220,20,20),pg.Rect(640,240,20,20),pg.Rect(660,240,20,20),pg.Rect(680,240,20,20),pg.Rect(700,240,20,20),pg.Rect(700,220,20,20),pg.Rect(680,220,20,20),pg.Rect(660,220,20,20)]
    pacman = pg.Rect(385, 500, 30, 30)

    while game_running == True:
        #INPUTS
        pg.event.pump()
        keys = pg.key.get_pressed()

        #UPDATES

        #EVENTS
        if keys[pg.K_w] == 1:
            pacman[1] -= 30
        if keys[pg.K_a] == 1:
            pacman[0] -= 30
        if keys[pg.K_s] == 1:
            pacman[1] += 30
        if keys[pg.K_d] == 1:
            pacman[0] += 30

        #DRAWING
        screen.fill(white)
        for bob in wallslist:
            pg.draw.rect(screen, black, bob)
        pg.draw.rect(screen, green, pacman)
        pg.display.flip()
        #CLOCK
        clock.tick(60)
        
while True:
    if state == 0:
        homescreen()
    if state == 1:
        gamerunning()

