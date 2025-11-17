# FastAPI Tasks Demo

Simple FastAPI project that demonstrates how to build a small async API with SQLite.  
The service provides two endpoints to create a task and list every stored task.

## Tech stack
- Python 3.11+
- FastAPI & Uvicorn
- SQLAlchemy (async) with SQLite
- Pydantic models for validation

## Getting started
1. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API with auto reload
   ```bash
   uvicorn main:app --reload
   ```
4. Open the interactive docs at http://127.0.0.1:8000/docs (Swagger UI) or http://127.0.0.1:8000/redoc.

The database file `tasks.db` is created automatically. On every app start the tables are recreated (see `lifespan` in `main.py`), so the data is cleared whenever the server restarts.

## API reference

### Create a task
- **Endpoint:** `POST /tasks`
- **Body:**
  ```json
  {
    "name": "Buy groceries",
    "description": "Milk, bread, eggs"
  }
  ```
- **Response:**
  ```json
  {
    "ok": true,
    "task_id": 1
  }
  ```

### List tasks
- **Endpoint:** `GET /tasks`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Buy groceries",
      "description": "Milk, bread, eggs"
    }
  ]
  ```

You can interact with the API via Swagger UI, `curl`, or REST clients like HTTPie and Postman.

## Development tips
- Use `uvicorn main:app --reload --port 9000` to change the default port.
- Update dependencies in `requirements.txt` and reinstall when upgrading FastAPI or SQLAlchemy.
- Run `rm tasks.db` if you need to wipe the database outside the app lifecycle.
