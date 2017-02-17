import sys
import telnetlib
import socket
import time
def loginToDut(HOST):
    user = "ADMIN"
    password = "PASSWORD"
    # try:
    #     tn = telnetlib.Telnet(HOST)
    # except:
    #     print "UNREACHABLE HOST   "+HOST+"\n"
    #     return
    #     pass
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username:",5)
    tn.write(user + '\r')
    while tn.expect(['Password:'], 5)[0] == -1:
        #i = tick(i)
        print 'It did not rcv Password'
        status[0] = False
        tn.close()
        #print ' ################################################# '
        return status

    tn.write(password + '\r\n')
    #print 'success  '+HOST
    
    tn.write("enable\r\n")
    tn.read_until("#")
    tn.write("terminal length 0\r\n")
    tn.read_until("#")
    tn.write("show topology tree detail\r")
    x=tn.read_until("#")
    temp = []
    y = x.split("\n")
    for n in y:
        z = n.split()
        try:
            if z[0].isdigit():
                #CMT- tje added, print 'z' just so can show something to the console to navigate by.
                #CMT- if here, than z[0] was a digit de-noting a string to be parsed below
                print z
                if z[0] != str((int(z[1].split('.')[3])-100)):
                    print "\n Fault Ip combination: " + z[0] + "  " + z[1] + " is in " + temp[-3]
            else:
                temp.append(' '.join(z))
        except IndexError:
            pass
    return tn
    
    
#inputList = sys.argv
HOST = '10.13.138.101'
loginToDut(HOST)