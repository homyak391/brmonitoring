import os
import socket
import struct
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ВСЕ 89 СЕРВЕРОВ BLACK RUSSIA (полный список)
SERVERS = [
    {"ip": "80.66.82.46", "port": 5125, "name": "BLACK RUSSIA | RED", "color": "FF0000", "online": "464", "maxonline": "1300"},
    {"ip": "80.66.82.47", "port": 5125, "name": "BLACK RUSSIA | GREEN", "color": "00FF00", "online": "255", "maxonline": "1300"},
    {"ip": "80.66.82.197", "port": 5125, "name": "BLACK RUSSIA | BLUE", "color": "2D57EC", "online": "278", "maxonline": "1300"},
    {"ip": "80.66.82.198", "port": 5125, "name": "BLACK RUSSIA | YELLOW", "color": "FFFF00", "online": "213", "maxonline": "1300"},
    {"ip": "80.66.82.210", "port": 5125, "name": "BLACK RUSSIA | ORANGE", "color": "FFA500", "online": "230", "maxonline": "1300"},
    {"ip": "80.66.82.211", "port": 5125, "name": "BLACK RUSSIA | PURPLE", "color": "800080", "online": "283", "maxonline": "1300"},
    {"ip": "80.66.82.208", "port": 5125, "name": "BLACK RUSSIA | LIME", "color": "CCFF00", "online": "183", "maxonline": "1300"},
    {"ip": "80.66.82.209", "port": 5125, "name": "BLACK RUSSIA | PINK", "color": "FF69B4", "online": "195", "maxonline": "1300"},
    {"ip": "80.66.82.236", "port": 5125, "name": "BLACK RUSSIA | CHERRY", "color": "790604", "online": "196", "maxonline": "1300"},
    {"ip": "80.66.82.237", "port": 5125, "name": "BLACK RUSSIA | BLACK", "color": "33393D", "online": "277", "maxonline": "1300"},
    {"ip": "80.66.82.233", "port": 5125, "name": "BLACK RUSSIA | INDIGO", "color": "4B0082", "online": "188", "maxonline": "1300"},
    {"ip": "80.66.82.234", "port": 5125, "name": "BLACK RUSSIA | WHITE", "color": "FFFFFF", "online": "234", "maxonline": "1300"},
    {"ip": "80.66.82.253", "port": 5125, "name": "BLACK RUSSIA | MAGENTA", "color": "C406C4", "online": "189", "maxonline": "1300"},
    {"ip": "80.66.82.254", "port": 5125, "name": "BLACK RUSSIA | CRIMSON", "color": "D9133B", "online": "274", "maxonline": "1300"},
    {"ip": "80.66.82.180", "port": 5125, "name": "BLACK RUSSIA | GOLD", "color": "F1B61F", "online": "251", "maxonline": "1300"},
    {"ip": "80.66.82.181", "port": 5125, "name": "BLACK RUSSIA | AZURE", "color": "3097FF", "online": "174", "maxonline": "1300"},
    {"ip": "80.66.82.175", "port": 5125, "name": "BLACK RUSSIA | PLATINUM", "color": "868480", "online": "176", "maxonline": "1300"},
    {"ip": "80.66.82.176", "port": 5125, "name": "BLACK RUSSIA | AQUA", "color": "0DEDED", "online": "191", "maxonline": "1300"},
    {"ip": "80.66.82.171", "port": 5125, "name": "BLACK RUSSIA | GRAY", "color": "C7C2C1", "online": "194", "maxonline": "1300"},
    {"ip": "80.66.82.170", "port": 5125, "name": "BLACK RUSSIA | ICE", "color": "B6F1FE", "online": "205", "maxonline": "1300"},
    {"ip": "80.66.82.166", "port": 5125, "name": "BLACK RUSSIA | CHILLI", "color": "FE2726", "online": "211", "maxonline": "1300"},
    {"ip": "80.66.82.167", "port": 5125, "name": "BLACK RUSSIA | CHOCO", "color": "BF835C", "online": "142", "maxonline": "1300"},
    {"ip": "80.66.82.157", "port": 5125, "name": "BLACK RUSSIA | MOSCOW", "color": "FF2B3B", "online": "421", "maxonline": "1300"},
    {"ip": "80.66.82.158", "port": 5125, "name": "BLACK RUSSIA | SPB", "color": "11A6FA", "online": "267", "maxonline": "1300"},
    {"ip": "80.66.82.151", "port": 5125, "name": "BLACK RUSSIA | UFA", "color": "FFBA08", "online": "226", "maxonline": "1300"},
    {"ip": "80.66.82.152", "port": 5125, "name": "BLACK RUSSIA | SOCHI", "color": "01AFD6", "online": "208", "maxonline": "1300"},
    {"ip": "80.66.82.145", "port": 5125, "name": "BLACK RUSSIA | KAZAN", "color": "007DB2", "online": "244", "maxonline": "1300"},
    {"ip": "80.66.82.146", "port": 5125, "name": "BLACK RUSSIA | SAMARA", "color": "82339D", "online": "230", "maxonline": "1300"},
    {"ip": "80.66.82.140", "port": 5125, "name": "BLACK RUSSIA | ROSTOV", "color": "FBB040", "online": "204", "maxonline": "1300"},
    {"ip": "80.66.82.141", "port": 5125, "name": "BLACK RUSSIA | ANAPA", "color": "24ACF8", "online": "208", "maxonline": "1300"},
    {"ip": "80.66.82.137", "port": 5125, "name": "BLACK RUSSIA | EKB", "color": "93F0A4", "online": "341", "maxonline": "1300"},
    {"ip": "80.66.82.138", "port": 5125, "name": "BLACK RUSSIA | KRASNODAR", "color": "A03429", "online": "266", "maxonline": "1300"},
    {"ip": "80.66.82.134", "port": 5125, "name": "BLACK RUSSIA | ARZAMAS", "color": "FFF72D", "online": "206", "maxonline": "1300"},
    {"ip": "80.66.82.135", "port": 5125, "name": "BLACK RUSSIA | NOVOSIB", "color": "99D53B", "online": "325", "maxonline": "1300"},
    {"ip": "80.66.82.130", "port": 5125, "name": "BLACK RUSSIA | GROZNY", "color": "009622", "online": "380", "maxonline": "1300"},
    {"ip": "80.66.82.131", "port": 5125, "name": "BLACK RUSSIA | SARATOV", "color": "0597EB", "online": "204", "maxonline": "1300"},
    {"ip": "80.66.82.125", "port": 5125, "name": "BLACK RUSSIA | OMSK", "color": "58E1A5", "online": "288", "maxonline": "1300"},
    {"ip": "80.66.82.126", "port": 5125, "name": "BLACK RUSSIA | IRKUTSK", "color": "06E1FF", "online": "392", "maxonline": "1300"},
    {"ip": "80.66.82.120", "port": 5125, "name": "BLACK RUSSIA | VOLGOGRAD", "color": "FE0000", "online": "244", "maxonline": "1300"},
    {"ip": "80.66.82.121", "port": 5125, "name": "BLACK RUSSIA | VORONEZH", "color": "FFF200", "online": "190", "maxonline": "1300"},
    {"ip": "80.66.82.114", "port": 5125, "name": "BLACK RUSSIA | BELGOROD", "color": "0039A6", "online": "158", "maxonline": "1300"},
    {"ip": "80.66.82.115", "port": 5125, "name": "BLACK RUSSIA | MAKHACHKALA", "color": "42AD42", "online": "500", "maxonline": "1300"},
    {"ip": "80.66.82.111", "port": 5125, "name": "BLACK RUSSIA | VLADIKAVKAZ", "color": "8EB0D9", "online": "155", "maxonline": "1300"},
    {"ip": "80.66.82.187", "port": 5125, "name": "BLACK RUSSIA | VLADIVOSTOK", "color": "3A95FF", "online": "341", "maxonline": "1300"},
    {"ip": "80.66.82.107", "port": 5125, "name": "BLACK RUSSIA | KALININGRAD", "color": "F0EBC9", "online": "172", "maxonline": "1300"},
    {"ip": "80.66.82.108", "port": 5125, "name": "BLACK RUSSIA | CHELYABINSK", "color": "FF6B00", "online": "211", "maxonline": "1300"},
    {"ip": "80.66.82.100", "port": 5125, "name": "BLACK RUSSIA | KRASNOYARSK", "color": "D99D1C", "online": "318", "maxonline": "1300"},
    {"ip": "80.66.82.101", "port": 5125, "name": "BLACK RUSSIA | CHEBOKSARY", "color": "6CBB74", "online": "153", "maxonline": "1300"},
    {"ip": "80.66.82.94", "port": 5125, "name": "BLACK RUSSIA | KHABAROVSK", "color": "0184C4", "online": "197", "maxonline": "1300"},
    {"ip": "80.66.82.95", "port": 5125, "name": "BLACK RUSSIA | PERM", "color": "FFD700", "online": "229", "maxonline": "1300"},
    {"ip": "80.66.82.92", "port": 5125, "name": "BLACK RUSSIA | TULA", "color": "F2B647", "online": "176", "maxonline": "1300"},
    {"ip": "80.66.82.93", "port": 5125, "name": "BLACK RUSSIA | RYAZAN", "color": "C659EB", "online": "151", "maxonline": "1300"},
    {"ip": "80.66.82.85", "port": 5125, "name": "BLACK RUSSIA | MURMANSK", "color": "396797", "online": "129", "maxonline": "1300"},
    {"ip": "80.66.82.86", "port": 5125, "name": "BLACK RUSSIA | PENZA", "color": "53E295", "online": "140", "maxonline": "1300"},
    {"ip": "80.66.82.83", "port": 5125, "name": "BLACK RUSSIA | KURSK", "color": "9E1C00", "online": "176", "maxonline": "1300"},
    {"ip": "80.66.82.84", "port": 5125, "name": "BLACK RUSSIA | ARKHANGELSK", "color": "FF007A", "online": "150", "maxonline": "1300"},
    {"ip": "80.66.82.76", "port": 5125, "name": "BLACK RUSSIA | ORENBURG", "color": "E39012", "online": "147", "maxonline": "1300"},
    {"ip": "80.66.82.77", "port": 5125, "name": "BLACK RUSSIA | KIROV", "color": "939393", "online": "145", "maxonline": "1300"},
    {"ip": "80.66.82.74", "port": 5125, "name": "BLACK RUSSIA | KEMEROVO", "color": "F61A1B", "online": "381", "maxonline": "1300"},
    {"ip": "80.66.82.75", "port": 5125, "name": "BLACK RUSSIA | TYUMEN", "color": "44C9F3", "online": "190", "maxonline": "1300"},
    {"ip": "80.66.82.72", "port": 5125, "name": "BLACK RUSSIA | TOLYATTI", "color": "8F00FF", "online": "129", "maxonline": "1300"},
    {"ip": "80.66.82.73", "port": 5125, "name": "BLACK RUSSIA | IVANOVO", "color": "D5AF80", "online": "148", "maxonline": "1300"},
    {"ip": "80.66.82.67", "port": 5125, "name": "BLACK RUSSIA | STAVROPOL", "color": "3F6BE9", "online": "160", "maxonline": "1300"},
    {"ip": "80.66.82.68", "port": 5125, "name": "BLACK RUSSIA | SMOLENSK", "color": "EE703E", "online": "161", "maxonline": "1300"},
    {"ip": "80.66.82.124", "port": 5125, "name": "BLACK RUSSIA | PSKOV", "color": "63A62E", "online": "143", "maxonline": "1300"},
    {"ip": "80.66.82.183", "port": 5125, "name": "BLACK RUSSIA | BRYANSK", "color": "26EEBE", "online": "168", "maxonline": "1300"},
    {"ip": "80.66.82.64", "port": 5125, "name": "BLACK RUSSIA | OREL", "color": "FFEA03", "online": "169", "maxonline": "1300"},
    {"ip": "80.66.82.65", "port": 5125, "name": "BLACK RUSSIA | YAROSLAVL", "color": "D01D0D", "online": "149", "maxonline": "1300"},
    {"ip": "80.66.82.56", "port": 5125, "name": "BLACK RUSSIA | BARNAUL", "color": "797CC7", "online": "204", "maxonline": "1300"},
    {"ip": "80.66.82.57", "port": 5125, "name": "BLACK RUSSIA | LIPETSK", "color": "CCD0DA", "online": "126", "maxonline": "1300"},
    {"ip": "80.66.82.52", "port": 5125, "name": "BLACK RUSSIA | ULYANOVSK", "color": "B55624", "online": "163", "maxonline": "1300"},
    {"ip": "80.66.82.53", "port": 5125, "name": "BLACK RUSSIA | YAKUTSK", "color": "44BFFC", "online": "301", "maxonline": "1300"},
    {"ip": "80.66.82.50", "port": 5125, "name": "BLACK RUSSIA | TAMBOV", "color": "959595", "online": "154", "maxonline": "1300"},
    {"ip": "80.66.82.51", "port": 5125, "name": "BLACK RUSSIA | BRATSK", "color": "E0C1A0", "online": "163", "maxonline": "1300"},
    {"ip": "80.66.82.42", "port": 5125, "name": "BLACK RUSSIA | ASTRAKHAN", "color": "F7243A", "online": "214", "maxonline": "1300"},
    {"ip": "80.66.82.43", "port": 5125, "name": "BLACK RUSSIA | CHITA", "color": "35CA68", "online": "315", "maxonline": "1300"},
    {"ip": "80.66.82.38", "port": 5125, "name": "BLACK RUSSIA | KOSTROMA", "color": "F1B10D", "online": "146", "maxonline": "1300"},
    {"ip": "80.66.82.36", "port": 5125, "name": "BLACK RUSSIA | VLADIMIR", "color": "F58041", "online": "161", "maxonline": "1300"},
    {"ip": "80.66.82.35", "port": 5125, "name": "BLACK RUSSIA | KALUGA", "color": "3032A4", "online": "153", "maxonline": "1300"},
    {"ip": "80.66.82.34", "port": 5125, "name": "BLACK RUSSIA | NOVGOROD", "color": "FFC700", "online": "125", "maxonline": "1300"},
    {"ip": "80.66.82.26", "port": 5125, "name": "BLACK RUSSIA | TAGANROG", "color": "984FCF", "online": "201", "maxonline": "1300"},
    {"ip": "80.66.82.27", "port": 5125, "name": "BLACK RUSSIA | VOLOGDA", "color": "F54141", "online": "137", "maxonline": "1300"},
    {"ip": "80.66.82.23", "port": 5125, "name": "BLACK RUSSIA | TVER", "color": "84B6FF", "online": "121", "maxonline": "1300"},
    {"ip": "80.66.82.24", "port": 5125, "name": "BLACK RUSSIA | TOMSK", "color": "00E9B2", "online": "279", "maxonline": "1300"},
    {"ip": "80.66.82.20", "port": 5125, "name": "BLACK RUSSIA | IZHEVSK", "color": "00A2A4", "online": "176", "maxonline": "1300"},
    {"ip": "80.66.82.21", "port": 5125, "name": "BLACK RUSSIA | SURGUT", "color": "4F27DE", "online": "190", "maxonline": "1300"},
    {"ip": "80.66.82.104", "port": 5125, "name": "BLACK RUSSIA | PODOLSK", "color": "B7A67E", "online": "235", "maxonline": "1300"},
    {"ip": "80.66.82.249", "port": 5125, "name": "BLACK RUSSIA | MAGADAN", "color": "B1C1C7", "online": "457", "maxonline": "1300"},
    {"ip": "80.66.82.153", "port": 5125, "name": "BLACK RUSSIA | CHEREPOVETS", "color": "3885E9", "online": "402", "maxonline": "1300"},
    {"ip": "80.66.82.154", "port": 5125, "name": "BLACK RUSSIA | NORILSK", "color": "AED4F6", "online": "444", "maxonline": "1300"},
    {"ip": "80.66.82.231", "port": 5125, "name": "BLACK RUSSIA | ASTANA", "color": "FFFFFF", "online": "849", "maxonline": "1300"}
]

