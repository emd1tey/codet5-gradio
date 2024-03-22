FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir transformers torch gradio

EXPOSE 7861

CMD ["python", "app.py"]
