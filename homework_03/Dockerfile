FROM python:3.9-buster

RUN apt update && apt upgrade -y

WORKDIR /app
RUN python -m pip install --upgrade pip

COPY  pyproject.toml poetry.lock /app/
COPY *.py /app/
COPY ./view/* /app/view/

RUN python -m pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]