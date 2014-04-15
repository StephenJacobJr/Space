'''
Created on 13 avr. 2014

@author: Etienne2
'''


import time

class EntityHandler:
    def __init__(self):
        self.entities = []
        self.endRun = False
        self.timestep = 100
    def run(self):
        while not self.endRun:
            entRects = []
            for Entity in self.entities:
                entRects.append(Entity.calcStep())
                
            for entIndex0 in xrange(len(self.entities)):
                for entIndex1 in xrange(len(self.entities)):
                    if entIndex0 == entIndex1 : continue
                    if entRects[entIndex0].colliderect(entRects[entIndex1]):
                        
                    
            for Entity in self.entities:
                Entity.step()               
            time.sleep(1.0/self.timestep)