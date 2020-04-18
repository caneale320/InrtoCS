# Caleb Neale, can4ku

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
camera.clear("blue")
logo = gamebox.from_image(400, 300,
    "https://vignette.wikia.nocookie.net/fantendo/images/8/85/Flappy_Bird.png")

score = 0


def tick(keys):
    if pygame.K_SPACE in keys: # you can check which keys are being pressed
        print(" the up arrow key is currently being pressed")
    if camera.mouseclick: #true if some mouse button is being pressed
        logo.center = camera.mouse # the current mouse position
    camera.draw(logo)
    keys.clear()
    camera.display() # you almost always want to end this method with this line

# tell gamebox to call the tick method 30 times per second
gamebox.timer_loop(30, tick)
# this line of code will not be reached until after the window is closed

