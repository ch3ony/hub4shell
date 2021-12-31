import string
import random
import socket
from PyInquirer import prompt
import psutil

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
    addrs = psutil.net_if_addrs()
    for addr in addrs.keys() :
        print(addrs[addr][1][1])


if __name__ == "__main__":
    getAddress()
