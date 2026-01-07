FROM python:3.13.5
ADD main.py .
RUN pip install gpiozero
CMD ["python", "./main.py"]


