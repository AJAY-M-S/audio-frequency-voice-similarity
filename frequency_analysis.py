import librosa
import numpy as np

def get_mean_frequency_spectrum(audio, sr, n_fft=2048, hop_length=512):
    """
    Compute mean frequency spectrum using STFT
    """
    stft = librosa.stft(audio, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    magnitude_db = librosa.amplitude_to_db(magnitude, ref=np.max)
    mean_spectrum = np.mean(magnitude_db, axis=1)
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    return freqs, mean_spectrum
