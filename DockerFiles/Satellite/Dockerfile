FROM ubuntu:latest
RUN apt update -y

RUN apt install -y git \
		python3 \
		pip \
		iproute2 \
		nano

RUN mkdir satellite
RUN git clone https://gitlab.com/librecube/lib/python-cfdp.git /satellite/
RUN cd satellite
RUN pip install cfdp

