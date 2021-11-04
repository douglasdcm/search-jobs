FROM python:3.9.7-bullseye
WORKDIR .
ENV HASH=dev
COPY ./requirements.txt .
COPY ./utils ./utils
COPY ./src/resources ./src/resources
RUN ./utils/setup.sh
COPY . .
CMD ./utils/start.sh
