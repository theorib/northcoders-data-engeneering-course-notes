# FastAPI

# Initializing FastAPI
```python
from fastapi import FastAPI

app = FastAPI()
```

## Simple Get Route
```sql
@app.get("/api/healthcheck")
def get_healthcheck():
    return {
        'message': 'All Ok'
    }
```

## Simple 