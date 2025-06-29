from fastapi import APIRouter, HTTPException
from .models import GenerateRequest, GenerateResponse
from .services import fake_llm_response

router = APIRouter()

@router.post("/generate", response_model=GenerateResponse)
def generate_text(request: GenerateRequest):
    prompt = request.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    response = fake_llm_response(prompt)
    return GenerateResponse(response=response)
