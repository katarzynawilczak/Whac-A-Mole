import pygame
import time
import random
from pygame.locals import *
from os import path



pygame.init()

white = (255,255,255)
yellow = (255,204,0)
black = (0,0,0)
lblack = (100,100,100)
red = (255,0,0)
lred = (220,0,0)
green = (0,200,0)
lgreen = (0, 170,0)
blue = (0,150,230)
lblue = (0, 100, 170)

clock = pygame.time.Clock()
FPS=5

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Whac-A-Mole")


icon = pygame.image.load("kret.png")
pygame.display.set_icon(icon)

fontObj = pygame.font.SysFont("None", 50)
fontnorm = pygame.font.SysFont("candara", 50)
fontsmall = pygame.font.SysFont ("candara", 25)
fontbig = pygame.font.SysFont ("comicsansms", 85)

def getHighScore(file):
    
    try:
        highScoreFile = open(file, "r")
        highScore = int(highScoreFile.read())
        highScoreFile.close()
        
    except:
        highScore = 0

    return int(highScore)

def saveHighScore(newHighScore, file):
    try:
        highScoreFile = open(file, "w")
        highScoreFile.write(str(newHighScore))
        highScoreFile.close()
    except:
        print("error")
    

def text(txt, color, x, y):
    screen_text=fontObj.render(txt, True, color)
    window.blit(screen_text, [x, y])

def textcenter(txt, color, y_updown, size):
    if size == "small":
        textSurface = fontsmall.render(txt,True, color)
    elif size == "normal":
        textSurface = fontnorm.render(txt,True, color)
    elif size == "big":
        textSurface = fontbig.render(txt,True, color)
    textRect = textSurface.get_rect()
    textRect.center = (800/2), (600/2) + y_updown
    window.blit(textSurface, textRect)

def textbutton(txt, color, x, y, width, height,size):
    if size == "small":
        textSurface = fontsmall.render(txt,True, color)
    elif size == "normal":
        textSurface = fontnorm.render(txt,True, color)
    elif size == "big":
        textSurface = fontbig.render(txt,True, color)
    textRect = textSurface.get_rect()
    textRect.center = ((x+(width/2)), y+(height/2))
    window.blit(textSurface, textRect)


def button(txt, x, y, width, height, color1, color2, textcolor, textsize, action):
    mousepos = pygame.mouse.get_pos()
    mousepX= mousepos [0]
    mousepY = mousepos [1]

    mouseclick = pygame.mouse.get_pressed()
    leftclick = mouseclick [0]
    
    if x + width > mousepX > x and y + height > mousepY > y :
        pygame.draw.rect(window, color2, (x, y, width, height))
        if leftclick == 1 and action != None:
            if action == "level1":
                gameMenu()
                gameLoop()
            if action == "level2":
                gameMenu()
                gameLoopMedium()
            if action == "level3":
                redmolepic = pygame.image.load("redkret.png")
                window.fill(black)
                textcenter("Uważaj na wściekłego kreta!", red, -70, "normal")
                textcenter("Jeśli go uderzysz, gra zakończy się!", red, 0, "normal")
                window.blit(redmolepic, (350, 400))
                pygame.display.update()
                time.sleep(3)
                gameMenu()
                gameLoopHard()
            
            if action == "menu":
                gameLevel()
                
            if action == "quit":
                pygame.quit()
                quit()
                
            if action == "scores":
                listScores()
                
            if action =="pass":
                pass
           
    else:
        pygame.draw.rect(window, color1, (x, y, width, height))
        
    textbutton(txt, textcolor, x, y, width, height, textsize)


def listScores():
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
                 
        score1=getHighScore("highscore.txt")
        score2=getHighScore("highscore2.txt")
        score3=getHighScore("highscore3.txt")
        
        window.fill(yellow)
        textcenter("Najlepsze wyniki: ", white, -100, "normal")
        textcenter("Poziom I: " + str (score1), green, 0, "normal")
        textcenter("Poziom II: " + str (score2), blue, 80, "normal")
        textcenter("Poziom III: " + str (score3), red, 160, "normal")
        button("<- Powrót ", 30, 30, 120, 50, lred, red , black, "small", "menu")
        pygame.display.update()
        
