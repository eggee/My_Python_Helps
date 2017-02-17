#define a list
part_num_list = list()
result = str()

f = open('C:\Tim\SecureCRT Logs\CLI-N (16)-10.13.138.116-date-09-07-time-1352.log','r')

#display the (long) string-array (i.e. 'list')
print f

for line in f:
    #if 'print line', then output should be that of original 'show version'
	#print line
	#Find each line with the keyword 'Part Number'
	if '64:68' in line:
        #line will look like this - '  Part Number                     : 1187550E1\r'
		#For that line, Make a new 'string array'('list') extracting just the P/N (the 3rd value)
        #from ['Part', 'Number', ':', '1187080L1']
		part_num_list.append(line.split()[2])

mylist = list(set(part_num_list))
print len(mylist)

		
#print out each item (the part numbers) in the list
print "here be a list of ye part numbers:"
for mac in mylist:
	print mac