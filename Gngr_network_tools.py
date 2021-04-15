############################################################################
#
#   Gngr_network_tools.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from  lib.interfaces import func_interfaces
from  lib.ip_portscan import func_ip_portscan
from  lib.network_scan import func_networkscan
from lib.tracking_ip import func_tracert
from lib.wifis import func_wifis
import os

# Ekranı Temizlemek için
def screenClear():
    print("\r\n") # Konsol dışı kullanımda ekranı temizlemek için
    # clear screen
    # ********************
    # Windows
    if os.name=='nt':
        os.system('cls')
    # Linux or MAC
    elif os.name=='posix':
        os.system('clear')
    # ********************
    print("")

# Giriş Menüsü
def menu():
    while True:
        screenClear()
        print()
        print('\t#####################################################')
        print('\t#/*************************************************\#')
        print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
        print('\t#**||                                           ||**#')
        print('\t#**||           Gngr Network Tools              ||**#')
        print('\t#**||                04/2021                    ||**#')
        print('\t#**||                                           ||**#')
        print('\t#**||       Developer: Abdulkadir GÜNGÖR        ||**#')
        print('\t#**||       (abdulkadir_gungor@outlook.com)     ||**#')
        print('\t#**||                                           ||**#')
        print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
        print('\t#\*************************************************/#')
        print('\t#####################################################')
        print()
        print()
        print('\t               MENU')
        print('\t----------------------------------------')
        print('\t1) Show interface(s)')
        print('\t2) Ip port scanner')
        print('\t3) Network scanner')
        print('\t4) Tracing route to ip')
        print('\t5) Show registered Wi-fi(s) and password(s)')
        print()
        print()
        print( '\tExit <<e>>' )
        tmp=input('\tSelection : ')
        if tmp.strip().lower() == 'e' :
            exit(0)
        elif tmp.strip().isdigit():
            slc = int(tmp.strip())
            if  slc == 1:
                screenClear()
                func_interfaces()
                print(' ')
                print(' ')
                input('\tBack <Enter> :')
            elif slc == 2:
                screenClear()
                func_ip_portscan()
                print(' ')
                print(' ')
                input('\tBack <Enter> :')
            elif slc == 3:
                screenClear()
                func_networkscan()
                print(' ')
                print(' ')
                input('\tBack <Enter> :')
            elif slc == 4:
                screenClear()
                func_tracert()
                print(' ')
                print(' ')
                input('\tBack <Enter> :')
            elif slc == 5:
                screenClear()
                func_wifis()
                print(' ')
                print(' ')
                input('\tBack <Enter> :')



if __name__ == '__main__':
    while True:
        menu()
