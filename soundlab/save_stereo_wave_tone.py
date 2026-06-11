import numpy as np
import wave

def save_stereo_wav(filename, freq_left, freq_right, duration=1.0, volume=0.5):
    sample_rate = 48000
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Generate tones
    left_tone = np.sin(2 * np.pi * freq_left * t)
    right_tone = np.sin(2 * np.pi * freq_right * t)

    # Scale and convert to 16-bit PCM
    left_audio = (left_tone * 32767 * volume).astype(np.int16)
    right_audio = (right_tone * 32767 * volume).astype(np.int16)

    # Create stereo frame data
    stereo_audio = np.column_stack((left_audio, right_audio)).flatten()

    # Save WAV file
    with wave.open(filename, "wb") as f:
        f.setnchannels(2)     # stereo
        f.setsampwidth(2)     # 2 bytes per sample (16-bit)
        f.setframerate(sample_rate)
        f.writeframes(stereo_audio.tobytes())

# Example usage:
save_stereo_wav("beta_1min_639-621.wav", 639, 621, duration=60.0)