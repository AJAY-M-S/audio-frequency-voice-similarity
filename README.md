# 🎵 Audio Frequency Comparison and Voice Similarity Evaluation

## 📌 Project Overview
This project analyzes and compares two audio recordings to evaluate how similar they are based on **frequency-domain characteristics**.
Instead of relying on pitch alone, the system examines **frequency distribution, intensity variation, and time-based behavior** of audio signals and produces both a **visual comparison** and a **numerical similarity score**.

An interactive **Streamlit-based UI** allows users to upload audio files and view results instantly.

---

## 🎯 Objectives
- Perform **frequency-domain analysis** on audio signals
- Compare audio recordings using **perceptually meaningful features**
- Generate:
  - A **single frequency-domain graph** showing both audios
  - A **numerical similarity score** indicating voice similarity
- Provide a **user-friendly interface** for evaluation

---

## 🧠 Methodology

### 1. Audio Preprocessing
- Convert audio to mono
- Resample to **16 kHz**
- Normalize amplitude

---

### 2. Frequency-Domain Analysis
- Applied **Short-Time Fourier Transform (STFT)**
- Converted magnitude spectra to **decibel (dB) scale**
- Averaged spectral energy across time
- Plotted both audio spectra on a **single frequency-domain graph**

---

### 3. Feature Extraction
- Extracted **Mel-Frequency Cepstral Coefficients (MFCCs)**
- Computed **mean and standard deviation** over time
- Formed a fixed-length feature vector

---

### 4. Similarity Evaluation
- Compared MFCC feature vectors using **cosine similarity**
- Generated a normalized similarity score between **0 and 1**

---

## 🖥️ User Interface
- Audio upload (MP3, WAV, FLAC, OGG)
- Compute button
- Frequency-domain graph
- Downloadable graph
- Numerical similarity score

---

## ▶️ How to Run

```bash
pip install librosa numpy scipy matplotlib streamlit
python -m streamlit run app.py
```

---

## 📊 Sample Output
Similarity Score example:
```
0.981 (Very High Similarity)
```

---

## 👤 Author
Ajay M S
