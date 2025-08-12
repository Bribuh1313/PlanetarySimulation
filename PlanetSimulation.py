#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:01:15 2025

@author: briannamerila
"""

import math
import pygame #used for animation

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Planet Simulation') #willname the pop up window
clock = pygame.time.Clock() #keeps the simulation running


#Using Newtonian physics
G = 6.67e-11 # Grav constant
scale = 6e-11 #This will scale the visulization so we can seel all orbits
zoom_scale = 1e-9 #This will let us zoom in to see individual
dt = 86400 #time step

zoomed = False #determines if we are initially zoomed out


class Body:
    def __init__(self, x, y, vx, vy, mass, radius, color,max_trail_age):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.radius = radius
        self.color = color
        self.max_trail_age = max_trail_age  # custom lifetime for trails
        self.trail = []  # [x, y, age]


    def update_position(self, bodies):
        fx = fy = 0
        for other in bodies:
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                r = math.sqrt(dx ** 2 + dy ** 2)
                if r > 0:
                    f = G * self.mass * other.mass / (r ** 2)
                    fx += f * dx / r
                    fy += f * dy / r

        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

        current_scale = zoom_scale if zoomed else scale
        screen_x = int(self.x * current_scale + WIDTH // 2)
        screen_y = int(self.y * current_scale + HEIGHT // 2)

        # Append new point with age = 0
        self.trail.append([screen_x, screen_y, 0])

        # Increase age of all points
        for point in self.trail:
            point[2] += 1

        # Remove old points
        self.trail = [p for p in self.trail if p[2] < self.max_trail_age]

    def draw(self, screen):
        if len(self.trail) > 1:
            for i in range(len(self.trail) - 1):
                x1, y1, age1 = self.trail[i]
                x2, y2, age2 = self.trail[i + 1]

                # Fade from white to black over lifetime
                fade = max(0, 255 - age1 * (255 / self.max_trail_age))
                color = (fade, fade, fade)  # white fading to black

                pygame.draw.line(screen, color, (x1, y1), (x2, y2), 1)

        current_scale = zoom_scale if zoomed else scale
        screen_x = int(self.x * current_scale + WIDTH // 2)
        screen_y = int(self.y * current_scale + HEIGHT // 2)
        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.radius)

#Creating the bodies for the sun and each of the planets, distance is in meters
#[Distance from sun in x, distance from sin in y, orbital vel in x, orbital vel in y, mass, place marker, color code, trail age]
bodies = [
    Body(0, 0, 0, 0, 1.989e30, 8, (255, 255, 0), 100),  # Sun  (1.989e30 kg, 8 pixel radius (not used in calculations, just visual))
    Body(5.79e10, 0, 0, 47360, 3.301e23, 2, (169, 169, 169), 150),  # Mercury
    Body(1.082e11, 0, 0, 35020, 4.867e24, 3, (255, 165, 0), 200),  # Venus
    Body(1.496e11, 0, 0, 29780, 5.972e24, 4, (0, 100, 255), 250),  # Earth
    Body(2.79e11, 0, 0, 24077, 6.39e23, 3, (255, 100, 0), 300),  # Mars
    Body(7.786e11, 0, 0, 13070, 1.898e27, 6, (200, 150, 100), 400),  # Jupiter
    Body(1.4335e12, 0, 0, 9680, 5.683e26, 5, (250, 200, 100), 450),  # Saturn
    Body(2.86725e12, 0, 0, 6810, 8.681e25, 4, (100, 200, 255), 500),  # Uranus
    Body(4.495e12, 0, 0, 5430, 1.024e26, 4, (0, 0, 255), 550),  # Neptune
    Body(5.906e12, 0, 0, 4670, 1.309e22, 2, (150, 100, 50), 600),  # Pluto
]
            
          
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                zoomed = not zoomed 
                
            for body in bodies:
                body.trail = []
    
    screen.fill((0, 0, 0)) #Black background in the simulation
    
    for body in bodies:
        body.update_position(bodies)
        body.draw(screen) #Draws individual bodies
    
    pygame.display.flip() 
    clock.tick(60)

pygame.quit() 
                
            
            
            
            