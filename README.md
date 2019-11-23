# bluewalker-gateway

Simple python gateway to access bluewalker data for multiple processes. Get bluewalker from https://gitlab.com/jtaimisto/bluewalker .

## Installing

The provided systemd unit files assume that bluewalker is installed to `/usr/local/sbin/bluewalker` and these scripts are in `/opt/bluewalker-gateway` folder.

### Create virtualenv
```
# cd /opt/bluewalker-gateway
# python3 -m venv env
# ./env/bin/pip install -r requirements.txt
```

### Create and enable services
```
# ln -s /opt/bluewalker-gateway/systemd/bluewalker-gateway.service /etc/systemd/system/bluewalker-gateway.service
# systemctl enable --now bluewalker-gateway.service
# ln -s /opt/bluewalker-gateway/systemd/bluewalker.service /etc/systemd/system/bluewalker.service
# systemctl enable --now bluewalker.service
```

### Test if everything works

If this works, everything is ok. If output is not seen, try checking `systemctl status bluewalker-gateway` and `systemctl status bluewalker`

```
/opt/bluewalker-gateway/env/bin/python allevents.py
{"data": ... }
{"data": ... }
```
