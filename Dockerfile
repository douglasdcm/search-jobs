FROM python:3.9.7-bullseye

WORKDIR .
COPY . .
RUN ./setup.sh
CMD ./start.sh
