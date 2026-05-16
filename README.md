# selvaflow_ai_chatbot
# 🚀 Selvaflow AI — Intelligent AI Assistant

[Selvaflow Official Website](https://selvaflow.netlify.app/)

## 📌 Overview

Selvaflow AI is a modern AI-powered chatbot built using Python, Streamlit, and Groq API with the LLaMA 3.3 70B model.

This AI assistant helps users with:

- Coding Help
- AI Projects
- Freelancing
- Business Ideas
- Website Development
- Software Solutions

The chatbot uses a local knowledge base file to provide business-oriented and beginner-friendly responses.

---

## ✨ Features

- Modern Dark UI
- Streamlit Chat Interface
- Groq LLaMA 3.3 70B Integration
- Knowledge Base Support
- Beginner Friendly Responses
- Step-by-Step Guidance
- Custom Sidebar Design
- Clear Conversation Option
- Responsive Layout

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- HTML & CSS
- LLaMA 3.3 70B Model

---

## 📂 Project Structure

```bash
project/
│
├── interface.py
└── kd_try.txt
```

---

## ⚙️ Installation

### 1️⃣ Install Required Packages

```bash
pip install streamlit groq
```

---

### 2️⃣ Add Your Groq API Key

Inside `interface.py`

```python
client = Groq(api_key="YOUR_API_KEY")
```

Get API Key:

https://console.groq.com/keys

---

### 3️⃣ Run the Project

```bash
streamlit run interface.py
```

---

## 📘 Knowledge Base

The chatbot reads information from:

```bash
kd_try.txt
```

You can store:

- Services
- FAQs
- Business Information
- AI Knowledge
- Coding Information
- Website Details

The assistant only answers using this knowledge base.

---

## 🤖 AI Model

```bash
llama-3.3-70b-versatile
```

Powered by Groq AI.

https://groq.com/

---

## 🎨 UI Highlights

- Premium Dark Theme
- Modern Chat Bubbles
- Gradient UI Design
- Responsive Sidebar
- Professional Layout
- Smooth Hover Effects

---

## 📌 Example Use Cases

- Portfolio Website Help
- Ecommerce Website Guidance
- Billing Software Ideas
- Freelancing Support
- AI Project Assistance
- Coding Explanations

---

## 🔒 Important Rule

If information is not available in the knowledge base, the assistant replies:

```bash
"I only provide answers based on my knowledge base."
```

---

## 👨‍💻 Developer

Developed under Selvaflow for freelance software and web development services.

https://selvaflow.netlify.app/

---

# ⭐ Support

If you like this project:

- Star the repository
- Share with developers
- Improve the knowledge base
- Build your own AI assistantject is open-source and available for educational and freelance development purposes.
