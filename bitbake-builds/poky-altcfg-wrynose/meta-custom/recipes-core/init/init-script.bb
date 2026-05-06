SUMMARY = "Init - Recipe"
LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " \ 
    file://init-script.sh \
    file://init-mqtt.py \
"

S = "${UNPACKDIR}"

do_install() {
    install -d ${D}/init
    install -m 0755 ${S}/init-script.sh ${D}/init/init-script.sh
    install -m 0755 ${S}/init-mqtt.py ${D}/init/init-mqtt.py
}

FILES:${PN} += "/init /init/init-script.sh /init/init-mqtt.py"

RDEPENDS:${PN} = "busybox"
