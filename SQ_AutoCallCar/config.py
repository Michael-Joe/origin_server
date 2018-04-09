# coding=utf-8

import time
import datetime

cookie = 'Hm_lvt_44b89a2108eb84a48ec1b4f686af2753=1521018627,1521122589; JSESSIONID=C6A28D72488B2B14942005B5E63E87CA; Hm_lpvt_44b89a2108eb84a48ec1b4f686af2753=1521122597; yc_cityName=%E5%8C%97%E4%BA%AC%E5%B8%82; yc_sid=zBp35C1DZ7MplxmesUB9iOBxoAoyrOcA0szZUZYDDO4dyzKgF-bUVIISmPwiHB4G'

# 预约叫车时间 （今天 21:10:36）
BookTime = '%Y-%m-%d 21:10:36'

now = datetime.datetime.now()
a = now.strftime(BookTime)
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
curr_time = int(time.mktime(timeArray))
curr_ime = str(int(time.time()))  
#即时叫车

# 上车位置
StartAddr = '百度科技园2号楼'

# 下车位置
EndAddr = '图景嘉园9号楼'

# 上车位置经度
StartPointLo = '116.274152'

# 上车位置纬度
StartPointLa = '40.044248'

# 下车位置经度
EndPointLo = '116.271292'

# 下车位置纬度
EndPointLa = '40.062674'
