#!/usr/bin/env python

from datetime import datetime
import time
import pygame
import os

class Capture:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    pad_size = [1000, 1000]
    cnt = 0
    data = list()
    pose = list()
    theta = list()
    arrow = list()
    jjal = 0

    def __init__(self):
        with open("/home/joonyeol/Downloads/2018516173134.txt", "r") as f:
            line = f.readline()
            self.data.append(line.split('\t'))
            while line:
                line = f.readline()
                if self.jjal % 1 == 0:
                    self.data.append(line.split('\t'))
                self.jjal += 1

        pygame.init()
        pygame.display.set_caption('screen_test')
        self.screen = pygame.display.set_mode(self.pad_size)
        self.clock = pygame.time.Clock()
        self.resolution = self.screen.get_size()

    def runCapture(self):
        runflag = True

        while runflag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runflag = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runflag = False
        
            self.screen.fill(self.WHITE)
            self.arrow.append(None)
            self.pose.append([int(float(self.data[self.cnt][1])*200)+600,int(float(self.data[self.cnt][2])*(-200))+550])
            self.theta.append(int(float(self.data[self.cnt][3])*360))
            self.arrow[self.cnt] = pygame.image.load('arrow.png')
            self.arrow[self.cnt] = pygame.transform.scale(self.arrow[self.cnt], (12, 10))
            self.arrow[self.cnt] = pygame.transform.rotate(self.arrow[self.cnt], self.theta[self.cnt])
            self.drawtext()
            self.drawObject()
            pygame.display.update()
            self.clock.tick(4)
            self.cnt += 1
        pygame.quit()

    def drawtext(self):
        font = pygame.font.SysFont(None, 40)
        text1 = font.render(str(self.data[self.cnt][0]), True, self.BLACK)
        text2 = font.render(str(self.theta[self.cnt]), True, self.BLACK)
        self.screen.blit(text1,(0,0))
        self.screen.blit(text2,(200,0))

    def drawObject(self):
        for i in range(len(self.pose)):
            self.screen.blit(self.arrow[i], self.pose[i])   
        pygame.draw.circle(self.screen, self.BLUE, self.pose[self.cnt], 10)
        
if __name__ == "__main__":
    start = Capture()
    start.runCapture()