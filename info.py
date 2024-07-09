import psutil
import GPUtil
import time
import json

def get_cpu_info():
    cpu_info = {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'cpu_freq': psutil.cpu_freq()._asdict(),
        'cpu_count': psutil.cpu_count(logical=False),
        'cpu_count_logical': psutil.cpu_count(logical=True)
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            'id': gpu.id,
            'name': gpu.name,
            'load': gpu.load,
            'memoryTotal': gpu.memoryTotal,
            'memoryFree': gpu.memoryFree,
            'memoryUsed': gpu.memoryUsed,
            'temperature': gpu.temperature,
            'uuid': gpu.uuid
        })
    return gpu_info

def get_ram_info():
    ram = psutil.virtual_memory()
    ram_info = {
        'total': ram.total,
        'available': ram.available,
        'percent': ram.percent,
        'used': ram.used,
        'free': ram.free
    }
    return ram_info

def get_disk_info():
    disk = psutil.disk_usage('/')
    disk_info = {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent
    }
    return disk_info

def get_network_info():
    net_io = psutil.net_io_counters()
    network_info = {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }
    return network_info

def log_info(filename='system_info.json'):
    while True:
        info = {
            'cpu': get_cpu_info(),
            'gpu': get_gpu_info(),
            'ram': get_ram_info(),
            'disk': get_disk_info(),
            'network': get_network_info(),
            'timestamp': time.time()
        }
        with open(filename, 'a') as f:
            json.dump(info, f)
            f.write('\n')
        time.sleep(5)  # Log every 5 seconds

if __name__ == '__main__':
    log_info()
