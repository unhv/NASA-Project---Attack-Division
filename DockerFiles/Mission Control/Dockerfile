FROM ubuntu:latest
RUN apt update -y

RUN apt install -y git \
		python3 \
		pip \
		iproute2 \
		nano

RUN mkdir mission_control
RUN git clone https://gitlab.com/librecube/lib/python-cfdp.git /mission_control/ 
RUN cd mission_control
RUN pip install cfdp
CMD ["python3", "/mission_control/examples/udp_transport/server.py"]

