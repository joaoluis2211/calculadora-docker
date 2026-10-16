FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends iputils-ping \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app.py test_app.py ./

EXPOSE 5000

CMD ["python", "app.py"]