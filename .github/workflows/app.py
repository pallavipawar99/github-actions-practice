from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Welcome to the Capstone App!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
