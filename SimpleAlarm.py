import time
from datetime import datetime

hour = int(input('Hour : '))
minute = int(input('Minute : '))
if hour <= 12:
    meredian = str(input('am/pm :'))
    if meredian == 'pm' and hour > 0 and hour < 12:
        hour = hour + 12

while True:
    if datetime.now().hour == hour and datetime.now().minute == minute:
        print('Alarming!!')
        break