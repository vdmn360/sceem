import asyncio
import logging
import sys

from tornado.web import Application
from tornado.ioloop import IOLoop

from handlers.ws_handler import WSIOHandler

port = 8001
address = "127.0.0.1"


class WSServer(Application):
    def __init__(self):
        handlers = [
            (r'/wsserver', WSIOHandler),
        ]
        Application.__init__(self, handlers)


def main():
    logging.info("socket server start at : ws://127.0.0.1:8001")
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app_instance = WSServer()
    app_instance.listen(port, address=address)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
