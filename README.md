# FastAPI Learning Repository

---
## What is FastAPI?
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python (3.7+). It is built on top of **Starlette** (for web parts) and **Pydantic** (for data validation).

It is widely used for:
* Building RESTful APIs
* Backend services for web/mobile apps
* Machine learning model serving
* Microservices

---

## How FastAPI Works (General Workflow)

1. **Define Routes**
   * We define endpoints using decorators like `@app.get()`, `@app.post()`.

2. **Request Handling**
   * FastAPI automatically parses incoming requests (JSON, query params, etc.)

3. **Data Validation**
   * Uses Pydantic models to validate request data.

4. **Processing**
   * The app logic runs inside the route function.

5. **Response**
   * Returns JSON responses automatically.

6. **Auto Documentation**
   * Interactive docs are generated at:

     * `/docs` (Swagger UI)
     * `/redoc`

---

## Uvicorn
Uvicorn is a lightning-fast **ASGI (Asynchronous Server Gateway Interface) server** used to run FastAPI applications.

* It acts as the **server that executes the FastAPI app**
* Supports **asynchronous communication**
* Built on `uvloop` and `httptools` for performance

### Example command:

```bash
uvicorn main:app --reload
```

---

## Asynchronous API
An **asynchronous API** allows handling multiple requests simultaneously **without blocking execution** (next client request is not blocked while previous request is being processed).

### Key Idea:
* Traditional (synchronous): One request at a time
* Asynchronous: Multiple requests handled concurrently

### In FastAPI:

```python
@app.get("/")
async def read_root():
    return {"message": "Hello World"}
```

### Benefits:

* Better performance under load
* Efficient I/O operations (DB calls, APIs)
* Non-blocking execution

---

## Key Features of FastAPI
1. Extremely fast (comparable to Node.js & Go)
2. Automatic data validation with Pydantic
3. Auto-generated API docs (Swagger & ReDoc)
4. Built-in support for authentication & security
5. Async support by default


---

## FastAPI vs Flask vs Django

### FastAPI vs Flask

| Feature         | FastAPI   | Flask    |
| --------------- | --------- | -------- |
| Performance     | Very High | Moderate |
| Async Support   | Native    | Limited  |
| Data Validation | Built-in  | Manual   |
| Documentation   | Automatic | Manual   |
| Learning Curve  | Moderate  | Easy     |

Flask is lightweight but requires more manual setup.

---

### FastAPI vs Django

| Feature       | FastAPI              | Django               |
| ------------- | -------------------- | -------------------- |
| Type          | API-first            | Full-stack framework |
| Performance   | High                 | Moderate             |
| Async Support | Strong               | Partial              |
| Flexibility   | High                 | Opinionated          |
| Use Case      | APIs & microservices | Large web apps       |

Django is powerful for full applications but heavier compared to FastAPI.


## Learning Goals

* Understand REST API concepts
* Learn async programming in Python
* Build scalable backend services
* Work with databases and authentication

