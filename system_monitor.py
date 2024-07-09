import os
import sys
import tkinter as tk
from tkinter import ttk
import psutil
import GPUtil
import time
from PIL import Image, ImageTk
from ttkthemes import ThemedTk


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


VERSION = "1.0.1"
DEVELOPER = "Matrex"


class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")

        # Use a modern theme
        self.style = ttk.Style(self.root)
        self.root.set_theme("breeze")  # You can try other themes like 'arc', 'equilux', etc.

        # Load icons
        self.cpu_icon = ImageTk.PhotoImage(Image.open(resource_path("icons/cpu.png")).resize((24, 24)))
        self.gpu_icon = ImageTk.PhotoImage(Image.open(resource_path("icons/gpu.png")).resize((24, 24)))
        self.ram_icon = ImageTk.PhotoImage(Image.open(resource_path("icons/ram.png")).resize((24, 24)))
        self.disk_icon = ImageTk.PhotoImage(Image.open(resource_path("icons/disk.png")).resize((24, 24)))
        self.network_icon = ImageTk.PhotoImage(Image.open(resource_path("icons/network.png")).resize((24, 24)))

        self.create_widgets()

    def create_widgets(self):
        # CPU Info Section
        self.cpu_frame = ttk.LabelFrame(self.root, text="CPU Info")
        self.cpu_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.cpu_icon_label = ttk.Label(self.cpu_frame, image=self.cpu_icon)
        self.cpu_icon_label.pack(side="left", padx=5)

        self.cpu_info = tk.StringVar()
        self.cpu_info_label = ttk.Label(self.cpu_frame, textvariable=self.cpu_info)
        self.cpu_info_label.pack(side="left")

        # GPU Info Section
        self.gpu_frame = ttk.LabelFrame(self.root, text="GPU Info")
        self.gpu_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.gpu_icon_label = ttk.Label(self.gpu_frame, image=self.gpu_icon)
        self.gpu_icon_label.pack(side="left", padx=5)

        self.gpu_info = tk.StringVar()
        self.gpu_info_label = ttk.Label(self.gpu_frame, textvariable=self.gpu_info)
        self.gpu_info_label.pack(side="left")

        # RAM Info Section
        self.ram_frame = ttk.LabelFrame(self.root, text="RAM Info")
        self.ram_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.ram_icon_label = ttk.Label(self.ram_frame, image=self.ram_icon)
        self.ram_icon_label.pack(side="left", padx=5)

        self.ram_info = tk.StringVar()
        self.ram_info_label = ttk.Label(self.ram_frame, textvariable=self.ram_info)
        self.ram_info_label.pack(side="left")

        # Disk Info Section
        self.disk_frame = ttk.LabelFrame(self.root, text="Disk Info")
        self.disk_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.disk_icon_label = ttk.Label(self.disk_frame, image=self.disk_icon)
        self.disk_icon_label.pack(side="left", padx=5)

        self.disk_info = tk.StringVar()
        self.disk_info_label = ttk.Label(self.disk_frame, textvariable=self.disk_info)
        self.disk_info_label.pack(side="left")

        # Network Info Section
        self.network_frame = ttk.LabelFrame(self.root, text="Network Info")
        self.network_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.network_icon_label = ttk.Label(self.network_frame, image=self.network_icon)
        self.network_icon_label.pack(side="left", padx=5)

        self.network_info = tk.StringVar()
        self.network_info_label = ttk.Label(self.network_frame, textvariable=self.network_info)
        self.network_info_label.pack(side="left")

        # Version and Developer Info
        self.footer_frame = ttk.Frame(self.root)
        self.footer_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.version_label = ttk.Label(self.footer_frame, text=f"Version: {VERSION}")
        self.version_label.pack(side="left", padx=5)

        self.developer_label = ttk.Label(self.footer_frame, text=f"Developer: {DEVELOPER}")
        self.developer_label.pack(side="left", padx=5)

        self.update_info()

    def get_cpu_info(self):
        cpu_info = f"CPU Usage: {psutil.cpu_percent(interval=1)}%\n" \
                   f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz\n" \
                   f"CPU Cores: {psutil.cpu_count(logical=False)}\n" \
                   f"Logical CPUs: {psutil.cpu_count(logical=True)}"
        return cpu_info

    def get_gpu_info(self):
        gpus = GPUtil.getGPUs()
        gpu_info = ""
        for gpu in gpus:
            gpu_info += f"GPU: {gpu.name}\n" \
                        f"Load: {gpu.load * 100:.2f}%\n" \
                        f"Memory Free: {gpu.memoryFree} MB\n" \
                        f"Memory Used: {gpu.memoryUsed} MB\n" \
                        f"Temperature: {gpu.temperature}°C\n"
        return gpu_info

    def get_ram_info(self):
        ram = psutil.virtual_memory()
        ram_info = f"Total: {ram.total / (1024 ** 3):.2f} GB\n" \
                   f"Available: {ram.available / (1024 ** 3):.2f} GB\n" \
                   f"Used: {ram.used / (1024 ** 3):.2f} GB ({ram.percent}%)\n" \
                   f"Free: {ram.free / (1024 ** 3):.2f} GB"
        return ram_info

    def get_disk_info(self):
        disk = psutil.disk_usage('/')
        disk_info = f"Total: {disk.total / (1024 ** 3):.2f} GB\n" \
                    f"Used: {disk.used / (1024 ** 3):.2f} GB ({disk.percent}%)\n" \
                    f"Free: {disk.free / (1024 ** 3):.2f} GB"
        return disk_info

    def get_network_info(self):
        net_io = psutil.net_io_counters()
        network_info = f"Bytes Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB\n" \
                       f"Bytes Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB\n" \
                       f"Packets Sent: {net_io.packets_sent}\n" \
                       f"Packets Received: {net_io.packets_recv}"
        return network_info

    def update_info(self):
        self.cpu_info.set(self.get_cpu_info())
        self.gpu_info.set(self.get_gpu_info())
        self.ram_info.set(self.get_ram_info())
        self.disk_info.set(self.get_disk_info())
        self.network_info.set(self.get_network_info())
        self.root.after(5000, self.update_info)  # Update every 5 seconds


if __name__ == '__main__':
    root = ThemedTk(theme="arc")
    app = SystemMonitorApp(root)
    root.mainloop()
