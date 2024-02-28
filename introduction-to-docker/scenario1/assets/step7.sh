#!/bin/bash

echo Please wait for background scripts to finish
while [ ! -f /tmp/background7 ]; do sleep 1; done
echo Done