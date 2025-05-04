#!/bin/bash
echo "Injecting network latency..."
tc qdisc add dev eth0 root netem delay 200ms
sleep 30
tc qdisc del dev eth0 root netem
