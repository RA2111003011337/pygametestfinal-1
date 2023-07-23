import pygame
import random
import math

#initialize
pygame.init()


#title
pygame.display.set_caption("pytestgame")


#screen creation
screen=pygame.display.set_mode((800,600))

#background
background=pygame.image.load("space.jpg")


#player
playerImg=pygame.image.load('space-invaders.png')
playerX=370
playerY=480
playerX_change=0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet
bulletImg=pygame.image.load('test bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=1
bullet_state="ready"

#score
score=0


def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#main quit and game run
running=True
while running:
    # screen colour
    screen.fill((32, 50, 60))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #keystroke check
        if event.type==pygame.KEYDOWN:
            print("key pressed")
            if event.key==pygame.K_LEFT:
                print("left active")
                playerX_change=-0.5
            if event.key==pygame.K_RIGHT:
                print("right active")
                playerX_change=0.5
            if event.key == pygame.K_SPACE:
                if  bullet_state=="ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)


        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                print("key released")
                playerX_change=0

    #player boundary enforce
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736

    #enemy movement
        for i in range(num_of_enemies):
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # bullet enemy collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score+= 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)
            enemy(enemyX[i], enemyY[i], i)

    #bullet movement
    if bulletY<=0:
        bullet_state = "ready"
        bulletY=480


    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change


    # player and enemy func call
    playerX+=playerX_change
    player(playerX,playerY)
    pygame.display.update()

    #bullet enemy collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(50, 150)
