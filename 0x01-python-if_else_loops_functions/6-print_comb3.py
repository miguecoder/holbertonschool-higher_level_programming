#!/usr/bin/python3
for j in range(0, 89):
    if j / 10 < j % 10:
        print(f"{j:02d}, ", end='')
print(89)