FROM taichi0315/pyenv-ubuntu:latest
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD Pipfile /code
RUN pipenv install
ADD . /code

WORKDIR /code/src
RUN pipenv run python manage.py makemigrations
RUN pipenv run python manage.py migrate
CMD ["pipenv","run","python","manage.py","runserver","0.0.0.0:8080"]
