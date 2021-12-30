import string
import random
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


if __name__ == "__main__":
    print(randomName())
