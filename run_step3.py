from preprocess import load_audio
from features import extract_mfcc_features
from similarity import cosine_similarity

audio1, sr1 = load_audio("audio1.mp3")
audio2, sr2 = load_audio("audio2.mp3")

features1 = extract_mfcc_features(audio1, sr1)
features2 = extract_mfcc_features(audio2, sr2)

score = cosine_similarity(features1, features2)

print(f"Audio Similarity Score: {score:.3f}")
