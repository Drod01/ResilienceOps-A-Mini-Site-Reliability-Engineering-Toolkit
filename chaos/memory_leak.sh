#!/bin/bash
echo "Allocating excessive memory..."
python3 -c "a = ' ' * 1024 * 1024 * 500"  # 500MB leak
sleep 20
