import websocket

class WSClientHandler:
    def __init__(self):
        pass

    @staticmethod
    def on_open(websocket_instance):
        print("socket opened!")
    
    @staticmethod
    def on_message(websocket_instance, message):
        print("message recvd: {}".format(message))

    @staticmethod
    def on_close(websocket_instance):
        print("socket closed!")

    @staticmethod
    def on_error(websocket_instance, error):
        print("socket error: {}".format(error))