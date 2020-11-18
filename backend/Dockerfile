FROM python:3.8

RUN mkdir -p /mscs621-concordance
WORKDIR /mscs621-concordance

COPY requirements.txt /mscs621-concordance/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /mscs621-concordance


EXPOSE 8080

CMD ["uwsgi", "/mscs621-concordance/uwsgi.ini"]