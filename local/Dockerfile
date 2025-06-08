FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt && playwright install && playwright install-deps
COPY docker_test.py /app/docker_test.py
CMD ["python", "docker_test.py"]
