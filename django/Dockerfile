FROM python:3
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
VOLUME /static
VOLUME /media
WORKDIR /code/app

COPY requirements.txt /code
RUN pip install --no-cache-dir --requirement /code/requirements.txt
COPY ./app /code/app

CMD python manage.py collectstatic --no-input && \
	python manage.py migrate && \
	gunicorn --config gunicorn.py app.wsgi:aioapp
