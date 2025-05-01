FROM python:3.7

ADD . /webapp/
WORKDIR /webapp

RUN chmod -R 777 /webapp/utils
RUN /webapp/utils/setup.sh
CMD /webapp/utils/start.sh
