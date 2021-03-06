from setup import registry

import socketio
import time

sio = socketio.Client()

class Socket():
    def __init__(self, api, room, status):
        print(api, room)
        self._isConnected = False
        self._socket = socketio.Client()
        time.sleep(1)
        self._socket.connect(api["url"]) #ws://sw-bot.mathis-figuet.com
        time.sleep(1)
        self.room_create({"credentials": api["credentials"], "room": room})
        self._status = status
        

        @self._socket.event
        def connect(self):
            print("Connection established.")

        @self._socket.event
        def update_order(order):
            print('order received : ', order)
            if "request" in order.keys():
                if order["request"] == "synchronise":
                    self.send_status(status.send())
                if order["request"] == "changeStage":
                    print("change Farm")
                    registry['in_game']['activeFarm']['farm'] = 'autofarm'
                    registry['in_game']['activeFarm']['times'] = 10
                    registry['in_game']['activeFarm']['user'] = True
                    registry['status']._actual = order["data"]["stage"]
                    self.send_status(registry['status'].send())
                    #Manager.selectFarm(farm = 'autofarm', times = 1000)

        @self._socket.event
        def is_connected(connected):
            print('Is connected : ', connected)
            self._isConnected = True

        @self._socket.event
        def disconnect(self):
            print("Disconected from webSocket.")

    def room_create(self, data):
        self._socket.emit("room_create", data)

    def send_status(self, status):
        print("Send status ...")
        self._socket.emit("send_status", status)
