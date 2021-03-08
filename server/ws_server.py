from tornado.web import Application
from tornado.ioloop import IOLoop

from handlers.ws_handler import WSIOHandler

class WSServer(Application):
    def __init__(self):
        handlers = [
            (r'/wsserver/', WSIOHandler)
        ]
        Application.__init__(self, handlers)

def main():
    app_instance = WSServer()
    app_instance.listen(8001, address='0.0.0.0')
    IOLoop.instance.start()

if __name__ == '__main__':
    main()