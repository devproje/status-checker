import time
import psutil

class CPU:
    def __init__(self, percent, freq):
        self.percent = percent
        self.freq = freq

def get_cpu():
    return CPU(psutil.cpu_percent(), psutil.cpu_freq())

def get_memory():
    return psutil.virtual_memory()

def get_uptime():
    return time.time() - psutil.boot_time()
