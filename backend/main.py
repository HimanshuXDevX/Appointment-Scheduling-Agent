from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os, logging
from api.mock_calendly import router as calendly_router

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Appointment Scheduling Agent",
    version="1.0.0",
    description="Advanced AI-powered codebase analysis using Groq LLMs"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(calendly_router)

@app.get("/")
async def root():
    return {
        "service": "Appointment Scheduling Agent",
        "version": "1.0.0",
        "status": "running",
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Codebase AI Analyst",
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)