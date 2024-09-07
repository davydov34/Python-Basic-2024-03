FROM tiangolo/uwsgi-nginx-flask:python3.11

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./
RUN poetry install
COPY ./prestart.sh ./prestart.sh
COPY ./app/  ./
