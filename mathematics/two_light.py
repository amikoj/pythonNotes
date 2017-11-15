# !/usr/bin/etc python
# -*-encoding:utf-8 -*-

import  sys
'''
二灯问题:
1)绿灯灭,黄灯亮
2)两个灯都灭
3)两个灯都亮

如上情况,可以按钮

'''

class Light:
    ON="on"
    OFF="off"
    def __init__(self,state=ON):
        '''
        灯的状态,设置两种:开启状态和关闭状态
        :param state:
        '''
        self.state=state





def IsCanPressed(greenState,yellowState):
    greenLightOn = greenState.state==Light.ON
    yellowLightOn = yellowState.state==Light.ON
    valA = not greenLightOn and yellowLightOn  #条件一
    valB = not greenLightOn and not yellowLightOn #条件二
    valC = greenLightOn and yellowLightOn  #条件三
    if (valA or valB or valC):
        return True
    else:
        return False



if  __name__ == "__main__":
   canPress= IsCanPressed(Light(Light.ON),Light(Light.OFF))
   print "you can press now." if canPress else  "you not can press"
