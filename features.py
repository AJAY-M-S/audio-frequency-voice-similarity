import librosa
import numpy as np

def extract_mfcc_features(audio, sr, n_mfcc=13):
    """
    Extract MFCC features and return a fixed-length vector
    """
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)

    mfcc_mean = np.mean(mfcc, axis=1)
    mfcc_std = np.std(mfcc, axis=1)

    return np.concatenate([mfcc_mean, mfcc_std])
