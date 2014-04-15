'''
Created on 14 avr. 2014

@author: Etienne2
'''

import Obstacle

class UnmovableObstacle(Obstacle):
    def __init__(self,Rect,life):
        super(Rect,(0,0),(0,0),life)
    def step(self):
        pass