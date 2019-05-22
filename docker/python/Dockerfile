FROM python:3.7
ADD . /code
WORKDIR /code
RUN pip install pipenv
RUN pipenv install --system --dev
CMD pipenv run start

