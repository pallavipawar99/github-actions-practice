from fastapi import FastAPI
import uvicorn

app = FastAPI(title="DevOpsVaultX Insights API")

@app.get("/")
def read_root():
    return {"message": "Welcome to DevOpsVaultX Insights API", "status": "Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)