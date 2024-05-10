# FastAPI
VEry simple FastAPI project that communicates with a local SQL database.


To run your FastAPI app, you typically need to start your server via Uvicorn, an ASGI server.

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It's designed to be easy to use and learn, and it's built on top of standard Python libraries and tools, including Starlette for the web parts and Pydantic for the data parts.

ASGI (Asynchronous Server Gateway Interface) is a specification for Python web servers and applications that supports asynchronous programming. It's designed as an extension of WSGI (Web Server Gateway Interface), which is synchronous and can handle only one request at a time per process. 

Starlette as a lightweight ASGI framework/toolkit for building async web services in Python. It efficiently handles multiple simultaneous connections, making it suitable for modern web applications that require real-time capabilities, such as handling websockets, long polling, and other asynchronous features. 


## Run the app

Install the required packages:
```bash
pip install fastapi uvicorn SQLAlchemy
```

Start ASGI server:
```bash
uvicorn main:app --reload
```

Once your server is running, you can access the Swagger UI by navigating to:
```url
localhost:8000/docs   # eq. http://127.0.0.1:8000/docs
```
in your web browser. This `/docs` route is provided by FastAPI automatically and doesn't refer to a physical directory in your project; it's a virtual endpoint that FastAPI provides when the server is running.

