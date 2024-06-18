from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer
import time

# Define a handler function to process incoming messages
def print_handler(address, *args):
    print(f"Received message from {address}: {args}")


# Set up the dispatcher and map the OSC address to the handler
dispatcher = Dispatcher()
# setup a default handler to handle any messages that don't match the mapped addresses
dispatcher.set_default_handler(print_handler)


# Define the IP and port for the server
ip = "127.0.0.1"
port = 9981

# Set up the server
server = ThreadingOSCUDPServer((ip, port), dispatcher)

# Start the server in a new thread
import threading
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    # Clean up and stop the server
    print ('shutting down server')
    server.shutdown()
    server_thread.join()