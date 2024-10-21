FROM python:3.9.20-slim

WORKDIR /app

# layer cache thay vì cache hết
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
# Mở cổng 3000
EXPOSE 3000 

# Chạy ứng dụng
CMD ["python", "app.py"]
