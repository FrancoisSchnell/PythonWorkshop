# Monitor network usage with psutil lib
# https://psutil.readthedocs.io/en/latest/#psutil.disk_io_counters

import psutil, time
from datetime import datetime

# initial values when script launched
res0= psutil.net_io_counters()
t0= datetime.now()
recvInit = res0.bytes_recv
sentInit = res0.bytes_sent

print("Counting Mo received and sent...")
while True:
    time.sleep(10)
    res= psutil.net_io_counters()
    moReceived = res.bytes_recv - recvInit 
    moSent = res.bytes_sent - sentInit
    duration = datetime.now()- t0
    print("Duration : ", str(duration).split(".")[0])
    print("Received:",moReceived/1000000.0,"Mo ")
    print("Sent:",moSent/1000000,"Mo ") 