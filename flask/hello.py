 # !/usr/bin/env python
# -*- encoding:utf-8 -*-

from flask import Flask

app = Flask(__name__) #创建一个Flask示例

@app.route('/hello') #通过route创建路由
def helloWorld():
  return "Hello world !"


if __name__ == '__main__':
  # 通过run启动一个server服务
  app.run(host='0.0.0.0',port=8080)
