#!/bin/bash

echo Please wait for background scripts to finish
while [ ! -f /tmp/background3 ]; do sleep 1; done
echo Done
