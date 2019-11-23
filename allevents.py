import zmq
import json


def main():
    zc = zmq.Context()
    zs = zc.socket(zmq.PULL)
    zs.connect('ipc:///var/run/bluewalker-gateway/relay.zmq')
    while True:
        print(json.dumps(zs.recv_json()))


if __name__ == '__main__':
    main()
