import os
import requests
import requests.exceptions
import time
import json

unlabeled = {
    'status', 'starttime', 'sense', 'badbatts', 'firmware', 'upsname', 'extbatts', 'lastxfer', 'driver', 'cable',
    'hostname', 'apc', 'serialno', 'version', 'model', 'end apc', 'battdate', 'date', 'mandate', 'upsmode'}

number = {'maxlinev', 'ambtemp', 'retpct', 'lotrans', 'humidity', 'hitrans', 'linev', 'minlinev', 'linefreq',
          'timeleft', 'loadpct', 'outputv', 'itemp', 'bcharge', 'battv', 'nomoutv', 'cumonbatt', 'maxtime', 'mintimel',
          'mbattchg', 'alarmdel', 'dwake', 'extbatts', 'tonbatt'}


def parse(key, value):
    key = key.lower()
    param = ""
    if key not in unlabeled:
        # Try to split value into value and typename (ex. 100 Volts)
        valparam = value.split(' ', 1)
        if len(valparam) == 2:
            value, param = valparam
        else:
            value = valparam[0]
    if key in number:
        # Convert value from string to number
        try:
            value = float(value)
        except:
            value = None
    return key.replace(' ', '_'), {"value": value, "type": param.lower()}


stat_file = os.getenv('STAT_FILE', '/var/log/apcupsd.status')
interval = int(os.getenv('INTERVAL', '3'))
target = os.getenv('TARGET', '')
name = os.getenv('APC_NAME', '')

while True:
    try:
        with open(stat_file, 'rt') as fstat:
            text = fstat.read()
        data = dict(parse(v[0].strip(), v[1].strip()) for v in
                    (line.strip().split(':', 1) for line in text.splitlines() if ':' in text))
        data['name'] = {'type': 'string', 'value': name}
        data = json.dumps(data)
        print(data)
        requests.post(target, data=data, headers={"Content-Type": "application/json; charset=utf-8"})
    except requests.exceptions.RequestException as ex:
        print(ex)
    except FileNotFoundError as ex:
        print(ex)
    time.sleep(interval)
