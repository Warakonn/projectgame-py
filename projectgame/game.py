import pgzrun
from random import randint
def draw():
    screen.blit('bg2',(0,0))
    ship1.draw()
    if StatusGame == 0:
        message = "Are you ready, presss Enter key to play."
        screen.draw.text(message,topleft = (200,200),fontsize = 40,color = 'red')
        
    elif StatusGame == 1:
        for alien in aliens:
            alien.draw()
        screen.draw.text("Score : "+str(Score),topleft = (10,10),fontsize = 30,color = 'white')
        screen.draw.text("Time : "+str(Time),topright = (850,10),fontsize = 30,color = 'white')
        
    elif StatusGame == 2:
        screen.fill((200,100,200))
        message = "Game Over Your Score : "+str(Score)
        screen.draw.text(message,topleft = (220,300),fontsize = 50, color = 'cyan')
    for bullet in bullets:
        bullet.draw()
def on_key_down(key):
    global StatusGame, Score, Time
    if StatusGame == 0:
        if key == keys.RETURN:
            start_game()
        elif StatusGame == 2:
            if key == keys.SPACE:
                start_game()
    if key == keys.SPACE:
        sounds.shoot.play()
        bullets.append(Actor('bullet')) 
        last = len(bullets)
        bullets[last-1].pos = ship1.pos

def update():
    global StatusGame,Maxaliens
    if StatusGame == 1:
        for n in range(Maxaliens):
            aliens[n].top += speeds[n]
            if (aliens[n].top > HEIGHT):
                aliens[n].bottom = 0
    if keyboard.left:
        ship1.x=ship1.x-2
        if ship1.left<0:
            ship1.left=0
    elif keyboard.right:
        ship1.x = ship1.x+2
        if ship1.right>WIDTH:
            ship1.right=WIDTH
    for bullet in bullets:
        bullet.y-=20
        if bullet.y>WIDTH:
            bullets.remove(bullet)
        if bullet.colliderect(aliens[5]):
            bullets.remove( bullet )
           
            
       
def start_game():
    global StatusGame, Time, Score
    for n in range(Maxaliens):
        speeds[n] = randint(2,10)
        aliens[n].pos = POS[n]
    StatusGame = 1
    Time = 0
    Score = 0
    clock.schedule_interval(time_count,1)
    clock.schedule(time_out, MaxTime)

def time_count():
    global Time
    Time += 1

def time_out():
    global StatusGame
    StatusGame = 2
    clock.unschedule(time_count)


WIDTH = 900
HEIGHT = 600


POS = [(150,0),(250,0),(350,0),(450,0),(550,0),(650,0)]
Maxaliens = 6
MaxTime = 60
StatusGame = 0
Score = 0
Time = 0
aliens= []
speeds = []
ship1 = Actor('ship1')
ship1.pos = (WIDTH/2,HEIGHT-40)
for n in range(Maxaliens):
    aliens.append(Actor('alien'))
    speeds.append(randint(2,10))
    aliens[n].pos = POS[n]

bullet = Actor('bullet')
bullets = []

pgzrun.go()
