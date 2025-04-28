FROM python:3.9-slim

RUN pip install Flask==2.0.3 PyYAML==5.4

COPY vulnerable_server.py /vulnerable_server.py

CMD ["python", "/vulnerable_server.py"]
