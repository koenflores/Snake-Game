# -*- coding: utf-8 -*-
import pygame
import sys
import random
#import time

#key to what each direction the numbers correspond to
'''
left: 1
right: 2
up: 3
down: 4
'''

class Snake(): #snake class 
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = 4
        self.changeDirectionTo = self.direction
        self.hasFast = False
        self.hasSlow = False
        
        
    def changeDirTo(self, dire): #change direction of snake
        
        if dire == 2 and not self.direction == 1:
            self.direction = 2
          
        elif dire == 1 and not self.direction == 2:
            self.direction = 1
            
        elif dire == 3 and not self.direction == 4:
            self.direction = 3
            
        elif dire == 4 and not self.direction == 3:
            self.direction = 4
            
    def move(self, foodPos): #moves snake
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
        
     
        
    def lengthen(self, foodPos): #lengthens snake
        if self.position == foodPos:
            self.body.insert(0,list(self.position))
        
        
        
    def checkCollision(self): #checks for snake collison with self or with side boundaries
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
    

class FoodSpawner: #class for regular food spawning
    def __init__(self):
        self.position = [random.randrange(4,46)*10, random.randrange(4,46)*10]
        self.isFoodOnScreen = True
        
    def spawnFood(self): #spawns food on screen if a food is not on screen
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(3,45)*10,random.randrange(3,45)*10]
            self.isFoodOnScreen = True
        return self.position
    
    def setFoodOnScreen(self,boolean):
        self.isFoodOnScreen = boolean
        
        
class SpeedFood(FoodSpawner): #class for speed food spawning
     def __init__(self):
        self.position = [random.randrange(7,40)*10, random.randrange(7,40)*10]
        self.isFoodOnScreen = True
        
     def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(7,40)*10,random.randrange(7,40)*10]
            self.isFoodOnScreen = True
        return self.position
    
    
            
 

        
                