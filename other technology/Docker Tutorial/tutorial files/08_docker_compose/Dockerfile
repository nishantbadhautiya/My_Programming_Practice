FROM python:latest

WORKDIR /myapp 

COPY ./sql_demo.py . 

RUN pip install pymysql

RUN pip install cryptography

CMD [ "python3", "sql_demo.py"] 