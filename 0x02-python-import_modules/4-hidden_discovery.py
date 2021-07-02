#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    for h in dir(hidden_4):
        if h[0] == '_' and h[1] == '_':
            continue
        else:
            print('{}'.format(h))
