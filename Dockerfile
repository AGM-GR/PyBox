FROM python:3.9-slim-buster

RUN pip3 install Flask

COPY app.py app.py


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
