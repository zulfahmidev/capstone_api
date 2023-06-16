FROM python:3.10-alpine

WORKDIR /capstone

COPY . .

RUN git submodule update --init --recursive

RUN apk add --no-cache mariadb-dev build-base \
    && apk add --no-cache mariadb-connector-c

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG ENV_FILE
ARG CREDENTIAL_FILE

ENV e_file=${ENV_FILE}
ENV credential_file=${CREDENTIAL_FILE}

COPY ${e_file} /capstone/.env
COPY ${credential_file} /capstone/credentials.json

EXPOSE 80

CMD ["python", "app.py"]
