from datetime import datetime  
import datetime
import way2sms
from time import sleep
import csv
now = datetime.date.today()
d = open(r'C:\text.csv','r')
csv_f = csv.reader(d)

for t in csv_f:
    a = datetime.datetime.now()
    q = way2sms.sms("username","password")
    print q.send(t[0],t[1])
    print q.msgSentToday()
    q.logout()
    