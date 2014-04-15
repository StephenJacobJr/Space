'''
Created on 13 avr. 2014

@author: Etienne2
'''
from pygame import Rect

class Entity:
    def __init__(self,Rect,maxSpeed,maxAcc,weight,life):
        self.x,self.y = Rect.x,Rect.y
        self.weight = weight
        self.width,self.height = Rect.width,Rect.height
        self.vx,self.vy = 0,0
        self.ax,self.ay = 0,0
        self.mvx,self.mvy = maxSpeed[0],maxSpeed[1]
        self.max,self.may = maxAcc[0],maxAcc[1]
        
    def setAcc(self,acc):
        self.ax,self.ay = acc[0],acc[1]
       
    def addAcc(self,acc):
        self.ax += acc[0]
        self.ay += acc[1]
        
    def calcStep(self):
        vx = self.vx + self.ax
        vy = self.vy + self.ay
            
        if vx > self.mvx : vx = self.vmx
        if vy > self.mvy : vy = self.vmy
        
        x = self.x + vx
        y = self.y + vy
        
        Result = Rect(x,y,self.width,self.height)
        
        return Result
    
    def step(self):        
        self.vx += self.ax
        self.vy += self.ay
        if self.vx > self.mvx : self.vx = self.vmx
        if self.vy > self.mvy : self.vy = self.vmy
        
        self.x += self.vx
        self.y += self.vy
        
        