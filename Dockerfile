FROM python:3-alpine
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip install flask
CMD ["python", "Utils/MainScores.py"]


