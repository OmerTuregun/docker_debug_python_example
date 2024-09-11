# Temel Python imajını kullan
FROM python:3.9-slim

# Psutil kütüphanesini yükle
RUN pip install psutil

# Çalışma dizini oluştur ve uygulama dosyasını kopyala
WORKDIR /app
COPY cpu_ram_monitor.py .

# Debug için debugpy yükle
RUN pip install debugpy

# Debug portunu aç ve uygulamayı çalıştır
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "cpu_ram_monitor.py"]
