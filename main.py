import Utils as ut
import LDAPServer as LS
import HTTPServer as HS
import threading

def init():
    ut.killPythonProcee()

def main():
    #logo printng
    print(ut.colored(ut.LOGO, 'green'))

    #IP input
    ip = ut.printListPrompt('IP', 'Choose the ip :', ut.getAddress())

    #thread 선언


    #LDAP Server open
    LS.OpenLDAPService(ip, ut.LDAP_PORT, ut.HTTP_PORT)




if __name__ == "__main__":
    init()
    main()

