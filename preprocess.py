import librosa
import numpy as np

def load_audio(path, sr=16000):
    """
    Load audio, convert to mono, resample, and normalize
    """
    audio, sr = librosa.load(path, sr=sr, mono=True)
    audio = audio / np.max(np.abs(audio))
    return audio, sr
