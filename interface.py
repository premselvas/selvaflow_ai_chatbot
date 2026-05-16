import streamlit as st
from groq import Groq
import time

st.set_page_config(
    page_title="Selvaflow AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

/* ---- Base Resets ---- */
*, *::before, *::after {
    box-sizing: border-box;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

html, body, .stApp {
    background-color: #0b1329 !important;
    color: #f1f5f9;
}

/* ---- Main Container Layout ---- */
.block-container {
    padding: 1.5rem 2rem 7rem !important;
    max-width: 850px !important;
}

/* ---- Sidebar Layout Fixes ---- */
[data-testid="stSidebar"] {
    background-color: #0e1a35 !important;
    border-right: 1px solid #1e293b !important;
}

[data-testid="stSidebar"] * {
    color: #cbd5e1 !important;
}

/* Target internal container to handle flex structure */
[data-testid="stSidebarUserContent"] {
    display: flex;
    flex-direction: column;
    height: calc(100vh - 40px);
}

.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 4px 24px;
    border-bottom: 1px solid #1e293b;
    margin-bottom: 24px;
}

.brand-icon {
    width: 42px;
    height: 42px;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.brand-name {
    font-size: 19px;
    font-weight: 700;
    color: #ffffff !important;
    letter-spacing: -0.5px;
}

.brand-sub {
    font-size: 11px;
    color: #94a3b8 !important;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    font-weight: 600;
}

.sidebar-section-title {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #64748b !important;
    margin: 24px 0 12px 4px;
}

.feature-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 14px;
    border-radius: 10px;
    margin-bottom: 6px;
    font-size: 13.5px;
    color: #94a3b8 !important;
    background: #132247;
    border: 1px solid #1e293b;
    transition: all 0.2s ease;
}

.feature-item:hover {
    background: #172a59;
    color: #f1f5f9 !important;
    transform: translateX(2px);
}

.feature-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    box-shadow: 0 0 8px rgba(59, 130, 246, 0.6);
}

/* Modernized Clear Button with explicit margin spacing */
.stButton > button {
    background: rgba(231, 76, 60, 0.05) !important;
    border: 1px solid rgba(231, 76, 60, 0.2) !important;
    color: #ef4444 !important;
    border-radius: 10px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 10px 16px !important;
    transition: all 0.2s !important;
    width: 100% !important;
    margin-top: 16px !important;
    margin-bottom: 12px !important;
}

.stButton > button:hover {
    border-color: #ef4444 !important;
    color: #ffffff !important;
    background: #ef4444 !important;
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2);
}

/* Static footer pushed to the bottom cleanly */
.sidebar-footer {
    margin-top: auto;
    padding-top: 16px;
    border-top: 1px solid #1e293b;
    font-size: 11px;
    color: #475569 !important;
    text-align: center;
}

/* ---- Main UI Chat Layout ---- */
.chat-header {
    text-align: center;
    padding: 30px 20px 20px;
}

.logo-ring {
    width: 72px;
    height: 72px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    border-radius: 22px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 36px;
    margin-bottom: 20px;
    box-shadow: 0 0 35px rgba(37, 99, 235, 0.35);
}

