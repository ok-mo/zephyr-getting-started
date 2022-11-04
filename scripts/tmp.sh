#!/bin/bash
# Install sdk for the user running this script using sudo
export SUDO_USER=mmccabe
export ZSDK_VERSION=0.14.2
sudo -u $SUDO_USER /opt/toolchains/zephyr-sdk-${ZSDK_VERSION}/setup.sh -t all -h -c

# Set the locale
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export OVMF_FD_PATH=/usr/share/ovmf/OVMF.fd
