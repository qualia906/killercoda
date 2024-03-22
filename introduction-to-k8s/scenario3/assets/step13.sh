#!/bin/bash

echo Please wait for background scripts to finish
while [ ! -f /tmp/background_intro ]; do sleep 1; done
echo Done