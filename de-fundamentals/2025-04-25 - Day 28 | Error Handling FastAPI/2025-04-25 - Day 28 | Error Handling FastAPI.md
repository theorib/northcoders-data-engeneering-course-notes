# 2025-04-25 - Day 28 | Error Handling FastAPI
# Fast 
- FastAPI returns a 404 if user tries to access an endpoint that does not exist
- FastAPI returns 405 if user tries a method that doesn't exist on the endpoint
- FastAPI raises a 500 if there was a database error propagated inside the server
- FastAPI raises 422 if user puts wrong data as input both in url and boy content



## Handling Error with FastAPI

`from fastapi import FastAPI, HTTPException`
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

## @app.exception_handler(ExceptionName):
[@app.exception_handler](https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers)
```python
from fastapi.responses import JSONResponse

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
```


## notes to self
- check that patch works with not all properties and with all properties
- for logging reasons it's better to raise an HTTPException than using JSONResponse so errors can be logged on the server succesfully intead of just returning a response that is just different but worked.