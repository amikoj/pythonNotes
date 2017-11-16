
#!/usr/bin/python
# -*- encoding:utf-8 -*-
##times

import time 

current =time.time()
print current

time1=time.localtime(time.time());
time1=time.localtime();
print  time1[0]

##format times
time2=time.asctime()
print time2;
print time.strftime(format('%Y/%m/%d   %H:%M:%S'))

# 将格式字符串转换为时间戳
a = "Sat Jun  3 22:17:35 2017"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

import calendar


cal = calendar.month(2017,6)
print cal

