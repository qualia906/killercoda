#!/bin/sh
echo "Wait for creating containers."
while [ ! -f /tmp/background7 ]; do sleep 1; done
echo "Containers created"