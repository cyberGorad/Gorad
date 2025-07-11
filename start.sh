#!/bin/bash

cd /opt/IDS-GORAD
source venv/bin/activate
daphne -b 0.0.0.0 -p 8000 port_monitor.asgi:application
