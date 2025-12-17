FROM ubuntu:latest

RUN apt update
RUN apt install -y socat

COPY entry.sh /
RUN chmod +x entry.sh

COPY stack /
RUN chmod +x stack

ENTRYPOINT [ "/entry.sh" ]