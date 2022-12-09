FROM python:3.6

ADD . /opt/webapp/
WORKDIR /opt/webapp

# WORKDIR .
# COPY . .
RUN chmod -R 777 /opt/webapp/utils
RUN /opt/webapp/utils/remove_files.sh
RUN /opt/webapp/utils/setup.sh
CMD /opt/webapp/utils/start.sh
