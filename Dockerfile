FROM python:3-alpine
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip install flask
CMD ["python", "/app/Utils/MainScores.py"]


