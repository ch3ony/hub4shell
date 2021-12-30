import string
import random


def randomName():
    class_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    return class_name


if __name__ == "__main__":
    print(randomName())