def pause():
     paused = True

     while paused:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
                 
             if event.type == pygame.MOUSEBUTTONUP:
                 mousep = pygame.mouse.get_pos()
                 mouseX = mousep [0]
                 mouseY = mousep [1]
                 if 30 + 130 > mouseX > 30 and 450 + 50 > mouseY > 50 :
                         paused = False
             
         window.fill(yellow)
         textcenter("PAUZA", red, -100, "big")
         textcenter("Chcesz powrócić do gry czy wyjść?", black, 50, "small")
         button("<- Powrót ", 30, 450, 130, 50, lgreen, green , black, "small", "pass")
         button("Wyjdź", 650, 450, 100, 50, lred, red , black, "small", "quit")
         pygame.display.update() 

def gameLevel():
    level = True

    while level:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        window.fill(yellow)
        textcenter("WHAC-A-MOLE", white, -230, "big")
        textcenter("Witaj w grze!", black, -130, "normal")
        textcenter("Wybierz poziom: ", black, -80, "normal")
        textcenter("Jeśli jesteś początkującym graczem, kliknij:", green, -20, "small")
        textcenter("Jeśli chcesz zagrać na średnim poziomie, kliknij:", blue, 90, "small")
        textcenter("Jeśli jesteś zaawansowanym graczem, kliknij:", red, 190, "small")

        button("Poziom I", 330, 310, 120, 60, lgreen, green, black, "small", "level1")
        button("Poziom II ", 330, 410, 120, 60, lblue, blue, black, "small", "level2")
        button("Poziom III", 330, 510, 120, 60, lred, red, black, "small", "level3")
        button("Wyjdź z gry", 620, 550, 150, 40, black, lblack, white, "small", "quit")
        button("Najlepsze wyniki", 30, 550, 200, 40, white, lblack, black, "small", "scores")
        pygame.display.update()


def gameMenu():
    menu = True
    
    while menu:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                mousep = pygame.mouse.get_pos()
                mouseX = mousep [0]
                mouseY = mousep [1]
                if 310 + 170 > mouseX > 310 and 500 + 80 > mouseY > 500 :
                    window.fill(yellow)
                    textcenter("3", red, -50, "big")
                    pygame.display.update()
                    time.sleep(1)
                    window.fill(yellow)
                    textcenter("2", red, -50, "big")
                    pygame.display.update()
                    time.sleep(1)
                    window.fill(yellow)
                    textcenter("1", red, -50, "big")
                    pygame.display.update()
                    time.sleep(1)
                    window.fill(yellow)
                    textcenter("Start!", red, -50, "big")
                    pygame.display.update()
                    time.sleep(1)
                    menu = False
                    
        window.fill(yellow)
        
        textcenter("WHAC-A-MOLE", white, -130, "big")
        textcenter("Uderz kreta najszybciej jak potrafisz!", red, -50, "normal")
        textcenter("Za każde uderzenie dostaniesz jeden punkt.", black, 50, "small")
        textcenter("Gdy uderzysz kreta, Twoje nietrafione uderzenia wyzerują się.", black, 80, "small")
        textcenter("Gra zakończy się, gdy nie trafisz 3 razy!", black, 110, "small")
        button("Graj! ->", 310, 500, 170, 80, lgreen, green , black, "normal", "pass")        
        button("<- Powrót ", 30, 30, 120, 50, lred, red , black, "small", "menu")    
        pygame.display.update()
        