def query_samp_server(ip, port, timeout=5):
    """
    Отправляет UDP запрос к SA-MP серверу и получает информацию о игроках.
    Использует стандартный протокол SA-MP Query.
    """
    try:
        # Создаем UDP сокет
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        
        # Формируем пакет для запроса информации (опкод 'i')
        # Структура: SAMP + IP в байтах + PORT + 'i'
        packet = b'SAMP' + socket.inet_aton(ip) + struct.pack('<H', port) + b'i'
        
        # Отправляем запрос
        sock.sendto(packet, (ip, port))
        
        # Получаем ответ
        data, _ = sock.recvfrom(4096)
        sock.close()
        
        # Парсим ответ
        if len(data) > 11 and data[0:4] == b'SAMP':
            offset = 11
            
            # Пароль (пропускаем)
            offset += 1
            
            # Количество игроков (2 байта)
            players = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            
            # Максимум игроков (2 байта)
            max_players = struct.unpack('<H', data[offset:offset+2])[0]
            
            return {
                "online": players,
                "maxonline": max_players,
                "status": "online"
            }
    except (socket.timeout, socket.error, struct.error):
        pass
    
    return None

@app.route('/')
def home():
    """Главная страница API"""
    return jsonify({
        "status": "ok",
        "message": "BLACK RUSSIA Monitor API",
        "servers_count": len(SERVERS),
        "endpoints": {
            "all_servers": "/api/servers",
            "single_server": "/api/server/<ip>/<port>"
        }
    })

@app.route('/api/servers')
def get_servers():
    """Возвращает статус всех 89 серверов в реальном времени"""
    results = []
    for server in SERVERS:
        info = query_samp_server(server["ip"], server["port"])
        results.append({
            "name": server["name"],
            "ip": server["ip"],
            "port": server["port"],
            "color": server["color"],
            "status": "online" if info else "offline",
            "online": info["online"] if info else 0,
            "maxonline": info["maxonline"] if info else int(server["maxonline"])
        })
    return jsonify(results)

@app.route('/api/server/<ip>/<int:port>')
def get_server(ip, port):
    """Проверяет один конкретный сервер"""
    info = query_samp_server(ip, port)
    if info:
        return jsonify({"status": "online", **info})
    return jsonify({"status": "offline"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)