from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer
import time
import threading


class OSC_Receiver():
    def __init__(self, ipaddr="127.0.0.1", port=9981):
        self.dispatcher = Dispatcher()
        self.dispatcher.set_default_handler(self.print_handler)
        self.server = ThreadingOSCUDPServer((ipaddr, port), self.dispatcher)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

    # Define a handler function to process incoming messages
    def print_handler(address, *args):
        print(f"Received message{args}")

    def add_handler(self, address, handler):
        self.dispatcher.map(address, handler)

    def shutdown(self):
        self.server.shutdown()


if __name__ == "__main__":
    osc_receiver = OSC_Receiver()
    print("receiving messages...")
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            osc_receiver.shutdown()
            break

