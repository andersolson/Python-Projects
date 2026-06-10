import numpy as np
import pygame

pygame.mixer.init(frequency=48000, size=-16, channels=1)

def play_tone(freq, duration, volume=0.25):
    samplerate = 48000
    t = np.linspace(0, duration, int(duration * samplerate), False)
    tone = np.sin(2 * np.pi * freq * t)
    audio = (tone * 32767).astype(np.int16)
    sound = pygame.sndarray.make_sound(audio)
    sound.set_volume(volume)
    sound.play()
    pygame.time.wait(int(duration * 1000))

play_tone(freq=440, duration=1)
