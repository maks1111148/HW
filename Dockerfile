# Version: 0.0.6
FROM python:3
MAINTAINER Maksym Kharchenko <1makskharchenko1@gmail.com>
RUN pip install psutil
ADD hardware_monitor.py /
ENTRYPOINT ["python3", "hardware_monitor.py"]
