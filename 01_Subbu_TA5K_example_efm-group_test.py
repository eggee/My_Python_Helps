#Example test from Subbu
from taut_ta5k.communication.ta5k_telnet import Ta5kTelnet
#C:\Python27\Lib\site-packages\taut_ta5k\communication
setup_dict = {
    'ip': '10.49.239.3'
}

param_dict = {
    'shelf': '1',
    'slot': '14',
    'group_id': '2',
    'admin_state': 'enable',
    'alias': 'DUMMY',
    'rate_control': 'disable',
    'up_stream_rate': '10',
    'down_stream_rate': '10',
    'xcv_link_treshold': 'le-5',
    'xcv_link_removal': 'disable',
    'sub_host_ip': '10.49.235.150',
}

tn = Ta5kTelnet()
tn.connect(setup_dict['ip'], 'ta5k', timeout=1100)

tn.efm_group_create(param_dict)  # configures EFM-Group interface 1/14/2

efm_dict = tn.efm_group_config_get(param_dict)   # getting the EFM-Group interface 1/14/2 parameters

ret_dict = tn.efm_group_status_get(param_dict)   # getting the status of EFM-Group interface 1/14/2

if ret_dict['state'] == u'IS':
    print 'efm-group %s/%s/%s is IS and running' %(param_dict['shelf'],param_dict['slot'],param_dict['group_id'])


tn.close_all_connections()

