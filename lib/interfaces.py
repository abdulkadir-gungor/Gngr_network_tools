############################################################################
#
#   interfaces.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from scapy.all import get_windows_if_list

def func_interfaces():
    winList = get_windows_if_list()
    if len(winList):
        title = '{:>62}'.format('Windows Interface(s)')
        title_header =  '\t{:^30}   {:^24}   {:^30}'.format('Name', 'MAC', 'Description')
        title_line = '\t{:>30}   {:>24}   {:>30}'.format('-'*30,'-'*24,'-'*30)
        print()
        print(title)
        print()
        print(title_header)
        print(title_line)
        for winMac in winList:
            tmp_write = '\t{:<30}   {:^24}   {:<30}'.format(winMac['name'], winMac['mac'], winMac['description'])
            print(tmp_write)
    else:
        title = '{:>62}'.format('Windows Interface(s)')
        text_tmp = '\tNo interfaces were found!'
        print()
        print(title)
        print()
        print(text_tmp)
