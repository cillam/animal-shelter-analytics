from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Shelter Analytics API",
    description="API for shelter animal analytics and bio generation",
    version="0.1.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Shelter Analytics API", "status": "healthy"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
