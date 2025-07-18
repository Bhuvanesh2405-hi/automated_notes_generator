import streamlit as st
import tempfile
import subprocess
import os

st.set_page_config(
    page_title="Automated Notes Generator",
    page_icon="📝",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align: center; color: #1a72e8;'>
        📝 Automated Notes Generator
    </h1>
    <p style='text-align: center; color: #444;'>Upload your video, get clear English notes.<br>
    <b>Powered by Local Whisper & FFmpeg</b>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <div style='text-align: center;'>
        <img src='https://img.icons8.com/fluency/96/video.png' width='96'>
    </div>
    """, unsafe_allow_html=True)

st.info("**Step 1:** Upload your MP4 video lecture or seminar below.")

mp4_file = st.file_uploader("", type=["mp4"])

def extract_audio_with_ffmpeg(mp4_file):
    tmp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tmp_video.write(mp4_file.read())
    tmp_video.close()
    audio_path = tempfile.mktemp(suffix='.mp3')
    command = [
        'ffmpeg', '-y', '-i', tmp_video.name, '-vn', '-acodec', 'mp3', audio_path
    ]
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        os.remove(tmp_video.name)
        raise RuntimeError("FFmpeg audio extraction failed. Please check FFmpeg installation and PATH.") from e
    os.remove(tmp_video.name)
    return audio_path

def transcribe_with_whisper(audio_path, model_size="base"):
    import whisper
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path, language="en")
    return result["text"]

if mp4_file is not None:
    st.video(mp4_file)
    model_size = st.selectbox(
        "🎚️ Whisper model size (smaller=faster, larger=slower but more accurate)",
        ["tiny", "base", "small", "medium", "large"],
        index=1
    )
    if st.button("🪄 Generate English Notes"):
        with st.spinner("Extracting audio & transcribing to English. This can take several minutes..."):
            try:
                audio_mp3 = extract_audio_with_ffmpeg(mp4_file)
                transcript = transcribe_with_whisper(audio_mp3, model_size=model_size)
                st.success("🎉 Done! Transcript below.")
                st.subheader("📝 Transcript (English)")
                st.text_area("Transcript:", transcript, height=300)
                st.download_button("⬇️ Download Transcript", data=transcript, file_name="transcript.txt", mime="text/plain")
                os.remove(audio_mp3)
            except Exception as e:
                st.error(f"❌ Error: {e}")
else:
    st.warning("Please upload an MP4 video to start.")

st.markdown("<hr style='border: 1px solid #e6ecf5;'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; color: #888; font-size: 1.10em;'>
        <b>Created by:</b><br>
        NADELLA BHUVANESH &middot; PAVAN KUMAR KANCHARLA &middot; KRISHNA CHAITANYA VEJANDLA
    </div>
    """, unsafe_allow_html=True
)
