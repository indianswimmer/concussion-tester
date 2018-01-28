import argparse

from pythonosc import dispatcher
from pythonosc import osc_server

def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4=0):
    print("EEG (uV) per channel: ", ch1, ch2, ch3, ch4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatch = dispatcher.Dispatcher()
    dispatch.map("/debug", print)
    dispatch.map("/muse/elements/low_freqs_absolute", eeg_handler, "EEG")

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
    server.shutdown()

main()
