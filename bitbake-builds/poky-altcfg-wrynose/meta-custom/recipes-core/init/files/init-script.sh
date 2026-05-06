#!/bin/sh

echo "\n ================== Minimal Image DSE ===================="

mkdir -p /proc /sys /dev
mount -t proc proc /proc
mount -t sysfs sysfs /sys
mount -t devtmpfs devtmpfs /dev

echo "Configurando DNS..."
echo "nameserver 8.8.8.8" > /etc/resolv.conf

echo "Verificando dependencias do sistema..."
python3 --version
python3 -c "import paho.mqtt; import psutil; print('\n Ambiente MQTT e Telemetria: OK!')"

echo "Listando diretórios:"
ls /

echo "Iniciando client MQTT de telemetria..."
exec python3 -u /init/init-mqtt.py
