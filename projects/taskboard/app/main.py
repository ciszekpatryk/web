from fastapi import FastAPI
from fastapi import Response
from pydantic import BaseModel
from fastapi import HTTPException

class TaskIn(BaseModel):
    title: str
    status: str = "open"
    priority: str = "medium"

app = FastAPI(title="TaskBoard")

@app.get("/")
def root():
    return {"message": "Hello Web"}

@app.get("/health")
def health():
    return {"status": "ok"}

TASKS: dict[int, dict] = {
    1: {"id": 1, "title": "Przygotować środowisko",
        "status": "done", "priority": "high"},
    2: {"id": 2, "title": "Przeczytać RFC 9110",
        "status": "open", "priority": "medium"},
}

NEXT_ID = 3

@app.get("/tasks")
def list_tasks(status: str | None = None, limit: int = 20):
    items = list(TASKS.values())
    if status is not None:
        items = [t for t in items if t["status"] == status]
    return {"items": items[:limit], "total": len(items)}

@app.get("/tasks/check-title")
def check_title(title: str):
    for task in TASKS.values():
        if task["title"].lower() == title.lower():
            raise HTTPException(status_code=409, detail="Tytuł zadania już istnieje")
    return {"message": "Tytuł jest dostępny"}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Zadanie nie istnieje")
    return task

@app.put("/tasks", status_code=201)
def create_task(payload: TaskIn, response: Response):
    global NEXT_ID
    task = {
        "id": NEXT_ID,
        "title": payload.title,
        "status": payload.status,
        "priority": payload.priority
    }
    TASKS[NEXT_ID] = task
    response.headers["Location"] = f"/tasks/{NEXT_ID}"
    NEXT_ID += 1
    return task

@app.post("/tasks", status_code=201)
def create_task(payload: TaskIn, response: Response):
    global NEXT_ID
    task = {
        "id": NEXT_ID,
        "title": payload.title,
        "status": payload.status,
        "priority": payload.priority
    }
    TASKS[NEXT_ID] = task
    response.headers["Location"] = f"/tasks/{NEXT_ID}"
    NEXT_ID += 1
    return task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Zadanie nie istnieje")
    del TASKS[task_id]
