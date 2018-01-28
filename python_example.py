import argparse
import threading
import time
import pandas as pd
from pythonosc import dispatcher
from pythonosc import osc_server

STATE = None


global rows_list
rows_list = []

def handler(unused_addr, args, ch1=0, ch2=0, ch3=0, ch4=0):
    d = {"ch1": ch1, "ch2":ch2, "ch3":ch3, "ch4":ch4}
    rows_list.append(d)
    print(unused_addr, args, ch1, ch2, ch3, ch4)

def collectData(signal="eeg"):
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
    dispatch.map("/muse/"+signal, handler, "EEG")
    # dispatch.map("/muse/elements/")

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatch)
    server_thread = threading.Thread(target=server.serve_forever)
    print("Serving on {}".format(server.server_address))
    server_thread.start()

    time.sleep(5)
    global STATE
    STATE = 'done'

    server.shutdown()
    print("Done serving on {}".format(server.server_address))

def analysis(data = rows_list):
    df = pd.DataFrame(data)
    # import pdb;pdb.set_trace()
    tot = 0
    count = 0
    for column in df:
        tot += df[column].mean()
        count += 1
    avg = tot / count
    return avg % 100


collectData()
res = analysis(rows_list)
print ("result:", res)
