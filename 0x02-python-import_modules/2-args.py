 #!/usr/bin/python3
import sys
if __name__ == '__main__':
    h = len(sys.argv)
    if h == 1:
        print("0 arguments.")
    elif h == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(h - 1))
    for l in range(1, h):
        print("{}: {}".format(l, sys.argv[l]))