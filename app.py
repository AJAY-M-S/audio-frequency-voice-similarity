import streamlit as st
import tempfile
import matplotlib.pyplot as plt
import io

from preprocess import load_audio
from frequency_analysis import get_mean_frequency_spectrum
from features import extract_mfcc_features
from similarity import cosine_similarity

st.set_page_config(
    page_title="Audio Frequency Comparison & Similarity",
    layout="centered"
)

st.title("Audio Frequency Comparison & Voice Similarity Evaluation")

st.markdown("""
Upload **two audio files**, then click **Compute Similarity**.
Results remain visible even after downloading the graph.
""")

if "computed" not in st.session_state:
    st.session_state.computed = False


audio_file_1 = st.file_uploader(
    "Upload Audio File 1", type=["wav", "mp3", "flac", "ogg"], key="upload_audio_1"
)
audio_file_2 = st.file_uploader(
    "Upload Audio File 2", type=["wav", "mp3", "flac", "ogg"], key="upload_audio_2"
)


if st.button("Compute Similarity"):
    if audio_file_1 is None or audio_file_2 is None:
        st.error("Please upload BOTH audio files.")
        st.stop()

    with st.spinner("Analyzing audio signals..."):
        
        with tempfile.NamedTemporaryFile(delete=False) as f1:
            f1.write(audio_file_1.read())
            path1 = f1.name

        with tempfile.NamedTemporaryFile(delete=False) as f2:
            f2.write(audio_file_2.read())
            path2 = f2.name

        
        audio1, sr1 = load_audio(path1)
        audio2, sr2 = load_audio(path2)

        if len(audio1) < sr1 or len(audio2) < sr2:
            st.error("One or both audio files are too short.")
            st.stop()

        
        freqs1, spec1 = get_mean_frequency_spectrum(audio1, sr1)
        freqs2, spec2 = get_mean_frequency_spectrum(audio2, sr2)

        
        features1 = extract_mfcc_features(audio1, sr1)
        features2 = extract_mfcc_features(audio2, sr2)
        score = cosine_similarity(features1, features2)

        
        st.session_state.freqs1 = freqs1
        st.session_state.spec1 = spec1
        st.session_state.freqs2 = freqs2
        st.session_state.spec2 = spec2
        st.session_state.score = score
        st.session_state.sr1 = sr1
        st.session_state.sr2 = sr2
        st.session_state.len1 = len(audio1)
        st.session_state.len2 = len(audio2)

        st.session_state.computed = True

if st.session_state.computed:

    st.success("Audio analysis completed successfully!")

    
    st.subheader("Audio Information")
    col1, col2 = st.columns(2)

    with col1:
        st.audio(audio_file_1)
        st.write(f"Duration: {st.session_state.len1 / st.session_state.sr1:.2f} s")
        st.write(f"Sample Rate: {st.session_state.sr1} Hz")

    with col2:
        st.audio(audio_file_2)
        st.write(f"Duration: {st.session_state.len2 / st.session_state.sr2:.2f} s")
        st.write(f"Sample Rate: {st.session_state.sr2} Hz")

    
    st.subheader("Frequency-Domain Comparison")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(st.session_state.freqs1, st.session_state.spec1, label="Audio 1")
    ax.plot(st.session_state.freqs2, st.session_state.spec2, label="Audio 2")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude (dB)")
    ax.set_title("Frequency-Domain Comparison")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    st.download_button(
        "Download Frequency Comparison Graph",
        data=buf.getvalue(),
        file_name="frequency_comparison.png",
        mime="image/png"
    )

    
    st.subheader("Similarity Score")
    st.metric("Cosine Similarity", f"{st.session_state.score:.3f}")
    st.progress(float(st.session_state.score))
    st.caption("Similarity Confidence Level")

    if st.session_state.score >= 0.9:
        st.success("Very High Similarity")
    elif st.session_state.score >= 0.7:
        st.info("Moderate Similarity")
    else:
        st.warning("Low Similarity")
