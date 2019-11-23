import socket
import zmq
import json
import argparse
import signal
import os


running = True
parser = argparse.ArgumentParser(description='bluewalker-gateway')
parser.add_argument('-b', '--bluewalker-socket', required=False, help='bluewalker unix socket', default='/var/run/bluewalker-gateway/bluewalker.sock')
parser.add_argument('-r', '--relay-zmq', required=False, help='zmq socket where to relay messages to', default='ipc:///var/run/bluewalker-gateway/relay.zmq')
args = parser.parse_args()


if os.path.exists(args.bluewalker_socket):
    os.unlink(args.bluewalker_socket)
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(args.bluewalker_socket)
sock.listen()


def sighandler(_a, _b):
    global running
    global sock
    running = False
    sock.close()


def main():
    global running
    signal.signal(signal.SIGINT, sighandler)
    signal.signal(signal.SIGTERM, sighandler)
    os.umask(0o111)
    zc = zmq.Context()
    zs = zc.socket(zmq.PUSH)
    zs.bind(args.relay_zmq)
    while running:
        conn, _addr = sock.accept()
        fd = conn.makefile()
        while running:
            line = fd.readline()
            if not line:
                break
            try:
                zs.send_json(json.loads(line), zmq.NOBLOCK)
            except zmq.Again:
                pass
    os.unlink(args.bluewalker_socket)


if __name__ == '__main__':
    main()
