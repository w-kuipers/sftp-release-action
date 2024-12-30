FROM python:3.9-slim

COPY src /src
COPY main.py /main.py
COPY requirements.txt /requirements.txt
COPY entrypoint.sh /entrypoint.sh

RUN pip install -r /requirements.txt

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
