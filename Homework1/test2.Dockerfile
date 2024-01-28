FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY zones.py zones.py

ENTRYPOINT [ "python", "zones.py" ]