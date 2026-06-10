import numpy as np
import pygame

pygame.mixer.init(frequency=44100, size=-16, channels=2)

def play_stereo_tones(freq_left, freq_right, duration=1.0, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Generate left & right tones
    left_tone  = np.sin(2 * np.pi * freq_left * t)
    right_tone = np.sin(2 * np.pi * freq_right * t)

    # Apply volume and convert to 16-bit integers
    left_audio  = (left_tone  * 32767 * volume).astype(np.int16)
    right_audio = (right_tone * 32767 * volume).astype(np.int16)

    # Combine into stereo (samples, 2)
    stereo_audio = np.column_stack((left_audio, right_audio))

    sound = pygame.sndarray.make_sound(stereo_audio)
    sound.play()
    pygame.time.delay(int(duration * 1000))

# Example: two different tones
play_stereo_tones(440, 225, duration=2)