def gameLoop():
    score = 0
    missed = 0
    gameExit = False
    gameOver = False
    molepic = pygame.image.load("kret.png")    
    
    while not gameExit:
        
        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    mousep = pygame.mouse.get_pos()
                    mouseX = mousep [0]
                    mouseY = mousep [1]
                    if 450 + 300 > mouseX > 450 and 350 + 70 > mouseY > 350 :
                        gameExit = True
                        gameOver = False
                    
            window.fill(yellow)
            textcenter("Czy chcesz opuścić grę?", red, -100,"normal")
            button("<- Zagraj ponownie ", 100, 350, 250, 70, lgreen, green,black, "small", "menu")
            button("Wyjdź z gry", 500, 350, 200,70, lred, red, black, "small", "pass")
            pygame.display.update()
                
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameOver = True
                    
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mouseX = mouse [0]
                mouseY = mouse [1]
                if (randMoleX - 5 < mouseX <randMoleX + 75 and 270 < mouseY < 270 + 80):
                    score=score+1
                    missed=0
                    window.fill(yellow)
                    textSurfaceObj = fontObj.render("Uderz kreta!", 1, black, yellow)
                    textcenter("Naciśnij P aby zapauzować", red, -250, "small")
                    highScore=getHighScore("highscore.txt")
                    textcenter("Najlepszy wynik: " + str(highScore), white, -220, "small")
                    window.blit(textSurfaceObj, (300, 100))
                    pygame.draw.rect(window, black, [350,270, 80, 80],0)
                    pygame.draw.rect(window, black, [150,270, 80, 80],0)
                    pygame.draw.rect(window, black, [550,270, 80, 80],0)
                    scoreText = fontObj.render("Wynik: " + str (score),1, black, yellow)
                    missedText = fontObj.render("Nietrafione: " + str (missed), 1, black, yellow)
                    shotText = fontObj.render("Trafiony!" , True, red, yellow)
                    window.blit(shotText, (330, 400))
                    window.blit(scoreText, (50, 500))
                    window.blit(missedText, (550, 500)) 
                    pygame.display.update()
                    pygame.time.wait(500-score*10)
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 
                    pause()

                    
        if missed>=3:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                high_Score = getHighScore("highscore.txt")
                if score > high_Score:
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        saveHighScore(score, "highscore.txt")
                        window.fill(yellow)
                        textcenter("KONIEC GRY", black, -50, "big")
                        textcenter("Twój wynik to: " + str (score), red, 50, "normal")
                        textcenter("Chcesz wrócić do menu czy zakończyć grę?", red,100, "small")
                        button("<- Powrót do menu", 100, 500, 210,70, lgreen, green, black, "small", "menu")
                        button("Wyjdź z gry", 500, 500, 200,70, lred, red, black, "small", "quit")
                        textcenter("Brawo!", red, -200, "big")
                        textcenter(" Uzyskałeś najlepszy wynik!", white, -120, "normal")
                        pygame.display.update()
                        
                else:   
                    window.fill(yellow)
                    textcenter("KONIEC GRY", black, -50, "big")
                    textcenter("Twój wynik to: " + str (score), red, 50, "normal")
                    textcenter("Chcesz wrócić do menu czy zakończyć grę?", red,100, "small")
                    button("<- Powrót do menu", 100, 500, 210,70, lgreen, green, black, "small", "menu")
                    button("Wyjdź z gry", 500, 500, 200,70, lred, red, black, "small", "quit")
                    pygame.display.update()
                
        window.fill(yellow)
        textSurfaceObj = fontObj.render("Uderz kreta!", 1, black, yellow)
        window.blit(textSurfaceObj, (300, 100))
        textcenter("Naciśnij P aby zapauzować", red, -250, "small")
        highScore=getHighScore("highscore.txt")
        textcenter("Najlepszy wynik: " + str(highScore), white, -220, "small")
        pygame.draw.rect(window, black, [350,270, 80, 80],0)
        pygame.draw.rect(window, black, [150,270, 80, 80],0)
        pygame.draw.rect(window, black, [550,270, 80, 80],0)

        randMoleX = random.randrange(155,556,200)
        window.blit(molepic, (randMoleX, 280))

        scoreText = fontObj.render("Wynik: " + str (score),1, black, yellow)
        missedText = fontObj.render("Nietrafione: " + str (missed), 1, black, yellow)
        window.blit(scoreText, (50, 500))
        window.blit(missedText, (550, 500))
        pygame.display.update()
        
        missed=missed+1
        pygame.time.wait(1000-score*10)
        clock.tick(FPS)
    
    pygame.quit()
    quit()

    
