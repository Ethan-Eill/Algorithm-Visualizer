import pygame
import random

class Algorithm():
    def __init__(self):
        self.arr = []
        for i in range(1, 100):
            self.arr.append(i)

        random.shuffle(self.arr)
        self.width, self.height = 8, 8
        
