# FastAPI
Very simple FastAPI project that communicates with a local SQL database. We'll go over:
- **FastAPI** is a modern, fast (high-performance), **web framework for building APIs** based on standard Python type hints. It's designed to be easy to use and learn, and it's built on top of standard Python libraries and tools, including Starlette for the web parts and Pydantic for the data parts.
- **Starlette** is a lightweight Asynchronous Server Gateway Interface (ASGI) **framework/toolkit** for building async web services in Python. It efficiently handles multiple simultaneous connections, making it suitable for modern web applications that require real-time capabilities, such as handling websockets, long polling, and other asynchronous features.
- **Uvicorn** is used to run FastAPI as an ASGI **web server**. Btw Web Server Gateway Interface (WSGI) server, which is synchronous, can handle only one request at a time per process. 
- **Locust** Locust is an performance/load testing tool for HTTP and other protocols. Its developer friendly approach lets you define your tests in regular Python code.

## Description 

We have created bunch of SQLAlchemy database APIs we would like to test. Prerequisites:
```bash
pip install -r requirements.txt
```

## Run the app

Start ASGI server:
```bash
fastapi run
```

Once your server is running, you can access the Swagger UI by navigating to:
```url
localhost:8000/docs   # eq. http://127.0.0.1:8000/docs
```
in your web browser. This `/docs` route is provided by FastAPI automatically and doesn't refer to a physical directory in your project; it's a virtual endpoint that FastAPI provides when the server is running.

# Run load testing using locust

```python
locust --host http://localhost:8000
# or to define how many CPUs to run on:
locust --processes 8
```

```url
http://localhost:8089
```

## Add Prometheus and Grafana (link)[https://medium.com/devopsturkiye/locust-real-time-monitoring-with-grafana-66654bb4b32].

Since the number of services/libraries is getting quite big now we'll switch to docker-compose to manage these. We'll now add Prometheus (time-series DB) and Grafana (visualization) services.


