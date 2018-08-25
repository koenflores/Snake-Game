# -*- coding: utf-8 -*-
import pygame
import sys
import random
#import time

'''
left: 1
right: 2
up: 3
down: 4
'''

class Snake():
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = 4
        self.changeDirectionTo = self.direction
        self.hasFast = False
        self.hasSlow = False
        
        
    def changeDirTo(self, dire):
        
        if dire == 2 and not self.direction == 1:
            self.direction = 2
          
        elif dire == 1 and not self.direction == 2:
            self.direction = 1
            
        elif dire == 3 and not self.direction == 4:
            self.direction = 3
            
        elif dire == 4 and not self.direction == 3:
            self.direction = 4
            
    def move(self, foodPos):
        if self.direction == 2:
            self.position[0] += 10
        if self.direction == 1:
            self.position[0] -= 10
        if self.direction == 3:
            self.position[1] -= 10
        if self.direction == 4:
            self.position[1] += 10
    
        self.body.insert(0,list(self.position))
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0
        
     
        
    def lengthen(self, foodPos):
        if self.position == foodPos:
            print('yes')
            self.body.insert(0,list(self.position))
        
        
        
    def checkCollision(self):
        if self.position[0] > 455 or self.position[0] < 30:
            return 1
        elif self.position[1] > 455 or self.position[1] < 30:
            return 1
        for bodyPart in self.body[1:]:
            if self.position[0] == bodyPart:
                return 1
        else:
            return 0
    
    def getheadPos(self):
        return self.position
    
    def getBody(self):
        return self.body
    

class FoodSpawner:
    def __init__(self):
        self.position = [random.randrange(4,46)*10, random.randrange(4,46)*10]
        self.isFoodOnScreen = True
        
    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(3,45)*10,random.randrange(3,45)*10]
            self.isFoodOnScreen = True
        return self.position
    
    def setFoodOnScreen(self,boolean):
        self.isFoodOnScreen = boolean
        
        
class SpeedFood(FoodSpawner):
     def __init__(self):
        self.position = [random.randrange(5,42)*10, random.randrange(5,42)*10]
        self.isFoodOnScreen = True
    
    
            
    
'''       
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snakey Snake")
fps = pygame.time.Clock()

score = 0

snake = Snake()
foodSpawner = FoodSpawner()

def gameOver():
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
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
    if (snake.move(foodPos) == 1):
        score += 1
        foodSpawner.setFoodOnScreen(False)
        
    window.fill(pygame.Color(225,225,225))
    
    for pos in snake.getBody():
        pygame.draw.rect(window, pygame.Color(0,225,0), pygame.Rect(pos[0],pos[1],10,10))
        pygame.draw.rect(window, pygame.Color(225,0,0), pygame.Rect(foodPos[0],foodPos[1],10,10))
    if snake.checkCollision() == 1:
        gameOver();
        
    pygame.display.set_caption("Snakey Snake | Score: " + str(score))
    pygame.display.flip() #refreshes 
    fps.tick(24)
    
'''
                

        
                