# Warehouse API

A simple FastAPI project for practice.

## Folder structure

```
warehouse-api/
├── app/
│   ├── main.py        # Starting point: creates the app
│   ├── database.py    # MySQL connection (later)
│   ├── models/        # Database tables
│   ├── schemas/       # Shape of data sent to / received from the API
│   ├── routes/        # API endpoints (URLs)
│   └── services/      # Business logic
├── requirements.txt   # Packages to install
└── README.md
```

## Run

```
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs
