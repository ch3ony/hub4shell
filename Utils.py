import string
import random
import socket
from PyInquirer import prompt
import psutil
from termcolor import colored
import platform
import re

LOGO = """
                     _  _       _          _ _ 
 ___  ___  ___ _   _| || |  ___| |__   ___| | |
/ __|/ _ \/ __| | | | || |_/ __| '_ \ / _ \ | |
\__ \  __/ (__| |_| |__   _\__ \ | | |  __/ | |
|___/\___|\___|\__,_|  |_| |___/_| |_|\___|_|_|
             @Youngcheon & Kyuwan
"""

def randomName():
    className = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    return className

def printInputPrompt(name, message):
    questions = [
        {
            'type': 'input',
            'name': name,
            'message': message,
        }
    ]
    pmt = prompt(questions)[name]
    return pmt
def printListPrompt(name, message, list):
    questions = [
        {
            'type': 'list',
            'name': name,
            'message': message,
            'choices' : list
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
    print(colored(LOGO, 'green'))