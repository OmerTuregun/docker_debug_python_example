import psutil
import time

def get_cpu_and_ram_usage():
    # CPU yüzdesi (tüm çekirdeklerin ortalaması)
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # RAM kullanımı
    ram_info = psutil.virtual_memory()
    total_ram = ram_info.total / (1024 * 1024)  # Toplam RAM (MB)
    used_ram = ram_info.used / (1024 * 1024)    # Kullanılan RAM (MB)
    ram_usage_percent = ram_info.percent        # RAM kullanımı yüzdesi

    return cpu_usage, total_ram, used_ram, ram_usage_percent

def monitor_system():
    while True:
        cpu, total_ram, used_ram, ram_percent = get_cpu_and_ram_usage()
        print(f"CPU Usage: {cpu}%")
        print(f"Total RAM: {total_ram:.2f} MB")
        print(f"Used RAM: {used_ram:.2f} MB ({ram_percent}%)")
        print("-" * 30)
        time.sleep(5)  # 5 saniyede bir verileri güncelle

if __name__ == "__main__":
    monitor_system()
