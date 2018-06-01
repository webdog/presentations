# Developed on python 3.6.5
FROM python:3.6.5

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV FLASK_APP presentations.py
#ENV FLASK_DEBUG 1

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

