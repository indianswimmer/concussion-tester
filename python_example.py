import argparse
import threading
import time
from pythonosc import dispatcher
from pythonosc import osc_server
import pandas

STATE = ''


def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4=0):
    print("EEG (uV) per channel: ", ch1, ch2, ch3, ch4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5001,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatch = dispatcher.Dispatcher()
    dispatch.map("/debug", print)
    dispatch.map("/muse/acc", eeg_handler, "EEG")

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatch)
    server_thread = threading.Thread(target=server.serve_forever)
    print("Serving on {}".format(server.server_address))
    server_thread.start()

    time.sleep(5)
    global STATE
    STATE = 'done'

    server.shutdown()
    print("Done serving on {}".format(server.server_address))
