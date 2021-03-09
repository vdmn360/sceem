import websocket
from handlers.client_handler import WSClientHandler

port = 8001
host = "127.0.0.1"
endpoint = "wsserver"
def main():
    ws_client = websocket.WebSocketApp(
        "ws://{}:{}/{}".format(host, port, endpoint),
        on_message=WSClientHandler.on_message,
        on_close=WSClientHandler.on_close,
        on_error=WSClientHandler.on_error,
    )
    ws_client.on_open = WSClientHandler.on_open
    ws_client.run_forever()

if __name__ == '__main__':
    main()