# APC Service

Docker based APC UPS monitor that posts parsed status of one APC over HTTP POST in JSON format.

# Docker

Use image `reddec/apcsrv` (by [Docker HUB](https://hub.docker.com/r/reddec/apcsrv))

Useful environment:

* `TARGET`       - (*required*) URL where to POST data in JSON format. Supports redirects (e.x. [Redirect](http://gihub.com/reddec/redirect/))
* `APC_APC_HOST` - (*required*) IP address of APC UPS with SNMP access
* `APC_PORT`     - SNMP APC UPS port. Default is 161
* `INTERVAL`     - Interval in seconds between checks. Default is 3

# Example

    docker run --rm -i                                 \
      -e APC_HOST=192.168.1.2                          \
      -e "TARGET=http://192.168.1.3:10100/collect/apc" \
      reddec/apcsrv