def gameLoopMedium():
    score = 0
    missed = 0
    gameExit = False
    gameOver = False
    molepic = pygame.image.load("kret.png")    
        
    while not gameExit:
        
        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    mousep = pygame.mouse.get_pos()
                    mouseX = mousep [0]
                    mouseY = mousep [1]
                    if 450 + 300 > mouseX > 450 and 350 + 70 > mouseY > 350 :
                        gameExit = True
                        gameOver = False
                    
            window.fill(yellow)
            textcenter("Czy chcesz opuścić grę?", red, -100,"normal")
            button("<- Zagraj ponownie ", 100, 350, 250, 70, lgreen, green,black, "small", "menu")
            button("Wyjdź z gry", 500, 350, 200,70, lred, red, black, "small", "pass")
            pygame.display.update()
                
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameOver = True
                        
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mouseX = mouse [0]
                mouseY = mouse [1]
                if (randMoleX - 5 < mouseX <randMoleX + 75 and randMoleY-10 < mouseY <randMoleY + 70):
                    score=score+1
                    missed=0
                    window.fill(yellow)
                    textSurfaceObj = fontObj.render("Uderz kreta!", 1, black, yellow)
                    textcenter("Naciśnij P aby zapauzować", red, -250, "small")
                    highScore=getHighScore("highscore2.txt")
                    textcenter("Najlepszy wynik: " + str(highScore), white, -220, "small")
                    window.blit(textSurfaceObj, (300, 100))
                    pygame.draw.rect(window, black, [250,200, 80, 80],0)
                    pygame.draw.rect(window, black, [450,200, 80, 80],0)
                    pygame.draw.rect(window, black, [250,300, 80, 80],0)
                    pygame.draw.rect(window, black, [450,300, 80, 80],0)
                    scoreText = fontObj.render("Wynik: " + str (score),1, black, yellow)
                    missedText = fontObj.render("Nietrafione: " + str (missed), 1, black, yellow)
                    shotText = fontObj.render("Trafiony!" , True, red, yellow)
                    window.blit(shotText, (330, 400))
                    window.blit(scoreText, (50, 500))
                    window.blit(missedText, (550, 500)) 
                    pygame.display.update()
                    pygame.time.wait(500-score*10)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 
                    pause()

                        
        if missed>=3:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                high_Score = getHighScore("highscore2.txt")
                if score > high_Score:
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        saveHighScore(score, "highscore2.txt")
                        window.fill(yellow)
                        textcenter("KONIEC GRY", black, -50, "big")
                        textcenter("Twój wynik to: " + str (score), red, 50, "normal")
                        textcenter("Chcesz wrócić do menu czy zakończyć grę?", red,100, "small")
                        button("<- Powrót do menu", 100, 500, 210,70, lgreen, green, black, "small", "menu")
                        button("Wyjdź z gry", 500, 500, 200,70, lred, red, black, "small", "quit")
                        textcenter("Brawo!", red, -200, "big")
                        textcenter(" Uzyskałeś najlepszy wynik!", white, -120, "normal")
                        pygame.display.update()
                        
                else:   
                    window.fill(yellow)
                    textcenter("KONIEC GRY", black, -50, "big")
                    textcenter("Twój wynik to: " + str (score), red, 50, "normal")
                    textcenter("Chcesz wrócić do menu czy zakończyć grę?", red,100, "small")
                    button("<- Powrót do menu", 100, 500, 210,70, lgreen, green, black, "small", "menu")
                    button("Wyjdź z gry", 500, 500, 200,70, lred, red, black, "small", "quit")
                    pygame.display.update()

        window.fill(yellow)
        textSurfaceObj = fontObj.render("Uderz kreta!", 1, black, yellow)
        window.blit(textSurfaceObj, (300, 100))
        textcenter("Naciśnij P aby zapauzować", red, -250, "small")
        highScore=getHighScore("highscore2.txt")
        textcenter("Najlepszy wynik: " + str(highScore), white, -220, "small")
        pygame.draw.rect(window, black, [250,200, 80, 80],0)
        pygame.draw.rect(window, black, [450,200, 80, 80],0)
        pygame.draw.rect(window, black, [250,300, 80, 80],0)
        pygame.draw.rect(window, black, [450,300, 80, 80],0)

        randMoleX = random.randrange(255,456,200)
        randMoleY = random.randrange(210,311,100)
        window.blit(molepic, (randMoleX, randMoleY))

        scoreText = fontObj.render("Wynik: " + str (score),1, black, yellow)
        missedText = fontObj.render("Nietrafione: " + str (missed), 1, black, yellow)
        window.blit(scoreText, (50, 500))
        window.blit(missedText, (550, 500))
        pygame.display.update()
            
        missed=missed+1
        pygame.time.wait(800-score*10)
        clock.tick(FPS)
        
    pygame.quit()
    quit()
    
