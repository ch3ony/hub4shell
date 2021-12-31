import string
import random
import socket
from PyInquirer import prompt
import psutil
import platform
import re

def randomName():
    className = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    return className

def printPrompt(name, message):
    questions = [
        {
            'type': 'input',
            'name': name,
            'message': message,
        }
    ]
    pmt = prompt(questions)[name]

    return pmt

def getAddress():
    print(platform.system())
    if platform.system()=="Windows":
        addrs = psutil.net_if_addrs()
        list = []
        for addr in addrs.keys() :
            ip = addrs[addr][1][1]
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip):
                list.append(ip)
        return list
    elif platform.system()=="Linux":
        return


if __name__ == "__main__":
    print(getAddress())
