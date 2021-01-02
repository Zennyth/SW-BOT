import socketio
import time

sio = socketio.Client()

status = {
    "state": "on",
    "history": [
        {
            "type": "db",
            "stage": "Dragon B12",
            "time": "12",
            "progress": "In progress"
        },
        {
            "type": "gb",
            "stage": "Giant B12",
            "time": "14",
            "progress": "Complete"
        },
        {
            "type": "gb",
            "stage": "Giant B12",
            "time": "15.2",
            "progress": "Complete"
        }
    ]
}

data_create = {
    "credentials": {
        "API_KEY": "API_KEY-SWRM-python",
    },
    "room": {
        "id": "1002",
        "password": "7400"
    }
}

class Socket():
    def __init__(self):
        global data_create
        global status
		self._socket = socketio.Client()
        self._socket.connect("ws://localhost:8080")
        self.room_create(data_create)
        while 1:
            self.send_status(status)
            time.sleep(5)

    @sio.event
    def connect():
        print("Connection established.")

    def room_create(data):
        sio.emit("room_create", data)

    def send_status(status):
        sio.emit("send_status", status)

    @sio.event
    def update_order(order):
        print('order received : ', order)
        if "request" in order.keys() and order["request"] == "synchronise":
            send_status(status)

    @sio.event
    def is_connected(connected):
        print('Is connected : ', connected)

    @sio.event
    def disconnect():
        print("Disconected from webSocket.")