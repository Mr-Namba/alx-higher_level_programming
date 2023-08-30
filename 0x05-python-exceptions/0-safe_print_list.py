#!/usr/bin/python3
def safe_print(my_list[], x = 0):
    prv = 0

    for i in range(x):
        try:
            print({}.format(my_list(i),end"")
            prv += 1
        except IndexError:
            break
    print("")
    return (prv)

