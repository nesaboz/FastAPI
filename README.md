# APIs testing and monitoring

I made a simple FastAPI project to test local SQLAlchemy Database APIs using Locust library. Performance metrics are stored long-term via Prometheus time-series database and monitored via Grafana. The whole thing was very easy to write and set up in a few hours (with big thanks to Docker compose too for this), and the setup is ready for production too.

Screenshots of four webapps: FastAPI, Locust, Prometheus, and Grafana:

| ![Image 1](assets/fastapi.png) | ![Image 2](assets/locust.png) |
|-------------------------------|-------------------------------|
| ![Image 3](assets/prometheus.png) | ![Image 4](assets/grafana.png) |


## Description 

Let me first describe the tools I used:  
- **[FastAPI](https://fastapi.tiangolo.com)** is a modern, fast (high-performance), web framework for building APIs based on standard Python type hints. It's built on top of standard Python libraries and tools, including Starlette for the web parts and Pydantic for the data parts.    
- **[Locust](https://locust.io)** is a performance/load testing tool for HTTP and other protocols. Great UI, all tests in Python.  
- **[Prometheus](https://prometheus.io)** is a monitoring system with a focus on reliability, designed for capturing time-series data like metrics. It supports queries, visualization, precise alerting, service discovery, and external storage integrations.   
- **[Grafana](https://grafana.com)** is an analytics and interactive visualization web application that provides charts, graphs, and alerts for the web when connected to supported data sources, like Prometheus. It's widely used for monitoring metrics and data visualization across various environments, including cloud infrastructure and applications.  
- **[Locust metrics exporter](https://github.com/ContainerSolutions/locust_exporter)** does exactly that: it preps locust metrics to be ingested by Prometheus.

## Run the FastAPI app

Prerequisites for those with no Docker installed:
```bash
pip install -r requirements.txt
```

Start ASGI server:
```bash
fastapi run main.py  # this runs: `uvicorn main:app --reload`
fastapi dev main.py  # to run in dev mode
```

Once your server is running, you can access the Swagger UI by navigating to:
```url
localhost:8000  # eq. http://127.0.0.1:8000
```
in your web browser.

![fastapi](assets/fastapi.png)


## Run load testing using Locust

```python
locust --host http://localhost:8000
```
Use flag  `--processes X` to define how many CPUs to run on, or `-1` for all.

Then check:
```url
http://localhost:8089
```

![locust](assets/locust.png)

## Long-term tracking with Prometheus and Grafana*

While Locust has it's own tracking, all data is lost once the locust server stops (data can be manually exported). In order to preserve any metrics long-term we:
- add Locust-metics-exporter
- add Prometheus as a time-series DB
- add Grafana for visualization
- scale using docker-compose

Docker-compose makes running several services straightforward (no Dockerfile needed):
```bash
docker-compose up
```

Notable points in `compose.yml`:
- mount volumes instead of copying as any changes to local files will be reflected in the container immediately:
```
 volumes:
      - .:/app
```
- each container is accessible to other containers within the same Docker Compose network using the service names as hostnames, for example:
`LOCUST_HOST=http://fastapi:8000`, where fastapi is the name of the service that runs FastAPI.
- to control how many CPUs you want to use for locust testing use `--processes X` (X=-1 means use all).
- `ro` stands for read-only
- use `volume` to persist all the data even if the container is stopped, see all volumes with `docker volume ls`

Prometheus and Grafana will then store data as long as it's needed, their UIs are excellent to set up all sorts of alerts and tracking.

```url
http://localhost:9090
```

![prometheus](assets/prometheus.png)

```url
http://localhost:3000
```
![grafana](assets/grafana.png)

*Inspired by Yusuf Tayman's [blog](https://medium.com/devopsturkiye/locust-real-time-monitoring-with-grafana-66654bb4b32).

## Conclusion

I wrote and ran simple FastAPI app with database (SQLAlchemy), stress test APIs (Locust) and monitor performance (Prometheus/Grafana), all containerized using docker-compose. While all WebApps ran on a local machine, scaling by splitting into microservices, or moving to the cloud host, would be straightforward (hosting can be done on EC2s with relevant ports exposed).
