import numpy as np
import pygame

pygame.mixer.init(frequency=48000, size=-16, channels=1)

def play_tone(freq, duration=5.0, volume=0.5):
    sample_rate = 48000
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * freq * t)

    # Convert mono -> stereo (duplicate the channel)
    audio = (tone * 32767).astype(np.int16)
    audio_stereo = np.column_stack((audio, audio))

    sound = pygame.sndarray.make_sound(audio_stereo)
    sound.set_volume(volume)
    sound.play()
    pygame.time.delay(int(duration * 1000))

play_tone(50)