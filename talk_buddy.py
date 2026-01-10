import streamlit as st
import pyttsx3
import re

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="Talk Buddy", page_icon="🗣️", layout="centered")
st.markdown("""
<style>
.stApp {background-color: #f0f8ff;}
.title {color: #0a3d62; font-size: 40px; font-weight: bold; text-align: center;}
.subtitle {color: #1e3799; font-size: 20px; text-align: center;}
.stTextArea textarea {background-color: #ffffff; color: #0a3d62;}
button.css-1emrehy.edgvbvh3 {background-color: #1e3799; color: white;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🗣️ Talk Buddy</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Paste your text and let me read it aloud in soft Indian English!</div>', unsafe_allow_html=True)
st.write("---")

# ----------------- Initialize TTS -----------------
engine = pyttsx3.init()

# Set Indian female voice if available
voices = engine.getProperty('voices')
for v in voices:
    if "Zira" in v.name:  # Example: Windows Indian female
        engine.setProperty('voice', v.id)
        break

engine.setProperty('rate', 130)  # slower storytelling speed
engine.setProperty('volume', 1.0)  # full volume

# ----------------- Session State -----------------
if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "current" not in st.session_state:
    st.session_state.current = 0
if "cleaned" not in st.session_state:
    st.session_state.cleaned = ""

# ----------------- Text Cleaning Section -----------------
raw_text = st.text_area("Paste raw text here:", height=150)
if st.button("🧹 Clean Text"):
    cleaned = re.sub(r'\s+', ' ', raw_text)  # remove extra spaces
    sentences = re.split(r'(?<=[.!?]) +', cleaned)  # split by sentence
    st.session_state.chunks = [s.strip() for s in sentences if s.strip()]
    st.session_state.cleaned = "\n".join(st.session_state.chunks)
    st.success("✅ Text cleaned into sentences!")

# ----------------- Main Text Box -----------------
main_text = st.text_area("Text ready to speak:", value=st.session_state.cleaned, height=200)
if main_text.strip():
    st.session_state.chunks = [s.strip() for s in re.split(r'(?<=[.!?]) +', main_text) if s.strip()]

# ----------------- Start Reading Button -----------------
if st.button("▶️ Start Reading"):
    st.session_state.current = 0
    while st.session_state.current < len(st.session_state.chunks):
        sentence = st.session_state.chunks[st.session_state.current]
        st.markdown(f"**Reading:** {sentence}")
        engine.say(sentence)
        engine.runAndWait()
        st.session_state.current += 1
    st.success("✅ Finished reading all sentences!")

# ----------------- Footer -----------------
st.markdown("---")
st.markdown('<div style="text-align:center; color: #0a3d62;">Made with ❤️ by Talk Buddy</div>', unsafe_allow_html=True)
