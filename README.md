🧰 Playwright Test Setup & Execution Guide

Create and activate virtual environment
```commandline
python -m venv venv
source venv/bin/activate
```

Install dependencies
```commandline
pip install -r requirements.txt
```

Install Playwright browsers
```commandline
python -m playwright install --with-deps
```


🧩 1. Run locally unicorn server:
```commandline
uvicorn main:app --reload
```



