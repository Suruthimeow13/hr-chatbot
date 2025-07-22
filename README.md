# TalentScout – AI-powered Technical Interview Assistant

TalentScout is an interactive Streamlit application that simulates a technical interview based on a candidate’s tech stack. It uses powerful open-source LLMs like **Mixtral-8x7B** via **Together.ai API** to generate relevant questions and evaluate candidate answers.

---

## Features

- Collects basic candidate information
- Dynamically generates challenging technical questions using `mistralai/Mixtral-8x7B-Instruct-v0.1`
- Allows users to type in answers during the session
- Evaluates each answer using the same LLM and provides feedback with a score
- Displays full Q&A with AI feedback after the round
- Option to restart the interview

---

## Tech Stack

- [Streamlit](https://streamlit.io/)
- [Together.ai API](https://www.together.ai/)
- [OpenAI Python SDK (>=1.0.0)](https://github.com/openai/openai-python)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/talentscout-ai.git
cd talentscout-ai
```

### 2. Install dependencies

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

Create a `.env` file in the root directory and paste your Together.ai API key:

```ini
TOGETHER_API_KEY=your_together_api_key_here
```

You can get your API key from [Together.ai](https://www.together.ai)

---

## Run the App

To launch the Streamlit app, run:

```bash
streamlit run app.py
```

Then open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## Project Structure

```bash
.
├── app.py               # Main Streamlit application
├── .env                 # API key file (DO NOT commit this)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── screenshots/         # UI preview images
```

---

## Screenshots

### Candidate Form
![Candidate Form](screenshots/candidate_form.png)

### Technical Questions
![Technical Questions](screenshots/technical_questions.png)

### Evaluated Answers
![Evaluated Answers](screenshots/evaluated_answers.png)

---

## Author

**Suruthivimal**

[LinkedIn](https://www.linkedin.com/in/suruthivimal)  
[GitHub](https://github.com/suruthivimal)

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
