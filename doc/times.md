## Python 日期和时间
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。时间间隔是以秒为单位的浮点小数。每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。

## python 时间元组
很多Python函数用一个元组装起来的9组数字处理时间,格式如下:
序号	字段	值
0	4位数年	2008
1	月	1 到 12
2	日	1到31
3	小时	0到23
4	分钟	0到59
5	秒	0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜


## 时间格式化代码
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身


## 代码

```

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


```






