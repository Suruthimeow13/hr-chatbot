import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key, base_url="https://api.together.xyz/v1")

# Function to generate a question using Together.ai with Mixtral
def generate_question(tech_stack):
    prompt = (
        f"You are a senior technical interviewer. Generate a challenging and relevant technical "
        f"interview question based on the following technologies: {tech_stack}. "
        "Focus on problem-solving or conceptual depth. Do not include an answer."
    )
    try:
        response = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=256
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ API error: {e}"
    
# Function to evaluate a candidate's answer using Mixtral
def evaluate_answer(question, answer):
    prompt = (
        f"You are a technical interviewer. Here's the question: '{question}' and the candidate's answer: '{answer}'. "
        "Evaluate the answer briefly (1–2 sentences) and give a rating out of 10."
    )
    try:
        response = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=150,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Evaluation error: {e}"


# Initialize session state
st.session_state.setdefault("question_list", [])
st.session_state.setdefault("current_question", "")
st.session_state.setdefault("answers", [])
st.session_state.setdefault("tech_stack", "")
st.session_state.setdefault("question_count", 0)

MAX_QUESTIONS = 3

# App UI
st.title("🤖 TalentScout Technical Interview Assistant")
st.markdown("Welcome! Let's simulate a short technical round based on your tech stack.")

# Step 1: Candidate Details Form
if not st.session_state.tech_stack:
    with st.form("candidate_details"):
        st.subheader("👤 Candidate Information")
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", min_value=0)
        position = st.text_input("Position Applying For")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (e.g., Python, React, SQL)", height=100)

        submitted = st.form_submit_button("Start Interview")
        if submitted and tech_stack.strip():
            st.session_state.tech_stack = tech_stack.strip()
            st.session_state.current_question = generate_question(tech_stack)
            st.success("✅ Interview started!")
            st.rerun()

# Step 2: Technical Interview Loop
else:
    if st.session_state.question_count < MAX_QUESTIONS:
        st.markdown(f"### 🔹 Question {st.session_state.question_count + 1}")
        st.markdown(f"**{st.session_state.current_question}**")

        with st.form("answer_form"):
            answer = st.text_area("✍️ Your Answer", height=150)
            answered = st.form_submit_button("Submit Answer")

        if answered and answer.strip():
            st.session_state.answers.append({
                "question": st.session_state.current_question,
                "answer": answer.strip()
            })
            st.session_state.question_count += 1

            if st.session_state.question_count < MAX_QUESTIONS:
                st.session_state.current_question = generate_question(st.session_state.tech_stack)
                st.rerun()
            else:
                st.success("🎉 You've completed the technical round!")

    else:
        st.subheader("📋 Your Responses with Evaluation")
        for idx, qa in enumerate(st.session_state.answers, 1):
            st.markdown(f"**Q{idx}: {qa['question']}**")
            st.markdown(f"**A{idx}: {qa['answer']}**")
            with st.spinner("Evaluating your answer..."):
                evaluation = evaluate_answer(qa['question'], qa['answer'])
                st.markdown(f"🧠 **Evaluation:** {evaluation}")

        if st.button("🔁 Start Over"):
            st.session_state.clear()
            st.rerun()

# Optional: Friendly exit
user_input = st.text_input("💬 Say something (type 'exit' to finish):")
if user_input.lower() == "exit":
    st.write("Thanks for your time! We’ll be in touch. 👋")
