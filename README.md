# APIs

I made a simple FastAPI project to test local SQLAlchemy database APIs using Locust. Performance metrics are stored long-term via Prometheus time-series database and monitored via Grafana. The whole thing was shockingly easy to write and set up (partially thanks to Docker too), kudos to smart engineers everywhere for making solutions like these work seamlessly. 

Screenshots of four webapps running: FastAPI, Locust, Prometheus, and Grafana.

| ![Image 1](assets/fastapi.png) | ![Image 2](assets/locust.png) |
|-------------------------------|-------------------------------|
| ![Image 3](assets/prometheus.png) | ![Image 4](assets/grafana.png) |

<!-- 
![fastapi](assets/fastapi.png)
![locust](assets/locust.png)
![prometheus](assets/prometheus.png)
![grafana](assets/grafana.png) -->


# Glossary

- **[FastAPI](https://fastapi.tiangolo.com)** is a modern, fast (high-performance), **web framework for building APIs** based on standard Python type hints. It's designed to be easy to use and learn, and it's built on top of standard Python libraries and tools, including Starlette for the web parts and Pydantic for the data parts.
- **[Locust](https://locust.io)** is an performance/load testing tool for HTTP and other protocols. Its developer friendly approach lets you define your tests in regular Python code.
- **[Prometheus](https://prometheus.io)** is a monitoring system with a focus on reliability, designed for capturing time-series data like metrics. It supports powerful queries, visualization, precise alerting, and has a strong ecosystem for service discovery and external storage integrations.
- **[Grafana](https://grafana.com)** is an analytics and interactive visualization web application that provides charts, graphs, and alerts for the web when connected to supported data sources, like Prometheus. It's widely used for monitoring metrics and data visualization across various environments, including cloud infrastructure and applications.


## Description 

We first start with local installation and later we'll containerize:
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

## Scaling with Prometheus and Grafana 

Inspired by (Yusuf Tayman's blog)[https://medium.com/devopsturkiye/locust-real-time-monitoring-with-grafana-66654bb4b32].

In order to preserve any metrics long term we:
- add Prometheus as a time-series DB
- Grafana for visualization
- scale using docker-compose

Take home lesson is how simple integration was.