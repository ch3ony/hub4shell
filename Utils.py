import string
import random
import socket
from PyInquirer import prompt, style_from_dict, Token
import colorama
import psutil
from termcolor import *
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

LDAP_PORT = 65210
HTTP_PORT = 65211

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

def killPythonProcee():
    net = psutil.net_connections()
    for con in net:
        if(con[3][1]==LDAP_PORT or con[3][1]==HTTP_PORT):
            parent = psutil.Process(con[6])
            for child in parent.children(recursive=True):
                child.kill()
            parent.kill()


if __name__ == "__main__":
    killPythonProcee()