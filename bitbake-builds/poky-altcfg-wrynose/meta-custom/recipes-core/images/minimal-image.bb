SUMMARY = "Imagem minima para rodar MQTT"      
LICENSE = "MIT"

inherit core-image

IMAGE_LINGUAS = ""

IMAGE_INSTALL = " \
    busybox \
    python3-core \
    python3-json \
    python3-paho-mqtt \
    python3-psutil \
    init-script \
"

IMAGE_FEATURES = ""

DISTRO_FEATURES:remove = "x11 wayland bluetooth wifi nfc"

QB_KERNEL_CMDLINE_APPEND += " init=/init/init-script.sh"

IMAGE_FSTYPES += "tar.gz"

NO_RECOMMENDATIONS = "1"

PACKAGE_EXCLUDE += "openssl-bin openssl-conf"
