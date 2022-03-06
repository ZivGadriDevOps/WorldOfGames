FROM python:3-alpine
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip install flask
RUN mkdir /Resources
CMD ["python", "Utils/MainScores.py"]


