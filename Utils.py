import string
import random
from PyInquirer import prompt

def randomName():
    class_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    return class_name

def printPrompt(name, message):
    questions = [
        {
            'type': 'input',
            'name': name,
            'message': message,
        }
    ]
    pmt = prompt(questions)

    return pmt


if __name__ == "__main__":
    print(randomName())
