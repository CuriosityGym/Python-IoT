import requests
import socket
import json

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
local_ip_address = s.getsockname()[0]
hostname = socket.gethostname()
#print (local_ip_address)
dataSet = {}
dataSet['value1'] = local_ip_address
dataSet['value2'] = hostname


json_data = json.dumps(dataSet)
URL="https://maker.ifttt.com/trigger/PiBoot/with/key/c7_XhH_HweVxsylITmRReL"


print (dataSet)
r = requests.post(URL, data=dataSet)
print(r.status_code, r.reason)
