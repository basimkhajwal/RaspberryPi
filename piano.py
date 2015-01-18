from utils.CapacitorSense import *
from time import sleep
import pygame.mixer as p

SLEEP = 0.1
THRESH_HOLD = 1

pins = (14,15,17,18,27,22,23,24)
sounds = ("a.wav", "b.wav", "bb.wav", "c.wav", "d.wav", "e.wav", "f.wav", "g.wav")

p.init(channels=8)

channels = []
music = []

for i in range(8):
    channels.append(p.Channel(i))
    music.append(p.Sound(sounds[i]))
    
setupCapacitorSensor(4)

try:
    while True:

        for i in range(8):
            value = capacitorSense(pins[i])

            if value > THRESH_HOLD:
                channels[i].play(music[i])
            
        sleep(SLEEP)
        
except KeyboardInterrupt:
    g.cleanup()
    
    
