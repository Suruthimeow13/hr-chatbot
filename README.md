# AI-Powered Hiring Assistant

An interactive Streamlit web app that acts as a virtual hiring assistant by dynamically generating technical interview questions based on the candidate's tech stack using Hugging Face's `flan-t5-base` model.

---

## Features

- Candidate detail form (name, experience, tech stack, etc.)
-  One-question-at-a-time Q&A interaction
- Next question revealed only after user submits an answer
- Summary of all questions and answers at the end
- Fast, responsive interface using Streamlit
- AI-powered question generation with Hugging Face Transformers

---

## Demo Preview

Coming Soon... *(Add a screenshot or GIF of the app here)*

---

## Tech Stack

| Technology        | Role                                 |
|-------------------|--------------------------------------|
| Python            | Core programming language            |
| Streamlit         | Frontend UI & user interaction       |
| Hugging Face (flan-t5-base) | AI model for question generation |

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/ai-hiring-assistant.git
cd ai-hiring-assistant
```

### 2. Install Dependencies

```bash
pip install streamlit transformers
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## Project Structure

```
ai-hiring-assistant/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
└── README.md              # This documentation file
```

---

## How It Works

1. User submits their profile and tech stack.
2. The app generates a technical question related to the input.
3. After the user answers, the next question is revealed.
4. This continues for a set number of rounds (default: 3).
5. A full Q&A summary is displayed at the end.

---

## Sample Output

**Q1:** What is the difference between Python lists and tuples?  
**A1:** Tuples are immutable, while lists can be modified. Tuples also use less memory.

**Q2:** Explain how decorators work in Python.  
**A2:** Decorators are functions that modify the behavior of other functions without changing their code.

*(…and so on)*

---

## Security & Privacy

- No external API key is needed.
- All data is stored in Streamlit's temporary session memory.
- Suitable for prototyping and local deployment.

---

## Future Enhancements

- Store Q&A results in a database
- Email results to recruiter or candidate
- Add question difficulty levels
- Introduce voice-to-text support

---

## Author

**Name**: Suruthivimal  
**Education**: B.Tech Artificial Intelligence & Data Science  
**GitHub**: [Suruthimeow13](https://github.com/Suruthimeow13)  
**LinkedIn**: [Suruthivimal](https://www.linkedin.com/in/suruthivimal)

---

## License

This project is open-source and available under the [MIT License](LICENSE).
