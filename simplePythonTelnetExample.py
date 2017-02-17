import os
import time
import sys
import telnetlib

#connect to shelf
tn = telnetlib.Telnet('10.213.253.33')
#login
tn.read_until('Username:')
tn.write('ADMIN\n')
tn.read_until('Password:')
tn.write('PASSWORD\n')
#look for the prompt
tn.read_until('>')
tn.write('enable\n')
tn.read_until('#')
tn.write('term len 0\n')
tn.read_until('#')
tn.write('show version\n')
a = tn.read_until('#')

print a
