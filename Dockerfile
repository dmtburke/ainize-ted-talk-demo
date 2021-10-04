FROM python:latest

WORKDIR /app

RUN pip install streamlit requests

COPY . .

CMD ["streamlit", "run", "app.py"]
