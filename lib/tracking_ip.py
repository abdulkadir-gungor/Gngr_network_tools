############################################################################
#
#   tracert.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import subprocess

def func_tracert():
    #
    print('')
    print('\t   Tracing route to ip   ')
    print('\t-------------------------')
    print('')
    print('\tEnter Ip or hostname!')
    print('\t[Example:192.168.1.1] or')
    host = input('\t[Example:www.google.com] ?: ')
    print()
    print("\tTracing route to ip...")
    print("\tPlease wait!")
    print()
    if host is not None:
        if host.strip():
            commad = f'tracert {host}'
            result = subprocess.call(commad)
            print(result)
        else:
            print("\tPlease enter valid content!")
    else:
        print("\tPlease enter valid content!")
