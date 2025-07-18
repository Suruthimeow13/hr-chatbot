import streamlit as st
from transformers import pipeline

# Load Hugging Face model (cache to avoid reloading)
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

model = load_model()

# Function to generate technical questions (one at a time)
def generate_single_question(tech_stack):
    prompt = f"Generate 1 technical interview question for the following technologies: {tech_stack}."
    try:
        response = model(prompt, max_length=128, do_sample=True)[0]["generated_text"]
        return response.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# Initialize session state variables
if 'question_list' not in st.session_state:
    st.session_state.question_list = []
if 'current_q' not in st.session_state:
    st.session_state.current_q = ""
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'tech_stack' not in st.session_state:
    st.session_state.tech_stack = ""
if 'question_count' not in st.session_state:
    st.session_state.question_count = 0
MAX_QUESTIONS = 3  # You can change this to any number

# Streamlit App UI
st.title("TalentScout Hiring Assistant 🤖")
st.write("Hi! I'm your virtual hiring assistant. Let's get started!")

# User Details Form
if st.session_state.tech_stack == "":
    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", min_value=0)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (e.g., Python, Django, MySQL, React)")
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.session_state.tech_stack = tech_stack
        st.session_state.current_q = generate_single_question(tech_stack)
        st.success("Thanks! Let’s begin your technical round.")
        st.rerun()

# Question and Answer Loop
else:
    if st.session_state.question_count < MAX_QUESTIONS:
        st.markdown(f"### Question {st.session_state.question_count + 1}")
        st.markdown(f"**{st.session_state.current_q}**")

        with st.form("answer_form"):
            answer = st.text_area("Your Answer")
            answered = st.form_submit_button("Submit Answer")

        if answered:
            st.session_state.answers.append({
                "question": st.session_state.current_q,
                "answer": answer
            })
            st.session_state.question_count += 1

            if st.session_state.question_count < MAX_QUESTIONS:
                st.session_state.current_q = generate_single_question(st.session_state.tech_stack)
                st.rerun()
            else:
                st.success("✅ You've completed all questions!")
                st.write("### Your Responses")
                for idx, qa in enumerate(st.session_state.answers, 1):
                    st.markdown(f"**Q{idx}: {qa['question']}**")
                    st.markdown(f"**A{idx}: {qa['answer']}**")
    else:
        st.info("Interview completed.")
        if st.button("Start Over"):
            st.session_state.clear()
            st.rerun()

# Optional exit interaction
user_input = st.text_input("Say something (or type 'exit' to end):")
if user_input.lower() == "exit":
    st.write("Thank you! We'll get back to you soon.")
