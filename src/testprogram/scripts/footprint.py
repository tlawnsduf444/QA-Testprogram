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
    jjal = 0
    def __init__(self):
        with open("/home/joonyeol/Pose/pose.txt", "r") as f:
            line = f.readline()
            self.data.append(line.split('\t'))
            while line:
                line = f.readline()
                if self.jjal % 3 == 0:
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
            self.pose.append([int(float(self.data[self.cnt][1])*100)+600,int(float(self.data[self.cnt][2])*100)+400])
            self.drawtext()
            self.drawObject()
            pygame.display.update()
            self.clock.tick(3600)
            self.cnt += 1

        pygame.quit()

    def drawtext(self):
        font = pygame.font.SysFont(None, 40)
        text1 = font.render(str(self.data[self.cnt][0]), True, self.BLACK)
        self.screen.blit(text1,(0,0))

    def drawObject(self):
        pygame.draw.circle(self.screen, self.BLUE, self.pose[self.cnt], 10)
        for i in range(len(self.pose)):
            pygame.draw.circle(self.screen, self.RED, self.pose[i], 1)

if __name__ == "__main__":
    start = Capture()
    start.runCapture()