Here’s a complete **`README.md`** file you can use for your GitHub repository:

---

```markdown
# 🎓 Campus Assistant Chatbot

An interactive campus assistant chatbot built with **FastAPI**, **OpenRouter GPT-4o**, and a modern HTML/CSS/JS frontend.

It allows students to ask questions about their campus, get voice-enabled responses, and navigate using an engaging UI with features like dark mode, avatars, and typing animation.

---

## 🚀 Features

- 🧠 Powered by GPT-4o (via OpenRouter)
- 🎤 Speech-to-text input with mic button
- 💬 Chat bubbles with user & bot avatars
- 🌓 Toggle between light/dark themes
- ✨ Typing animation for responses
- 📍 Navigation help for campus locations (coming soon)

---

## 📁 Project Structure

```

campus-chatbot/
│
├── main.py               # FastAPI backend
├── static/
│   └── chat.html         # Frontend (HTML, CSS, JS)
└── venv/                 # (Optional) Python virtual environment

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/campus-chatbot.git
cd campus-chatbot
````

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn openai python-multipart httpx
```

### 4. Set Your API Key

```bash
$env:OPENAI_API_KEY="your_openrouter_key"  # Windows PowerShell
# export OPENAI_API_KEY=your_openrouter_key  # macOS/Linux
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

Then open your browser and visit:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌐 OpenRouter API Key

* Get your free API key from: [https://openrouter.ai](https://openrouter.ai)
* Make sure to choose GPT-4o model (`openai/gpt-4o`) in the code.

---

## 📸 Preview

![Chat UI Screenshot](https://i.imgur.com/7k12EPD.png)

---

## 📄 License

This project is open-source under the **MIT License**.

```

---

Let me know if you want this tailored for a team, with credits, or deployed to platforms like Vercel or Render.
```
