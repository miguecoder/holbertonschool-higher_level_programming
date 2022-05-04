#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ac = ord(i)
        if 97 <= ac <= 122:
            ac = ac - 32
        print('{:c}'.format(ac), end = "")
    print()
