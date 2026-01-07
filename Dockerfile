FROM python:3.13
ADD main.py .
RUN pip install RPi.GPIO
CMD ["python", "./main.py"]