def gameLoopHard():
    score = 0
    missed = 0
    gameExit = False
    gameOver = False
    molepic = pygame.image.load("kret.png")
    redmolepic = pygame.image.load("redkret.png")
        
    while not gameExit:
        
        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    mousep = pygame.mouse.get_pos()
                    mouseX = mousep [0]
                    mouseY = mousep [1]
                    if 450 + 300 > mouseX > 450 and 350 + 70 > mouseY > 350 :
                        gameExit = True
                        gameOver = False
                    
            window.fill(yellow)
            textcenter("Czy chcesz opuścić grę?", red, -100,"normal")
            button("<- Zagraj ponownie ", 100, 350, 250, 70, lgreen, green,black, "small", "menu")
            button("Wyjdź z gry", 500, 350, 200,70, lred, red, black, "small", "pass")
            pygame.display.update()
                
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                gameOver = True
                        
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mouseX = mouse [0]
                mouseY = mouse [1]
                if blackOrRed==0:
                    if (randMoleX - 5 < mouseX <randMoleX + 75 and randMoleY-10 < mouseY <randMoleY + 70):
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                            window.fill(yellow)
                            textcenter("KONIEC GRY", black, -50, "big")
                            textcenter("Uderzyłeś wściekłego kreta!", red, -150, "normal")
                            textcenter("Chcesz wrócić do menu czy zakończyć grę?", red,100, "small")
                            button("<-Powróć do menu", 100, 500, 210,70, lred, red, black, "small", "menu")
                            button("Wyjdź z gry", 500, 500, 200,70, lred, red, black, "small", "quit")
                            pygame.display.update()
                            
                else:
                    if (randMoleX - 5 < mouseX <randMoleX + 75 and randMoleY-10 < mouseY <randMoleY + 70):
                        score=score+1
                        missed=0
                        window.fill(yellow)
                        textSurfaceObj = fontObj.render("Uderz kreta!", 1, black, yellow)
                        textcenter("Naciśnij P aby zapauzować", red, -250, "small")
                        highScore=getHighScore("highscore3.txt")
                        textcenter("Najlepszy wynik: " + str(highScore), white, -220, "small")
                        window.blit(textSurfaceObj, (300, 100))
                        pygame.draw.rect(window, black, [250,150, 80, 80],0)
                        pygame.draw.rect(window, black, [350,150, 80, 80],0)
                        pygame.draw.rect(window, black, [450,150, 80, 80],0)
                        pygame.draw.rect(window, black, [250,250, 80, 80],0)
                        pygame.draw.rect(window, black, [350,250, 80, 80],0)
                        pygame.draw.rect(window, black, [450,250, 80, 80],0)
                        pygame.draw.rect(window, black, [250,350, 80, 80],0)
                        pygame.draw.rect(window, black, [350,350, 80, 80],0)
                        pygame.draw.rect(window, black, [450,350, 80, 80],0)
                        scoreText = fontObj.render("Wynik: " + str (score),1, black, yellow)
                        missedText = fontObj.render("Nietrafione: " + str (missed), 1, black, yellow)
                        shotText = fontObj.render("Trafiony!" , True, red, yellow)
                        window.blit(shotText, (330, 450))
                        window.blit(scoreText, (50, 500))
                        window.blit(missedText, (550, 500)) 
                        pygame.display.update()
                        pygame.time.wait(800-score*10)
                       
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 
                    pause()

                        
        if missed>=3:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                high_Score = getHighScore("highscore3.txt")
                if score > high_Score:
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        saveHighScore(score, "highscore3.txt")
                        window.fill(yellow)
                        textcenter("KONIEC GRY", black, -50, "big")
                        textcenter("Twój wynik to: " + str (score), red, 50, "normal")
                        textcenter("Chcesz wrócić do menu czy zakończyć grę?", red,100, "small")
                        button("<- Powrót do menu", 100, 500, 210,70, lgreen, green, black, "small", "menu")
                        button("Wyjdź z gry", 500, 500, 200,70, lred, red, black, "small", "quit")
                        textcenter("Brawo!", red, -200, "big")
                        textcenter(" Uzyskałeś najlepszy wynik!", white, -120, "normal")
                        pygame.display.update()
                        
                else:   
                    window.fill(yellow)
                    textcenter("KONIEC GRY", black, -50, "big")
                    textcenter("Twój wynik to: " + str (score), red, 50, "normal")
                    textcenter("Chcesz wrócić do menu czy zakończyć grę?", red,100, "small")
                    button("<- Powrót do menu", 100, 500, 210,70, lgreen, green, black, "small", "menu")
                    button("Wyjdź z gry", 500, 500, 200,70, lred, red, black, "small", "quit")
                    pygame.display.update()
                

        blackOrRed = random.randrange(0,5,1)                    
        if blackOrRed ==0:
                
            window.fill(yellow)
            textSurfaceObj = fontObj.render("Uderz kreta!", 1, black, yellow)
            window.blit(textSurfaceObj, (300, 100))
            textcenter("Naciśnij P aby zapauzować", red, -250, "small")
            highScore=getHighScore("highscore3.txt")
            textcenter("Najlepszy wynik: " + str(highScore), white, -220, "small")
            pygame.draw.rect(window, black, [250,150, 80, 80],0)
            pygame.draw.rect(window, black, [350,150, 80, 80],0)
            pygame.draw.rect(window, black, [450,150, 80, 80],0)
            pygame.draw.rect(window, black, [250,250, 80, 80],0)
            pygame.draw.rect(window, black, [350,250, 80, 80],0)
            pygame.draw.rect(window, black, [450,250, 80, 80],0)
            pygame.draw.rect(window, black, [250,350, 80, 80],0)
            pygame.draw.rect(window, black, [350,350, 80, 80],0)
            pygame.draw.rect(window, black, [450,350, 80, 80],0)

            randMoleX = random.randrange(255,456,100)
            randMoleY = random.randrange(160,361,100)
            
            window.blit(redmolepic, (randMoleX, randMoleY))
                
            scoreText = fontObj.render("Wynik: " + str (score),1, black, yellow)
            missedText = fontObj.render("Nietrafione: " + str (missed), 1, black, yellow)
            window.blit(scoreText, (50, 500))
            window.blit(missedText, (550, 500))
            pygame.display.update()
                
            pygame.time.wait(800-score*10)
            clock.tick(FPS)
                    
        else:
            
            window.fill(yellow)
            textSurfaceObj = fontObj.render("Uderz kreta!", 1, black, yellow)
            window.blit(textSurfaceObj, (300, 100))
            textcenter("Naciśnij P aby zapauzować", red, -250, "small")
            highScore=getHighScore("highscore3.txt")
            textcenter("Najlepszy wynik: " + str(highScore), white, -220, "small")
            pygame.draw.rect(window, black, [250,150, 80, 80],0)
            pygame.draw.rect(window, black, [350,150, 80, 80],0)
            pygame.draw.rect(window, black, [450,150, 80, 80],0)
            pygame.draw.rect(window, black, [250,250, 80, 80],0)
            pygame.draw.rect(window, black, [350,250, 80, 80],0)
            pygame.draw.rect(window, black, [450,250, 80, 80],0)
            pygame.draw.rect(window, black, [250,350, 80, 80],0)
            pygame.draw.rect(window, black, [350,350, 80, 80],0)
            pygame.draw.rect(window, black, [450,350, 80, 80],0)

            randMoleX = random.randrange(255,456,100)
            randMoleY = random.randrange(160,361,100)
            window.blit(molepic, (randMoleX, randMoleY))
                
            scoreText = fontObj.render("Wynik: " + str (score),1, black, yellow)
            missedText = fontObj.render("Nietrafione: " + str (missed), 1, black, yellow)
            window.blit(scoreText, (50, 500))
            window.blit(missedText, (550, 500))
            pygame.display.update()

            missed=missed+1
            pygame.time.wait(800-score*10)
            clock.tick(FPS)
        
    pygame.quit()
    quit()    

    
gameLevel()
