#!/bin/bash

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Not running as root"
    exit
fi

cp acpi.py /etc/dd-agent/checks.d/
cp acpi.yaml /etc/dd-agent/conf.d/
chown dd-agent:dd-agent /etc/dd-agent/checks.d/acpi.py
chown dd-agent:dd-agent /etc/dd-agent/conf.d/acpi.yaml
service datadog-agent restart

