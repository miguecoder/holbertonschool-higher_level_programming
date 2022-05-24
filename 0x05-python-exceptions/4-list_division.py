#!/usr/bin/python3
from shutil import ExecError


def list_division(my_list_1, my_list_2, list_length):
    new = []
    div = 0
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new.append(div)
    return new
