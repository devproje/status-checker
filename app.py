from flask import Flask, jsonify
from util import resource
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/info")
def info():
    cpu = resource.get_cpu()
    mem = resource.get_memory()
    data = {
        "cpu": {
            "freq": {
                "current": round(cpu.freq.current / 1000, 1),
                "min": round(cpu.freq.min / 1000, 1),
                "max": round(cpu.freq.max / 1000, 1)
            },
            "usage": round(cpu.percent),
        },
        "memory": {
            "used": mem.used >> 30,
            "total": mem.total >> 30,
            "usage": round(mem.percent)
        }
    }
    
    return jsonify(data)
