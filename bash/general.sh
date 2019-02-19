#!/bin/bash

# Passing in byte array to string stdin:
python -c 'print <bytecode as \x format>' | ./target
