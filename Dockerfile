FROM python:3.9-slim

COPY src /src

# RUN pip install --no-cache-dir -r /requirements.txt || true

ENTRYPOINT ["python", "/src/package.py"]