.chat-header h1 {
    font-size: 32px;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 8px;
    letter-spacing: -0.8px;
    background: linear-gradient(to right, #ffffff, #cbd5e1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.chat-header p {
    font-size: 14.5px;
    color: #94a3b8;
    margin: 0;
    font-weight: 400;
}

.chat-divider {
    border: none;
    border-top: 1px solid #1e293b;
    margin: 15px 0 35px;
}

/* ---- Sleek Chat Layout ---- */
.msg-wrapper {
    display: flex;
    gap: 16px;
    margin-bottom: 24px;
    align-items: flex-start;
    width: 100%;
}

.msg-wrapper.user-wrapper {
    flex-direction: row-reverse;
}

.avatar {
    width: 38px;
    height: 38px;
    border-radius: 12px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    flex-shrink: 0;
    font-weight: 600;
}

.bot-avatar {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    font-size: 18px;
    box-shadow: 0 4px 10px rgba(37, 99, 235, 0.2);
}

.user-avatar {
    background: #1e293b;
    border: 1px solid #334155;
    color: #f1f5f9;
}

.msg-content {
    display: flex;
    flex-direction: column;
    max-width: 80%;
}

.user-wrapper .msg-content {
    align-items: flex-end;
}

.msg-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.bot-label { color: #60a5fa; }
.user-label { color: #94a3b8; }

.msg-bubble {
    padding: 14px 18px;
    border-radius: 16px;
    font-size: 14.5px;
    line-height: 1.6;
    word-break: break-word;
    white-space: pre-wrap;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.bot-bubble {
    background: #111e38;
    border: 1px solid #1e293b;
    color: #e2e8f0;
    border-top-left-radius: 4px;
}

.user-bubble {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: #ffffff;
    border-top-right-radius: 4px;
}

/* ---- Input Configuration ---- */
[data-testid="stChatInput"] {
    background-color: transparent !important;
    padding: 0 !important;
}

[data-testid="stChatInput"] textarea {
    background: #0e1a35 !important;
    border: 1px solid #1e293b !important;
    border-radius: 14px !important;
    color: #f1f5f9 !important;
    font-size: 14.5px;
    padding: 14px !important;
}

[data-testid="stChatInput"]:focus-within textarea {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
}

/* ---- Streamlit Core Brand Hiding ---- */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="brand-icon">🤖</div>
        <div>
            <div class="brand-name">Selvaflow</div>
            <div class="brand-sub">AI Assistant</div>
        </div>
    </div>
    <div class="sidebar-section-title">Capabilities</div>
    <div class="feature-item"><div class="feature-dot"></div> Coding Help</div>
    <div class="feature-item"><div class="feature-dot"></div> AI Projects</div>
    <div class="feature-item"><div class="feature-dot"></div> Freelancing</div>
    <div class="feature-item"><div class="feature-dot"></div> Business Ideas</div>
    <div class="feature-item"><div class="feature-dot"></div> Beginner Friendly</div>
    """, unsafe_allow_html=True)

    if st.button("🗑  Clear conversation"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("""
    <div class="sidebar-footer">
        Powered by Groq · LLaMA 3.3 70B
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="chat-header">
    <div class="logo-ring">🤖</div>
    <h1>Selvaflow AI</h1>
    <p>Your intelligent assistant for software, web development &amp; business ideas</p>
</div>
<hr class="chat-divider">
""", unsafe_allow_html=True)

client = Groq(api_key="")

try:
    with open("kd_try.txt", "r", encoding="utf-8") as f:
        kb = f.read()
except:
    kb = "Knowledge base not found."

system_prompt = f"""
You are Selvaflow, an intelligent AI assistant developed for freelance software and web development services.

About Selvaflow:
- Official Website: https://selvaflow.netlify.app/
- Services:
  * Portfolio Websites
  * Ecommerce Websites
  * Billing Software Solutions
  * UI/UX Design
  * Business Software Development
  * Web Applications

Rules:
- Speak professionally and simply.
- Be beginner friendly.
- Provide step-by-step explanations.
- Help users with coding, freelancing, AI projects, websites, and business ideas.
- Only answer using the provided knowledge base.
- Keep answers short, clear, and practical.
- Explain technical concepts in simple English.
- Focus on business-oriented software and website solutions.
- Do not generate unrelated information.

Important Rule:
If information is not available in the knowledge base, reply exactly:
"I only provide answers based on my knowledge base."

Response Style:
- Professional
- Beginner friendly
- Simple English
- Step-by-step guidance
- Clear explanations

Knowledge Base:
{kb}
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="msg-wrapper user-wrapper">
            <div class="avatar user-avatar">PS</div>
            <div class="msg-content">
                <div class="msg-label user-label">You</div>
                <div class="msg-bubble user-bubble">{message["content"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif message["role"] == "assistant":
        st.markdown(f"""
        <div class="msg-wrapper">
            <div class="avatar bot-avatar">🤖</div>
            <div class="msg-content">
                <div class="msg-label bot-label">Selvaflow</div>
                <div class="msg-bubble bot-bubble">{message["content"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


prompt = st.chat_input("Ask Selvaflow anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"""
    <div class="msg-wrapper user-wrapper">
        <div class="avatar user-avatar">PS</div>
        <div class="msg-content">
            <div class="msg-label user-label">You</div>
            <div class="msg-bubble user-bubble">{prompt}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("Selvaflow is thinking..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        time.sleep(0.5)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.markdown(f"""
    <div class="msg-wrapper">
        <div class="avatar bot-avatar">🤖</div>
        <div class="msg-content">
            <div class="msg-label bot-label">Selvaflow</div>
            <div class="msg-bubble bot-bubble">{reply}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
