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
        self._anviz.set_datetime(datetime.now())
        records = self._anviz.download_all_records()
        self._listrecords = list(records)
        total = len(self._listrecords)
        print("New Record to Download2: "+str(total))

    def getTotal(self):
        return self._total
    
        
    
r = InfoReloj()
