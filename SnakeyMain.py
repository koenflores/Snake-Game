import random, pygame, sys
from SnakeySnake import Snake, FoodSpawner, SpeedFood
pygame.init()


window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snakey Snake")
fps = pygame.time.Clock()

score = 0

snake = Snake()
foodSpawner = FoodSpawner()
speedFoodSpawner = SpeedFood()

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    


def gameOver():
    window.fill(pygame.Color(225,225,225))
    
    #displays game over
    largeText = pygame.font.SysFont('comicsansms',50)
    TextSurf, TextRect = text_objects("Game Over", largeText, (100,100,100) )
    TextRect.center = (500/2, 500/3)
    window.blit(TextSurf, TextRect)
    
    #displays score
    largeText = pygame.font.SysFont('comicsansms',30)
    TextSurf, TextRect = text_objects("Score: " + str(score), largeText, (100,100,100) )
    TextRect.center = (500/2, 500/2)
    window.blit(TextSurf, TextRect)
    
    pygame.display.update()
    pygame.time.wait(4000)
    
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
speedFoodTimer = 0 #how long speed lasts
displaySpeedFood = 0 #wait time until next food
displaySpeedFoodTimer = 200 #how long speed food on screen
   
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver();
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
    
   
    
    
    if (snake.move(foodPos) == 1): #lengthens snake if moves over a regular food
        score += 1
        foodSpawner.setFoodOnScreen(False)
        
    #print(str(displaySpeedFood) + ' displayspeedfood')   
    #print(displaySpeedFoodTimer)
    
    window.fill(pygame.Color(225,225,225))
    
    if displaySpeedFood == 0 and not displaySpeedFoodTimer == 0:
        speedFoodPos = speedFoodSpawner.spawnFood()    
        pygame.draw.circle(window, pygame.Color(91,127,164), speedFoodPos, 8)    #position of fast food
        #print('here')
        for x  in range(12):
            for y in range(12):
                threshold1 = [speedFoodPos[0] + x, speedFoodPos[1] + y]
                threshold2 = [speedFoodPos[0] - x, speedFoodPos[1] - y]
                
                if threshold1 == snake.position or threshold2 == snake.position:
                    #snake.body.pop()
                    speedFoodSpawner.setFoodOnScreen(False)
                    score +=3
                    randomSpeed = random.randrange(1,3)
                    speedFoodTimer = 100
                    break
        displaySpeedFoodTimer-=1
        if displaySpeedFoodTimer == 0:
            displaySpeedFood = 300
            
    if displaySpeedFood != 0:
        displaySpeedFood -=1
        displaySpeedFoodTimer = 100
        

    for pos in snake.getBody():
        pygame.draw.rect(window, pygame.Color(0,225,0), pygame.Rect(pos[0],pos[1],10,10))
        pygame.draw.rect(window, pygame.Color(225,0,0), pygame.Rect(foodPos[0],foodPos[1],10,10)) #draws regular food

        
       
        
    if snake.checkCollision() == 1:
        gameOver();
        
    pygame.display.set_caption("Snakey Snake | Score: " + str(score))
     #refreshes 
    
    #print('random speed' + str(randomSpeed))
    if speedFoodTimer > 1:
        if randomSpeed == 1:
            fps.tick(70)
            print('fast')
            speedFoodTimer-= 1
        elif randomSpeed == 2:
            fps.tick(10)
            print('slow')
            speedFoodTimer-=2
    else:
        fps.tick(30)
        #ateSpeedFood = False
        print('norman')
        
    pygame.display.flip()      
    #print(len(snake.getBody()))
    #print(randomSpeed)
   
                

        
                