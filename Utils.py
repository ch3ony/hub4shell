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


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

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
    pmt = prompt(questions, style=style)[name]
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
    pmt = prompt(questions, style=style, qmark='[?]')[name]
    return pmt

def getAddress():
    if platform.system()=="Windows":
        num = 1
    elif platform.system()=="Linux":
        num = 0

    addrs = psutil.net_if_addrs()
    list = []
    for addr in addrs.keys():
        ip = addrs[addr][num][1]
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            list.append(ip)
    return list


if __name__ == "__main__":
    ip = printListPrompt('ip', 'choose the ip : ', getAddress())