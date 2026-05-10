
FROM python:3.9.13


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["uvicorn", "routers.orders:router", "--host", "0.0.0.0", "--port", "8080"]
