FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
