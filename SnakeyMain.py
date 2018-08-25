import random, pygame, sys
from SnakeySnake import Snake, FoodSpawner, SpeedFood
from pygame.locals import *
pygame.init()


#Button, gameOver and text_objects functions originates from sentdex pygame tutorial on YouTube
#link to Pygame Tutorial : https://www.youtube.com/watch?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&time_continue=1&v=ujOTNg17LjI

window = pygame.display.set_mode((500,500))  #sets size of pygame window
pygame.display.set_caption("Snakey Snake")   #caption on top of window
fps = pygame.time.Clock()

score = 0   
howDied = ''

#create objects for game
snake = Snake()
foodSpawner = FoodSpawner()
speedFoodSpawner = SpeedFood()

#function for displaying text
def text_objects(text, fonts, color):
    textSurface = fonts.render(text, True, color)
    return textSurface, textSurface.get_rect()
    

#method for Game Over Screen- takes in the final score and how snake died
def gameOver(score, howDied):
    
    #color of the screen
    window.fill(pygame.Color(225,225,225))
    
    #displays game over
    largeText = pygame.font.SysFont('comicsansms',45)
    TextSurf, TextRect = text_objects("You " + howDied , largeText, (100,100,100) )
    TextRect.center = (500/2, 500/3)
    window.blit(TextSurf, TextRect)
    
    #displays score
    largeText = pygame.font.SysFont('comicsansms',30)
    TextSurf, TextRect = text_objects("Score: " + str(score), largeText, (100,100,100) )
    TextRect.center = (500/2, 500/2)
    window.blit(TextSurf, TextRect)
    
    pygame.display.update()
    pygame.time.wait(2000)
    
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
    
#method for Game Intro
def GameIntro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        window.fill((225,225,225))
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Snakey Snake", largeText, (0,0,0))
        TextRect.center = ((500/2),(500/2))
        window.blit(TextSurf, TextRect)
        pygame.draw.rect(window, pygame.Color(225,40,0), pygame.Rect(175,310,150,50))
        button("Start!",175,310,150,50,(225,40,0), (100,100,100), Game)
        pygame.display.update()
        fps.tick(15)  
 

#button method, takes in message, x and y location, size, inital color and final color       
def button(msg, x, y, w, h, initialColor, afterColor, action=None):
    
    #creates mouse and click variables to track mouse behavior
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
  
    #if mouse is within the button range, the color changes
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, afterColor,(x,y,w,h))

        if click[0] == 1 and action != None:
            #if button is clicked the action occurs
            action()         
    else:
    #if mouse is not within button range, the color is the inital color
        pygame.draw.rect(window, initialColor,(x,y,w,h))

    
    smallText = pygame.font.SysFont("comicsansms",20)
    
    #passes into text_objects to create words
    textSurf, textRect = text_objects(msg, smallText, (100,90,80))
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)
    
    
      

def Game():
    
    score = 0
    snake = Snake()
    foodSpawner = FoodSpawner()
    speedFoodSpawner = SpeedFood()
    
    speedFoodTimer = 0 #how long speed lasts
    displaySpeedFood = 0 #wait time until next food
    displaySpeedFoodTimer = 200 #how long speed food on screen
    
    timeElapsed = 0 #keeps track of health bar
    
    ateFood = True
     
    while True:
        
        dt = fps.tick() #time that passed during each loop itteration
        
        timeElapsed += dt
        
        
        if ateFood == True: #if a food was eaten the heath bar timer resets
            timeElapsed = 0
            ateFood = False
        elif ateFood == False and 1.975*timeElapsed > 158: #if a food was not eaten and 1.975*timeElapsed >158 the game ends 
            howDied = 'Died of Starvation!'
            gameOver(score, howDied)
            
        
        
        
        for event in pygame.event.get():
            #takes in key input
            if event.type == pygame.QUIT:
                gameOver(score, howDied);
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.changeDirTo(2)
                     
                elif event.key == pygame.K_LEFT:
                    snake.changeDirTo(1)
                    
                elif event.key == pygame.K_UP:
                    snake.changeDirTo(3)
                    
                elif event.key == pygame.K_DOWN:
                    snake.changeDirTo(4)
                    
                    
        foodPos = foodSpawner.spawnFood()
        
       
        
        #if snake is on food pos the score goes up by one
        if (snake.move(foodPos) == 1): #lengthens snake if moves over a regular food
            score += 1
            foodSpawner.setFoodOnScreen(False)
            ateFood = True
            
        
        window.fill(pygame.Color(225,225,225))
        
        for ii in range(25,465): # the side boundaries of the game
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(ii,25,5,5))
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(465,ii,5,5))
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(ii,465,5,5))
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(25,ii,5,5))
            
        for ii in range(300,460): # life timer
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(ii,5,2,2))
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(ii,20,2,2))
            
        for ii in range(5,20): # life timer
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(300,ii,2,2))
            pygame.draw.rect(window, pygame.Color(0,0,0), pygame.Rect(460,ii,2,2))
            
        pygame.draw.rect(window, pygame.Color(250,0,0), pygame.Rect(302,7.5,158-(1.975*timeElapsed),13)) #draws health bar that changes with time
        
       
        
        
            
            
        if displaySpeedFood == 0 and not displaySpeedFoodTimer == 0:
            speedFoodPos = speedFoodSpawner.spawnFood()    
            pygame.draw.circle(window, pygame.Color(91,127,164), speedFoodPos, 8)    #position of fast food
        
            for x  in range(12):
                for y in range(12):
                    threshold1 = [speedFoodPos[0] + x, speedFoodPos[1] + y]
                    threshold2 = [speedFoodPos[0] - x, speedFoodPos[1] - y]
                    
                    #thresholding for circular food positon, if snake w/in region the food is eaten
                    if threshold1 == snake.position or threshold2 == snake.position:
                        speedFoodSpawner.setFoodOnScreen(False)
                        score +=3
                        randomSpeed = random.randrange(1,3)
                        speedFoodTimer = 100 #timer for speed food (blue circle)
                        ateFood = True
                        break
                    
            displaySpeedFoodTimer-=1 #food timer goes down 1 ever itteration
            if displaySpeedFoodTimer == 0:
                displaySpeedFood = 300 
                
        if displaySpeedFood != 0:
            displaySpeedFood -=1
            displaySpeedFoodTimer = 100
            
    
        for pos in snake.getBody():
            pygame.draw.rect(window, pygame.Color(0,225,0), pygame.Rect(pos[0],pos[1],10,10))
            pygame.draw.rect(window, pygame.Color(225,0,0), pygame.Rect(foodPos[0],foodPos[1],10,10)) #draws regular food
    
            
           
            
        if snake.checkCollision() == 1: #if snake collides with wall or self, game over
            howDied = 'Crashed!'
            gameOver(score, howDied);
            
        pygame.display.set_caption("Snakey Snake | Score: " + str(score))
         #refreshes 
        
        if speedFoodTimer > 1:
            if randomSpeed == 1: #if the randomSpeed is 1, then the snake moves fast
                fps.tick(70)
                speedFoodTimer-= 1
            elif randomSpeed == 2: #if the randomSpeed is 0 then the snake moves slow
                fps.tick(10)
                speedFoodTimer-=2
        else:
            fps.tick(30)
    
            
            
        pygame.display.flip()      

        
   
#What actually runs...
        
GameIntro()
Game()              

        
                