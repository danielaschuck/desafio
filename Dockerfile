FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY extract_and_load.py /app/

CMD ["python", "extract_and_load.py"]
