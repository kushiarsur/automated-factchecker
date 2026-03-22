"""
Main FastAPI application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import ALLOWED_ORIGINS, API_VERSION
from .routes import auth, posts, verify

app = FastAPI(
    title="Fact-Check Social API",
    description="API for automated fact-checking social media platform",
    version=API_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(posts.router, prefix="/api/v1")
app.include_router(verify.router, prefix="/api/v1/verify-post")

@app.get("/")
async def root():
    return {"message": "Fact-Check Social API", "version": API_VERSION, "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
