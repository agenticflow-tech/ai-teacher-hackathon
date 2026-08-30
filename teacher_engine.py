import google.generativeai as genai

def setup_gemini(api_key):
    """Initializes Google Gemini API."""
    genai.configure(api_key=api_key)

def generate_lesson_plan(topic_or_content, level, time_available, language):
    """Generates a structured, human-like lesson plan based on user inputs."""
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"""
    You are an expert, encouraging AI Teacher. 
    Create a personalized lesson plan for the following topic or educational material:
    "{topic_or_content}"
    
    Learner Profile & Requirements:
    - Educational Level: {level}
    - Time Available: {time_available} minutes
    - Language: {language}
    
    Structure the lesson like a real human teacher:
    1. Warm Introduction & Lesson Objectives
    2. Progressive Concept Breakdown (Tailored to {level} level for a {time_available}-minute session)
    3. Practical Analogies & Real-World Examples
    4. Mid-Lesson Checkpoint Questions
    5. Summary & Recommended Next Topics
    """
    
    response = model.generate_content(prompt)
    return response.text

def evaluate_student_answer(question, student_answer, context, language):
    """Evaluates student answers, detects misconceptions, and provides adaptive explanations."""
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"""
    You are a supportive AI Teacher evaluating a student's understanding.
    Question Asked: "{question}"
    Student's Answer: "{student_answer}"
    Lesson Context: "{context}"
    Teaching Language: {language}
    
    Tasks:
    1. Determine if the answer is correct, partially correct, or incorrect.
    2. If incorrect, identify the exact misconception gently and explain the concept again using a fresh analogy.
    3. Provide a constructive follow-up question to re-evaluate understanding.
    """
    
    response = model.generate_content(prompt)
    return response.text