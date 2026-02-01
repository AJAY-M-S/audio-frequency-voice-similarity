from preprocess import load_audio
from frequency_analysis import get_mean_frequency_spectrum
from visualize import plot_frequency_comparison

audio1, sr1 = load_audio("audio1.mp3")
audio2, sr2 = load_audio("audio2.mp3")
freqs1, spec1 = get_mean_frequency_spectrum(audio1, sr1)
freqs2, spec2 = get_mean_frequency_spectrum(audio2, sr2)
plot_frequency_comparison(freqs1, spec1, freqs2, spec2)
