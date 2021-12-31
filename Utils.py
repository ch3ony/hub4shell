import string
import random
import socket
from PyInquirer import prompt

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
    print(socket.gethostbyname(socket.gethostname()))
    return


if __name__ == "__main__":
    getAddress()
