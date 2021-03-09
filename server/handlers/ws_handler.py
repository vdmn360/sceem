from tornado.websocket import WebSocketHandler


class WSIOHandler(WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        try:
            print(self.request.headers.get('çlient_id'))
        except Exception as err:
            print(err)

    def on_message(self, message):
        print("message : {}".format(message))

    def on_close(self):
        print("client closed!")
