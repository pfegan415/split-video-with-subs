#!/bin/bash

# Bash script for moving test files to a location that is easier for my home PC to open with VLC.

rm -r /mnt/c/Users/pfega/Videos/Superman/*

cp -r tests/input/ /mnt/c/Users/pfega/Videos/Superman/
cp -r tests/output/ /mnt/c/Users/pfega/Videos/Superman/