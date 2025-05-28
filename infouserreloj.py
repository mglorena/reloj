from reloj import Reloj
from config import Conf
from datetime import datetime
from conectDB import sqlDB

class InfoReloj(object):
    _total = 0
    _listrecords = None
    _anviz = None

    def __init__(self):
        config = Conf()
        datosReloj = config.getConfReloj();
        self._anviz = Reloj(device_id=int(1), ip_addr=str(datosReloj.reloj), ip_port=int(datosReloj.puerto))
        records = self._anviz.download_staff_info()
        self._listrecords = list(records)
        total = len(self._listrecords)
        self._total = total
        print(total)
        for record in self._listrecords:
            strrec = str(record)
            print(strrec)
        
        print("New Record to Download: "+str(total))

r = InfoReloj()
