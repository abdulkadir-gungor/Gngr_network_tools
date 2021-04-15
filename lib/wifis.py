############################################################################
#
#   wifis.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import subprocess

def func_wifis():
    #
    names = []
    keys = []
    #
    cmd_command_1    = 'netsh wlan show profiles'
    res_command_1    = subprocess.Popen(cmd_command_1, stdout=subprocess.PIPE)
    output_command_1 = res_command_1.stdout.read()
    txt_command_1    = output_command_1.decode(encoding='utf-8')
    list_command_1   = txt_command_1.split(sep='\r\n')
    #
    for name in list_command_1:
        if -1 != name.find('All User Profile'):
            name_list = name.split(sep=':')
            names.append(name_list[1].strip())
    #
    for key in names:
        cmd_command_2  = 'netsh wlan show profile {} key=CLEAR'.format(key)
        res_command_2  = subprocess.Popen(cmd_command_2, stdout=subprocess.PIPE)
        #
        output_command_2 = res_command_2.stdout.read()
        txt_command_2    = output_command_2.decode(encoding='utf-8')
        list_command_2   = txt_command_2.split(sep='\r\n')
        for key in list_command_2:
            if -1 != key.find('Key Content'):
                key_list = key.split(sep=':')
                keys.append(key_list[1].strip())
    #
    title      = '\t{}'.format('All Registered WI-FI(s) and Password(s)')
    title_line = '\t{}'.format('---------------------------------------')
    print()
    print(title)
    print(title_line)
    print()
    if len(names) > 0:
        for ii in range(0,len(names),1):
            txt_tmp = '\t{:<20} : "{}"'.format(names[ii], keys[ii])
            print(txt_tmp)

