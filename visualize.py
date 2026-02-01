import matplotlib.pyplot as plt

def plot_frequency_comparison(freqs1, spec1, freqs2, spec2):
    plt.figure(figsize=(10, 6))

    plt.plot(freqs1, spec1, label="Audio 1")
    plt.plot(freqs2, spec2, label="Audio 2")

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title("Frequency-Domain Comparison of Two Audio Signals")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
