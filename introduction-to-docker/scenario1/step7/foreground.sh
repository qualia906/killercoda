#!/bin/bash

echo Waiting for background scripts to finish
while [ ! -f /tmp/background2 ]; do sleep 1; done
echo Done