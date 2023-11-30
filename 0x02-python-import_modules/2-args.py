#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1

    if leng == 0:
        print("{} arguments.".format(i))
    elif leng == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if leng >= 1:
    leng = 0
        for arg in sys.argv:
            if leng != 0:
                print("{}: {}".format(leng, arg))
            leng += 1
