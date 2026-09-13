import io
import re
import streamlit as st
from gtts import gTTS
import document_processor as dp
import teacher_engine as te

# Page Configuration
st.set_page_config(page_title="AI Teacher - Adaptive Educator", page_icon="🎓", layout="wide")

# Helper Function: Generate Spoken Audio for Lesson Content
def generate_audio_stream(text, language_choice):
    try:
        # Map selected language to TTS engine voice code
        lang_code = 'hi' if language_choice in ["Hindi", "Hinglish"] else 'en'
        # Clean markdown symbols for natural speech rendering
        clean_text = re.sub(r'[*#$`_~]', '', text)
        if not clean_text.strip():
            return None
        tts = gTTS(text=clean_text[:1500], lang=lang_code, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp
    except Exception:
        return None

# Header Presentation
st.title("🎓 AI Teacher: Adaptive Virtual Educator")
st.write("Welcome to your personalized AI teaching session.")

# Sidebar Configuration
st.sidebar.header("⚙️ Lesson Settings")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

level = st.sidebar.selectbox("Educational Level", ["Beginner", "Intermediate", "Advanced"])
time_available = st.sidebar.slider("Available Time (Minutes)", 5, 60, 20)
language = st.sidebar.selectbox("Teaching Language", ["English", "Hindi", "Hinglish"])

# File Upload or Topic Input
uploaded_file = st.sidebar.file_uploader("Upload Study Material (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
topic_input = st.text_input("Or enter a topic directly:", placeholder="e.g., Explain Newton's Laws of Motion")

if api_key:
    te.setup_gemini(api_key)

if st.button("🚀 Start Lesson") and api_key:
    content_to_teach = ""

    if uploaded_file:
        extracted_text = dp.extract_text_from_file(uploaded_file)
        content_to_teach = extracted_text[:3000] # Grounding context window
        st.info(f"Loaded content from {uploaded_file.name}")
    elif topic_input:
        content_to_teach = topic_input
    else:
        st.warning("Please upload a file or enter a topic.")

    if content_to_teach:
        with st.spinner("Preparing your personalized lesson plan..."):
            lesson_plan = te.generate_lesson_plan(content_to_teach, level, time_available, language)
            st.session_state['lesson_plan'] = lesson_plan
            st.success("Lesson plan generated!")

# Main Classroom Lesson Session Display
if 'lesson_plan' in st.session_state:
    st.markdown("---")
    
    # Human-Like AI Avatar Video Visual Block (15% Weight)
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 25px;">
            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=600" 
                 style="border-radius: 14px; width: 260px; box-shadow: 0 4px 12px rgba(0,0,0,0.4);" 
                 alt="AI Educator Avatar">
            <p style="color: #888888; margin-top: 8px; font-size: 14px;">🎥 <b>AI Virtual Educator - Live Avatar Session</b></p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.subheader("📚 Personalized Teaching Session")
    
    # Render Lesson Markdown Content
    st.markdown(st.session_state['lesson_plan'])
    
    # AI Voice Audio Generation & Playback Widget (10% Weight)
    st.markdown("### 🔊 Spoken Audio Explanation")
    with st.spinner("Generating AI spoken voice explanation..."):
        audio_fp = generate_audio_stream(st.session_state['lesson_plan'], language)
        if audio_fp:
            st.audio(audio_fp, format="audio/mp3")
        else:
            st.caption("Audio playback unavailable for this section.")

    st.markdown("---")
    st.subheader("❓ Interactive Misconception Check & Quiz")
    user_question = st.text_input("Teacher's Checkpoint Question:", value="Explain the main concept in your own words.")
    user_answer = st.text_area("Your Response:")

    if st.button("Submit Answer") and api_key and user_answer:
        with st.spinner("Evaluating your response & analyzing misconceptions..."):
            feedback = te.evaluate_student_answer(
                question=user_question,
                student_answer=user_answer,
                context=st.session_state['lesson_plan'][:1000],
                language=language
            )
            st.markdown("### 💡 Teacher Diagnostic Feedback & Guidance")
            st.info(feedback)
            
            # Spoken Audio Feedback for Quiz
            feedback_audio = generate_audio_stream(feedback, language)
            if feedback_audio:
                st.audio(feedback_audio, format="audio/mp3")
import streamlit as st
import streamlit.components.v1 as components

# Floating AI Teacher Avatar (Compact Mode)
components.html(
    """
    <script type="module"
      src="https://agent.d-id.com/v2/index.js"
      data-mode="fabio"
      data-client-key="ck_u1_ySW-cl5V8NRIAcl3NB"
      data-agent-id="v2_agt_UJ5ust4q"
      data-name="did-agent"
      data-monitor="true"
      data-orientation="horizontal"
      data-position="right"
      data-open-mode="compact">
    </script>
    """,
    height=600,
)
