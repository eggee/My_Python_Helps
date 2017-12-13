import telnetlib

# define a list
part_num_list = list()
result = str()
ta5k_ip = '10.13.138.101'
tn = telnetlib.Telnet()
# connect to shelf
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
    # tn.write('show version\n')
    # result = node1.read_until('#')
    # return result
def show_system_inventory():
    tn.write('show system inventory\n')
    result = tn.read_until('#')
    return result

# MAIN - connect to shelf
login(ta5k_ip)
login_enable()

inventory = show_system_inventory()
print inventory
