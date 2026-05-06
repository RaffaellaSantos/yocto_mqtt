#!/usr/bin/env python3
import time
import json
import socket
import psutil
import paho.mqtt.client as mqtt

# ── Configurações ──────────────────────────────────────────
BROKER_HOST = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC_BASE = "embarcados/telemetria/v3"
INTERVAL = 5
CLIENT_ID = "yocto-device-01"
# ───────────────────────────────────────────────────────────

def coletar_dados():
    origem_dispositivo = socket.gethostname()
    return {
        "user": origem_dispositivo,
        "cpu_percent": psutil.cpu_percent(interval=1),
        "mem_total_mb": round(psutil.virtual_memory().total / 1024**2, 2),
        "mem_used_mb": round(psutil.virtual_memory().used / 1024**2, 2),
        "mem_percent": psutil.virtual_memory().percent,
        "disk_total_mb": round(psutil.disk_usage("/").total / 1024**2, 2),
        "disk_free_mb": round(psutil.disk_usage("/").free / 1024**2, 2),
        "disk_percent": psutil.disk_usage("/").percent,
        "timestamp": int(time.time()),
    }

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("[MQTT] Conectado ao broker!")
    else:
        print(f"[MQTT] Falha na conexão, código: {rc}")

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=CLIENT_ID)
    client.on_connect = on_connect

    while True:
        try:
            client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
            client.loop_start()
            break
        except Exception as e:
            print(f"[MQTT] Erro ao conectar: {e}. Tentando em 5s...")
            time.sleep(5)

    print("[Telemetria] Iniciando coleta...")
    while True:
        try:
            dados = coletar_dados()
            payload = json.dumps(dados)
            client.publish(TOPIC_BASE, payload, qos=1)
            print(f"[Telemetria] Publicado: {payload}")
        except Exception as e:
            print(f"[Telemetria] Erro: {e}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
