import numpy as np
import wave

def generate_wav(filename, freq, duration=5.0, volume=0.5):
    sample_rate = 48000
    t = np.linspace(0, duration, int(sample_rate*duration), False)
    tone = np.sin(2*np.pi*freq*t) * volume
    audio = (tone * 32767).astype(np.int16)

    with wave.open(filename, "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        f.writeframes(audio.tobytes())

generate_wav("tone440.wav", 440)