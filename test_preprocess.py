from preprocess import load_audio

audio1, sr1 = load_audio("audio1.mp3")
audio2, sr2 = load_audio("audio2.mp3")

print("Audio 1:", len(audio1), "Sample Rate:", sr1)
print("Audio 2:", len(audio2), "Sample Rate:", sr2)
