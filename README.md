#!/bin/bash

cat << 'EOF' > README.md
# 🤖 TalentScout Hiring Assistant

TalentScout is an AI-powered Streamlit application that simulates a short technical interview round. It generates customized technical questions based on the candidate's tech stack using the `mistralai/Mixtral-8x7B-Instruct` model via [Together.ai](https://together.ai). The app also evaluates each answer using the same model, providing instant feedback.

---

## 🚀 Features

- 🔎 Personalized technical question generation
- ✍️ Candidate information form
- 🔁 Three-question interview loop (customizable)
- 🧠 AI-powered answer evaluation (Mixtral)
- 📥 Ready for CSV export or scoring
- 💻 Simple and intuitive Streamlit interface

---

## 🛠 Tech Stack

- Python 3.8+
- Streamlit
- Together.ai API (Mixtral model)
- OpenAI Python SDK (v1+)
- dotenv

---

## 📦 Installation

Clone the repository and install dependencies:

\`\`\`bash
git clone https://github.com/your-username/talent-hiring-assistant.git
cd talent-hiring-assistant
pip install -r requirements.txt
\`\`\`

---

## 🔐 Setup API Key

Create a `.env` file in the root directory:

\`\`\`env
TOGETHER_API_KEY=your_together_api_key_here
\`\`\`

You can get your free API key from: https://www.together.ai

---

## ▶️ Run the App

\`\`\`bash
streamlit run app.py
\`\`\`

---

## 🖼 Screenshot (Optional)

Add a screenshot under `assets/screenshot.png` and uncomment this:

\`\`\`md
![screenshot](assets/screenshot.png)
\`\`\`

---

## 📁 File Structure

\`\`\`
├── app.py                # Main application file
├── .env                  # Your API key (not pushed)
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── assets/               # Optional images
\`\`\`

---

## ✍️ Author

**Suruthivimal**  
[LinkedIn Profile](https://www.linkedin.com/in/suruthivimal)

---

## 📜 License

This project is licensed under the MIT License.
EOF

echo "✅ README.md created successfully!"
