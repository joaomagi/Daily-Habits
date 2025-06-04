from fastapi import FastAPI, Request, HTTPException, Header, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from helper import validate_habit_question, habits_ai
import json

app = FastAPI()

TOKEN_FIXO = "IHC"

class HabitRequest(BaseModel):
    question: str

def verificar_token(authorization: Optional[str] = Header(None)):
    if authorization != f"Bearer {TOKEN_FIXO}":
        raise HTTPException(status_code=401, detail="Token inválido ou ausente")

@app.post("/habito")
async def criar_habito(request: HabitRequest, _: None = Depends(verificar_token)):
    question = request.question.strip()

    if not question:
        return JSONResponse(content={"error": "A pergunta está vazia."}, status_code=400)

    if not validate_habit_question(question):
        return JSONResponse(content={"error": "Isso não é uma pergunta válida sobre hábito."}, status_code=400)

    try:
        response = habits_ai(question)
        habit_data = json.loads(response.content)
        
        if not habit_data or "name" not in habit_data:
            return JSONResponse(content={"error": "Hábito inválido gerado."}, status_code=500)
        
        return habit_data

    except json.JSONDecodeError:
        return JSONResponse(content={"error": "Erro ao interpretar a resposta da IA."}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
