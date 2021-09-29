import os
import time

def ping_multiplo(arquivo):
    with open(arquivo) as file:
        dump = file.read()
        dump = dump.splitlines()
        for ip in dump:
            os.system('ping {}'.format(ip))
            time.sleep(5)

        return dump


if __name__ == "__main__":
    print(ping_multiplo('host.txt'))