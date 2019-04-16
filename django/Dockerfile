FROM python:3
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
VOLUME /usr/src/media
VOLUME /usr/src/static
WORKDIR /usr/src/app

COPY requirements.txt /usr/src
RUN pip install --no-cache-dir --requirement /usr/src/requirements.txt
COPY ./app /usr/src/app

CMD python3 manage.py migrate && \
	python3 manage.py collectstatic --no-input && \
	[ "$DEBUG" = "1" ] && \
		python3 manage.py runserver 0.0.0.0:8000 || \
		gunicorn --config gunicorn.py app.aio:aioapp