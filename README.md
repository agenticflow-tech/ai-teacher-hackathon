# 🎓 AI Teacher: Adaptive Virtual Educator

An intelligent, adaptive educational assistant powered by the Google Gemini API (`gemini-3.6-flash`) and Streamlit. This application transforms custom topics or uploaded study materials into structured, human-like lesson plans and features an interactive misconception engine that diagnoses student errors in real time.

---

## 📐 System Architecture & Technical Implementation
* **Frontend UI:** Built with Streamlit to provide an intuitive, responsive interface.
* **AI Model Engine:** Powered by Google Gemini (`gemini-3.6-flash`) for dynamic lesson planning, context reasoning, and answer evaluation.
* **Document Processing & Knowledge Grounding:** Uses `PyPDF2` and `python-docx` to extract text from uploaded PDF, DOCX, and TXT files, injecting document context directly into prompts to minimize hallucinations.

---

## 🧠 Prompt Architecture & Adaptive Logic
* **Structured Lesson Planner:** Formulates teaching modules based on user-selected educational levels (Beginner, Intermediate, Advanced), target time limits (e.g., 5 min, 20 min, 60 min), and language choices.
* **Misconception Detection Engine:** Analyzes quiz answers step-by-step. If an error occurs, it gently identifies the specific conceptual gap and provides a fresh real-world analogy to rebuild understanding.

---

## ✨ Key Features
* **Document & Topic Learning:** Process custom textbooks/notes or learn any subject from scratch.
* **Personalized & Time-Aware:** Adapts depth and pacing dynamically based on user availability.
* **Multilingual Capability:** Supports teaching across preferred languages while maintaining lesson context.
* **Interactive Evaluation:** Tests student knowledge and offers targeted feedback.

---

## 🚧 Known Limitations & Future Roadmap
* **Current UI:** Delivers structured interactive text and visual markdown formatting.
* **Future Roadmap:** Direct integration with text-to-speech engines and realistic AI avatar video rendering pipelines.

---

## 🚀 Quick Setup & Installation

```bash
git clone [https://github.com/agenticflow-tech/ai-teacher-hackathon.git](https://github.com/agenticflow-tech/ai-teacher-hackathon.git)
cd ai-teacher-hackathon
pip install -r requirements.txt
python -m streamlit run app.py
