import ujson
import urequests as requests
from machine import RTC

rtc = RTC()

def init_clock():

    res = requests.get(url = 'http://worldtimeapi.org/api/timezone/Europe/Warsaw').text
    res = ujson.loads(res)['datetime']

    yr = int(res[0:4])
    mth = int(res[5:7])
    day = int(res[8:10])
    hr = int(res[11:13])
    mnt = int(res[14:16])
    sec = int(res[17:19])
    msec = int(res[20:23])

    print(yr, mth, day, hr, mnt, sec, msec)

    rtc.init((yr, mth, day, 0, hr, mnt, sec, msec))

    return rtc

