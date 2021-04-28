#!/usr/bin/python3
for h in range(10):
    for l in range(10):
        if (h != l and h < l):
            if h == 8 and l == 9:
                print('{}{}'.format(h, l))
            else:
                print('{}{}, '.format(h, l), end="")
