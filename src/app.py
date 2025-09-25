from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import routes  # import your router
import uvicorn

app = FastAPI(
    title="Job Description Generator API",
    description="Agentic system for creating structured job descriptions",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(routes.router, prefix="/api")  # assuming your router is named `router` in routes.py

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
