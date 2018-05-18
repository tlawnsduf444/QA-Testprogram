# -*- coding:utf-8 -*-
from datetime import datetime
import time
#----------------------------
starttime = datetime.now()
time.sleep(2)
stoptime = datetime.now()
term = stoptime - starttime
print(term.strftime('%H시 %M분 %S초'))