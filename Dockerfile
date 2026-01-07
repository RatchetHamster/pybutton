FROM python:3.13.5
ADD main.py .
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]

