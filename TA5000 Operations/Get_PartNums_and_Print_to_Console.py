import telnetlib

part_num_list = list()
result = str()

tn = telnetlib.Telnet('10.13.138.101')
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
result = tn.read_until('#')


#make a 'string array' or 'list' of the 'show version' output at each of the line-breaks
#eg a = ['line1', 'line2'], or,
#eg  a = ['show version\r', '1/1 TA5000 1187550E1 \r', '  Part Number  : 1187550E1\r', ....]
show_version = result.split("\n")

#display the (long) string-array (i.e. 'list')
print show_version

for line in show_version:
    #if 'print line', then output should be that of original 'show version'
	#print line
	#Find each line with the keyword 'Part Number'
	if 'Part Number' in line:
        #line will look like this - '  Part Number                     : 1187550E1\r'
		#For that line, Make a new 'string array'('list') extracting just the P/N (the 3rd value)
        #from ['Part', 'Number', ':', '1187080L1']
		part_num_list.append(line.split()[3])

print part_num_list
		
#print out each item (the part numbers) in the list
print "here be a list of ye part numbers:"
for part_num in part_num_list:
	print part_num