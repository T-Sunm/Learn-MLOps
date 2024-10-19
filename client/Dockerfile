FROM python:3.9.20-slim

WORKDIR /app

# Sao chép toàn bộ mã nguồn vào thư mục làm việc
COPY . . 

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Mở cổng 3000
EXPOSE 3000 

# Chạy ứng dụng
CMD ["python", "app.py"]
