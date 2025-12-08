FROM python:3.10-slim

WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 3000
CMD ["python", "flask_app.py"]
