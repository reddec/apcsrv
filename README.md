# APC Service

Docker based APC UPS monitor that posts parsed status of one APC over HTTP POST in JSON format.

# Docker

Use image `reddec/apcsrv` (by [Docker HUB](https://hub.docker.com/r/reddec/apcsrv))

Useful environment:

* `TARGET`       - (*required*) URL where to POST data in JSON format. Supports redirects (e.x. [Redirect](http://github.com/reddec/redirect/))
* `APC_APC_HOST` - (*required*) IP address of APC UPS with SNMP access
* `APC_PORT`     - SNMP APC UPS port. Default is 161
* `INTERVAL`     - Interval in seconds between checks. Default is 3

# Example

    docker run --rm -i                                 \
      -e APC_HOST=192.168.1.2                          \
      -e "TARGET=http://192.168.1.3:10100/collect/apc" \
      reddec/apcsrv


# JSON Example


```json
{
    "alarmdel": {
        "type": "seconds",
        "value": "5"
    },
    "stesti": {
        "type": "",
        "value": "336"
    },
    "dwake": {
        "type": "seconds",
        "value": "000"
    },
    "battv": {
        "type": "volts",
        "value": 218.0
    },
    "lotrans": {
        "type": "volts",
        "value": 154.0
    },
    "": {
        "type": "+0000",
        "value": "28"
    },
    "status": {
        "type": "",
        "value": "ONLINE"
    },
    "hitrans": {
        "type": "volts",
        "value": 242.0
    },
    "driver": {
        "type": "",
        "value": "SNMP UPS Driver"
    },
    "statflag": {
        "type": "status flag",
        "value": "0x07000008"
    },
    "sense": {
        "type": "",
        "value": "Unknown"
    },
    "firmware": {
        "type": "",
        "value": "476.17.W"
    },
    "itemp": {
        "type": "c internal",
        "value": 14.0
    },
    "mbattchg": {
        "type": "percent",
        "value": "5"
    },
    "bcharge": {
        "type": "percent",
        "value": 100.0
    },
    "mintimel": {
        "type": "minutes",
        "value": "3"
    },
    "maxlinev": {
        "type": "volts",
        "value": 227.0
    },
    "battdate": {
        "type": "",
        "value": "11/06/15"
    },
    "end_apc": {
        "type": "",
        "value": "2016-03-19 19:28:43 +0000"
    },
    "maxtime": {
        "type": "seconds",
        "value": "0"
    },
    "lastxfer": {
        "type": "",
        "value": "Automatic or explicit self test"
    },
    "cumonbatt": {
        "type": "seconds",
        "value": "0"
    },
    "upsname": {
        "type": "",
        "value": "XXXXYYYZZZ"
    },
    "xoffbatt": {
        "type": "",
        "value": "N/A"
    },
    "model": {
        "type": "",
        "value": "Smart-UPS RT 10000 XL"
    },
    "nomoutv": {
        "type": "volts",
        "value": "220"
    },
    "apc": {
        "type": "",
        "value": "001,049,1179"
    },
    "date": {
        "type": "",
        "value": "2016-03-19 19:28:43 +0000"
    },
    "minlinev": {
        "type": "volts",
        "value": 218.0
    },
    "extbatts": {
        "type": "",
        "value": "1"
    },
    "starttime": {
        "type": "",
        "value": "2016-03-19 19:28:25 +0000"
    },
    "ambtemp": {
        "type": "c",
        "value": 0.0
    },
    "loadpct": {
        "type": "percent load capacity",
        "value": 17.0
    },
    "dshutd": {
        "type": "seconds",
        "value": "020"
    },
    "cable": {
        "type": "",
        "value": "Ethernet Link"
    },
    "humidity": {
        "type": "percent",
        "value": 0.0
    },
    "serialno": {
        "type": "",
        "value": "xxxxxxxxxxxxxxxxx"
    },
    "numxfers": {
        "type": "",
        "value": "0"
    },
    "linev": {
        "type": "volts",
        "value": 226.0
    },
    "retpct": {
        "type": "percent",
        "value": 0.0
    },
    "badbatts": {
        "type": "",
        "value": "0"
    },
    "version": {
        "type": "",
        "value": "3.14.10 (13 September 2011) debian"
    },
    "selftest": {
        "type": "",
        "value": "OK"
    },
    "timeleft": {
        "type": "minutes",
        "value": 59.0
    },
    "upsmode": {
        "type": "",
        "value": "Stand Alone"
    },
    "hostname": {
        "type": "",
        "value": "yyyyyyyyyyyy"
    },
    "dlowbatt": {
        "type": "minutes",
        "value": "02"
    },
    "tonbatt": {
        "type": "seconds",
        "value": "0"
    },
    "outputv": {
        "type": "volts",
        "value": 221.0
    },
    "mandate": {
        "type": "",
        "value": "01/12/08"
    },
    "linefreq": {
        "type": "hz",
        "value": 50.0
    }
}
```