FROM python:3
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install requests
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py makemigrations
CMD python manage.py runserver 0.0.0.0:8000