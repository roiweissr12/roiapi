from fastapi import FastAPI
from roiapi.api import router as api_router

app = FastAPI(title="Fake LLM Service")
app.include_router(api_router)
