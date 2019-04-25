#!/bin/bash

# Passing in byte array to string stdin:
python -c 'print <bytecode as \x format>' | ./target

# Find any file locally on machine
locate --regex '<target-file>'
find / -name "<target-file" -exec grep "<file-contents>" {} \;

