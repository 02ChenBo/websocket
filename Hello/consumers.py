from channels.generic.websocket import WebsocketConsumer
import json
import threading
import time

cancel_tmr = False


class ChatConsumer(WebsocketConsumer):
    # 连接上的方法
    def connect(self):
        self.accept()
        self.heart_beat()
        print('connect----')

    # 断开连接时进入
    def disconnect(self, close_code):
        pass
        print('disconnect----')

    # 接收到消息的方法
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))

    # 心跳检测
    def heart_beat(self):
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        # print(date)
        self.send(text_data=json.dumps({
            'message': date
        }))
        if not cancel_tmr:
            threading.Timer(3, self.heart_beat).start()
