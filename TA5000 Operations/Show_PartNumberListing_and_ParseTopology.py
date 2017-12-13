import telnetlib

#CMT-define a list
part_num_list = list()
result = str()
ta5k_ip = '10.13.138.101'
tn = telnetlib.Telnet()


#CMT-connect to shelf
def login(ip):
    tn.open(ip)
def login_enable():
    tn.read_until('Username:')
    tn.write('ADMIN\n')
    tn.read_until('Password:')
    tn.write('PASSWORD\n')
    tn.read_until('>')
    tn.write('enable\n')
    tn.read_until('#')
    tn.write('term len 0\n')
    tn.read_until('#')
    tn.write('show version\n')
    #CMT-result = node1.read_until('#')
    #CMT-return result

def show_version(result):
    tn.write('show version\n')
    result = tn.read_until('#')
    return result

def show_topology(result):
    tn.write("show topology tree detail\r")
    result = tn.read_until("#")

#CMT-MAIN - connect to shelf
login(ta5k_ip)
login_enable()

#**********************************************************************************
#CMT-SHOW VERSION AND SPLIT INTO LINES
#CMT-call show_version() and save to a variable
show_version = show_version(result)
#CMT-make a 'string array' or 'list' of the 'show version' output at each of the line-breaks
#CMT-eg a = ['line1', 'line2'], or,
#CMT-eg  a = ['show version\r', '1/1 TA5000 1187550E1 \r', '  Part Number  : 1187550E1\r', ....]
show_version = show_version.split("\n")

#CMT-display the (long) string-array (i.e. 'list')
print show_version

for line in show_version:
    #CMT-if 'print line', then output should be that of original 'show version'
	#CMT-print line
	#CMT-Find each line with the keyword 'Part Number'
	if 'Part Number' in line:
        #CMT-line will look like this - '  Part Number                     : 1187550E1\r'
		#CMT-For that line, Make a new 'string array'('list') extracting just the P/N (the 3rd value)
        #CMT-from ['Part', 'Number', ':', '1187080L1']
		part_num_list.append(line.split()[3])

print part_num_list
		
#CMT-print out each item (the part numbers) in the list
print "here be a list of ye part numbers:"
for part_num in part_num_list:
	print part_num
#**********************************************************************************

#**********************************************************************************
#CMT-Show and Parse Topology
show_topology = show_topology(result)
    # x=tn.read_until("#")
    # temp = []
y = show_topology.split("\n")
for n in y:
    z = n.split()
    try:
        if z[0].isdigit():
            if z[0] != str((int(z[1].split('.')[3])-100)):
                print "\n Fault Ip combination: " + z[0] + "  " + z[1] + " is in " + temp[-3]
        else:
            temp.append(' '.join(z))
    except IndexError:
        pass
return tn