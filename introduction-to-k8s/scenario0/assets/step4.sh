#!/bin/bash

echo Please wait for background scripts to finish
while [ ! -f /tmp/background_step4 ]; do sleep 1; done
echo Done