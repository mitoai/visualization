FROM python:3.6

RUN mkdir /mito

WORKDIR /mito

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

ENTRYPOINT ["python", "utils.py"]