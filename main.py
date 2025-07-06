import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

# ✅ Environment key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or "enter your api key"

# ✅ OpenRouter / OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENAI_API_KEY"]
)

# ✅ FastAPI setup
app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Static files (HTML/CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Simple memory (in production use Redis or DB)
user_memory = {}

# ✅ Serve chat UI
@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/chat.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# ✅ Handle chat + memory
@app.post("/chat")
async def chat(request: Request, user_input: str = Form(...)):
    client_ip = request.client.host  # Use IP as session ID
    history = user_memory.get(client_ip, [])

    # Add user message to history
    history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=history,
            max_tokens=600,
            temperature=0.7
        )

        bot_reply = response.choices[0].message.content.strip()
        history.append({"role": "assistant", "content": bot_reply})
        user_memory[client_ip] = history[-10:]  # keep last 10 messages

        return JSONResponse(content={"response": bot_reply})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
