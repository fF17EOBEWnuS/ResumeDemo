from datetime import datetime
import subprocess


fmt = '%Y-%m-%d %H:%M:%S'

tstamp1pre = subprocess.check_output("cat /var/log/battery-percentage.log| grep '100.0' | tail -n1", shell=True).decode("utf-8")
ts1=tstamp1pre[1:20]
dat1=tstamp1pre[22:-1]
tstamp2pre = subprocess.check_output("cat /var/log/battery-percentage.log| tail -n1", shell=True).decode("utf-8")
ts2=tstamp2pre[1:20]
dat2=tstamp2pre[22:-1]

tstamp1 = datetime.strptime(ts1, fmt)
tstamp2 = datetime.strptime(ts2, fmt)
td = tstamp2 - tstamp1
td_mins = int(round(td.total_seconds() / 60 ))

print('The difference is approx. %s minutes' % td_mins)


#print("%s"%tstamp1post[22:-1])
