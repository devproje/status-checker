from flask import Flask, jsonify
from flask_cors import CORS
from util import resource

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    health_check = {
        "status": 200,
        "ok": 1
    }

    return jsonify(health_check)

@app.route("/info", methods=["GET"])
def info():
    cpu = resource.get_cpu()
    mem = resource.get_memory()
    data = {
        "status": 200,
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
