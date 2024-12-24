FROM python:3.9-slim

COPY src /src
COPY main.py /main.py
COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

# Install Node.js v22 and npm
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python", "/main.py"]
CMD []
