from typing import Optional, Annotated

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends

app = FastAPI()



class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()]
):
    tasks.append(task)
    return {"ok": True}
