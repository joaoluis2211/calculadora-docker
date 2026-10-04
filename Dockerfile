FROM python:3.12-slim

WORKDIR /app

COPY app.py test_app.py ./

EXPOSE 5000

CMD ["python", "app.py"]