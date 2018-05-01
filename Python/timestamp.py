import time

def timestamp() :
    now = time.localtime()

    timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" % 
    (now.tm_year, now.tm_mon, now.tm_mday, 
    now.tm_hour, now.tm_min, now.tm_sec))

    return timestamp