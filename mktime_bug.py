import ctypes

mktime = ctypes.CDLL('libc.so.6').mktime

# https://stackoverflow.com/a/46982702
class TimeStruct(ctypes.Structure):
    _fields_ = [
        ("tm_sec", ctypes.c_int),
        ("tm_min", ctypes.c_int),
        ("tm_hour", ctypes.c_int),
        ("tm_mday", ctypes.c_int),
        ("tm_mon", ctypes.c_int),
        ("tm_year", ctypes.c_int),
        ("tm_wday", ctypes.c_int),
        ("tm_yday", ctypes.c_int),
        ("tm_isdst", ctypes.c_int),
    ]

mktime.argtypes = [ctypes.POINTER(TimeStruct), ]
mktime.restype = ctypes.c_int

for isdst in (-1, 0, 1):
    tm = TimeStruct(tm_year=2017, tm_mon=5, tm_mday=21, tm_hour=15, tm_min=30, tm_sec=16, tm_wday=6, tm_yday=141, tm_isdst=isdst)
    print(tm._objects)
    res = mktime(tm)
    print(tm._objects)
    print(f"tm_isdst={isdst} mktime -> {res}", flush=True)

print("done", flush=True)
