FROM python:3.9.20-slim

WORKDIR /app

# Sao chép toàn bộ mã nguồn vào thư mục làm việc
COPY . . 

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Mở cổng 8000
EXPOSE 8000 

# Chạy ứng dụng
CMD ["python", "main.py"]
