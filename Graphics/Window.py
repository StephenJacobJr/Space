'''
Created on 13 avr. 2014

@author: Etienne2
'''

import pygame,time


class Window:
    def __init__(self,size):
        self.display = pygame.display.set_mode((800,600))
        self.framerate = 30
        self.endRun = False
    def run(self):
        while not self.endRun:
            time.sleep(1.0/self.framerate)