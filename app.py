import requests
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Разрешаем запросы с любых сайтов (для твоего PWA)
CORS(app, resources={r"/*": {"origins": "*"}})

# URL с данными серверов
API_URL = "https://api.blackrussia.online/servers.json"

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "message": "BLACK RUSSIA Monitor API работает!",
        "endpoints": {
            "servers": "/api/servers"
        }
    })

@app.route('/api/servers')
def get_servers():
    try:
        # Получаем данные с официального API
        response = requests.get(API_URL, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": f"Ошибка API: {response.status_code}"}), 500
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
