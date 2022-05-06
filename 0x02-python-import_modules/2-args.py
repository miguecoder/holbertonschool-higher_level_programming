#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv) - 1
    if (argv_len == 0):
        print(f"{argv_len} arguments.")
    elif (argv_len == 1):
        print(f"{argv_len} argument:")
        print(f"{argv_len}: {argv[1]}")
    else:
        print(f"{argv_len} arguments:")
    for i in range(1, argv_len + 1, 1):
        print(f"{i}: {argv[i]}")
