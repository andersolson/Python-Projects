import numpy as np
import pygame

pygame.mixer.init(frequency=44100, size=-16, channels=1)

def play_tone(freq, duration=1.0, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * freq * t)
    audio = (tone * 32767).astype(np.int16)
    sound = pygame.sndarray.make_sound(audio)
    sound.set_volume(volume)
    sound.play()
    pygame.time.delay(int(duration * 1000))

play_tone(440)