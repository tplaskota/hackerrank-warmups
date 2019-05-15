#!/bin/python3

import sys


time = input().strip()
if time[-2:] == 'PM':
    print(str(int(time[:2]) % 12 + 12).zfill(2)+time[2:-2])
else:
    print(str(int(time[:2]) % 12).zfill(2)+time[2:-2])
