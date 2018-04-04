FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python3-pip curl

EXPOSE 80 80
RUN mkdir /opt/wikirestapi /opt/wikirestapi/db

COPY . /opt/wikirestapi

RUN python3 -m pip install -r /opt/wikirestapi/etc/requirements.txt
RUN chmod +x /opt/wikirestapi/bin/run.sh

CMD /opt/wikirestapi/bin/run.sh
