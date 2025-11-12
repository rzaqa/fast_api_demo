from typing import Optional, Annotated

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends

from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("DB is ready")
    yield
    print("Switching Off")

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
