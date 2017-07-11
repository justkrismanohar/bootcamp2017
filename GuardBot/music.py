import pygame
from threading import Thread,Event
from time import sleep

class AudioFile(Thread):
    
    def __init__(self,file):
        Thread.__init__(self)
        self._stop = Event()
        self.on = 1 #1 - play audi0, 0 - stop audio
        self.file = file #save file reference for use later

    def run(self):
        self._stop.clear()
        pygame.mixer.init()
        print("Start " + self.file)
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() and self.on == 1) == True:
                continue

    def stop(self):
        self.on = 0
        print("Stop " + self.file)
        self._stop.set()

def play(file):
    return AudioFile(file)
        

    
