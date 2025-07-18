# automated_notes_generator
Automated Notes Generator
Built with Streamlit · Powered by Open-Source Whisper & FFmpeg

Description
Automated Notes Generator is a web app that turns educational videos (MP4) into accurate, English transcripts—making revision and study easier than ever!
The app runs fully locally:

Upload an MP4 (such as a lecture or seminar)

Audio is extracted using FFmpeg

The Whisper model provides speech-to-text transcription in English
No OpenAI API, no cloud costs—just accurate, secure transcription on your machine.
Features
Simple drag-and-drop MP4 upload

Automatic audio extraction (FFmpeg)

Whisper (open-source) English transcription

Download your notes as a convenient .txt

User-friendly Streamlit interface

Requirements
Python 3.8+

FFmpeg installed and accessible from your PATH (Download FFmpeg)

The following Python packages (see requirements.txt):

streamlit

openai-whisper

torch (recommended for performance)
