#!/bin/bash

sed "s/UPSTYPE apcsmart/UPSTYPE snmp/g" /opt/apcupsd.conf | \
sed "s/#UPSNAME/UPSNAME $APC_NAME/g" | \
sed "s|DEVICE /dev/ttyS0|DEVICE $APC_HOST:$APC_PORT:APC:private|g" | \
sed "s/LOGSTATS off/LOGSTATS on/g" | \
sed "s/STATTIME 0/STATTIME 15/g"  > /etc/apcupsd/apcupsd.conf
apcupsd
python3 /usr/src/app/main.py
