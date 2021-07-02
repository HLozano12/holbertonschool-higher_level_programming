#!/usr/bin/env python3
def uppercase(str):
    nuevo = ""
    for h in str:
        if ord(h) >= 97 and ord(h) <= 122:
            nuevo += chr(ord(h) - 32)
        else:
            nuevo += h
    print("{}".format(nuevo))
