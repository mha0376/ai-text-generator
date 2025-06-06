from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.ai_service import generate_text
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

class TextRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    output_type: str = "story"

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate(text_request: TextRequest):
    try:
        response = generate_text(text_request.prompt, text_request.max_tokens, text_request.output_type)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}