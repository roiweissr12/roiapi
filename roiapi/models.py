from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Prompt to send to the LLM")


class GenerateResponse(BaseModel):
    response: str
