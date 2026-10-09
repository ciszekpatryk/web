from fastapi import FastAPI 

app = FastAPI(title="TaskBoard")

@app.get("/")
def root():
    return {"message": "Hello Web"}

@app.get("/health")
def health():
    return {"status": "ok"}