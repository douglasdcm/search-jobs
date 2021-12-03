FROM python:3.9.7-bullseye

WORKDIR .
COPY . .
RUN chmod -R 777 /utils
RUN ./utils/remove_files.sh
RUN ./utils/setup.sh
CMD ./utils/start.sh
