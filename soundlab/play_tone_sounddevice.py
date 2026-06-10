import numpy as np
import sounddevice as sd

def play_tone(frequency, duration, volume=0.25):
    samplerate = 48000 #44100 = 44.1kHz standard audio cd quality
    t = np.linspace(0, duration, int(duration * samplerate), False)
    tone = np.sin(2 * np.pi * frequency * t) * volume
    sd.play(tone, samplerate)
    sd.wait()

play_tone(frequency=440, duration=5)

