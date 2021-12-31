import Utils as ut
import LDAPServer as LS
import HTTPServer as HS
import threading

def init():
    ut.killPythonProcee()
    ut.colorama.init()

def main():
    #logo printng
    print(ut.colored(ut.LOGO, 'yellow'))

    #IP input
    ip = ut.printListPrompt('IP', 'Choose the ip :', ut.getAddress())

    #thread 선언
    t1 = threading.Thread(target=LS.OpenLDAPService, args=(ip, ut.LDAP_PORT, ut.HTTP_PORT))
    t1.start()
    ut.cprint('[+] LDAP SERVER OPEN', 'yellow')


    t2 = threading.Thread(target=HS.httpServer, args=(ut.HTTP_PORT,))
    t2.start()
    ut.cprint('[+] HTTP SERVER OPEN', 'yellow')

    #LDAP Server open
    #LS.OpenLDAPService(ip, ut.LDAP_PORT, ut.HTTP_PORT)

if __name__ == "__main__":
    init()
    main()


