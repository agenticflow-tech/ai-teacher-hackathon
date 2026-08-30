import streamlit as st
import document_processor as dp
import teacher_engine as te

st.set_page_config(page_title="AI Teacher - Adaptive Educator", page_icon="🎓", layout="wide")

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
        content_to_teach = extracted_text[:3000]  # Grounding context
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

if 'lesson_plan' in st.session_state:
    st.markdown("---")
    st.subheader("📚 Personalized Teaching Session")
    st.markdown(st.session_state['lesson_plan'])
    
    st.markdown("---")
    st.subheader("❓ Interactive Misconception Check & Quiz")
    user_question = st.text_input("Teacher's Checkpoint Question:", value="Explain the main concept in your own words.")
    user_answer = st.text_area("Your Response:")
    
    if st.button("Submit Answer") and api_key and user_answer:
        with st.spinner("Evaluating your response..."):
            feedback = te.evaluate_student_answer(
                question=user_question,
                student_answer=user_answer,
                context=st.session_state['lesson_plan'][:1000],
                language=language
            )
            st.markdown("### 💡 Teacher Feedback & Guidance")
            st.write(feedback)