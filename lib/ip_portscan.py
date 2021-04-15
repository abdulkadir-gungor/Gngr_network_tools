############################################################################
#
#   ip_portscan.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import socket
from time import strftime

#
def func_ip_portscan():
    #
    ports = []
    #
    print()
    print('\t   Ip Port Scannner   ')
    print('\t-----------------------')
    print()
    print('\t[Example: 192.168.1.1] (It scans 1 to 65535 ports of the entered ip address.)')
    print('\t[Example: 192.168.1.1 Port] (It just scans the given port of the ip address.)')
    print('\t[Example: 192.168.1.1 StartPort EndPort]')
    print()
    print('\t[Example: www.google.com] (It scans 1 to 65535 ports of the entered ip address.)')
    print('\t[Example: www.google.com Port] (It just scans the given port of the ip address.)')
    print('\t[Example: www.google.com StartPort EndPort]')
    print()
    entered = input('\t[Enter] ?: ')
    print()
    #
    if entered.strip() != '':
        entered_tmp =  entered.strip()
        entered_list = entered_tmp.split(sep=' ')
        #
        if len(entered_list) == 1:
            try:
                target_ip = socket.gethostbyname( entered_list[0].strip() )
                #
                print('\t'+("-" * 50) )
                print("\tScanning Target     : " + target_ip)
                print("\tScanning Ports      : 1 - 65535" )
                print("\tScanning started at : " + strftime("%Y-%m-%d %H:%M:%S") )
                print('\t'+("-" * 50))
                print()
                print("\tScanning ports...")
                print("\tPlease wait!")
                print()
                #
                for port in range(1, 65536):
                    #
                    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = tmp_socket.connect_ex((target_ip, port))
                    if result == 0:
                        ports.append(port)
                        print("\tPort {} is open".format(port))
                    else:
                        print(f"\t{port} - *")
                    tmp_socket.close()
            except socket.gaierror:
                print("\tHostname Could Not Be Resolved !!!!")
                print()
            except socket.error:
                print("\tServer not responding !!!!")
                print()
            except:
                print("\tAn error occurred")
            #
            if len(ports) > 0:
                print('')
                print('')
                print('')
                print('\tOpen Ports')
                print('\t----------')
                for port_tmp in ports:
                    print(f'\t  {str(port_tmp)}')
                print()
        #
        elif len(entered_list) == 2:
            try:
                #
                target_ip = socket.gethostbyname( entered_list[0].strip() )
                #
                print('\t' + ("-" * 50))
                print("\tScanning Target     : " + target_ip )
                print("\tScanning Port       : " + entered_list[1].strip() )
                print("\tScanning started at : " + strftime("%Y-%m-%d %H:%M:%S"))
                print('\t' + ("-" * 50))
                print()
                print("\tScanning ports...")
                print("\tPlease wait!")
                print()

                #
                tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = tmp_socket.connect_ex((target_ip, int(entered_list[1].strip()) ))
                if result == 0:
                    print("\tPort {} is open".format( int(entered_list[1].strip()) ))
                else:
                    print(f"\t{str(entered_list[1].strip())} - *")
                tmp_socket.close()
            except socket.gaierror:
                print("\tHostname Could Not Be Resolved !!!!")
                print()
            except socket.error:
                print("\tServer not responding !!!!")
                print()
            except:
                print("\tAn error occurred")

        elif len(entered_list) == 3:
            try:
                target_ip = socket.gethostbyname( entered_list[0].strip() )
                #
                print('\t'+("-" * 50) )
                print("\tScanning Target     : " + target_ip)
                print("\tScanning Ports      : " + str(entered_list[1].strip()) + " - " + str(entered_list[2].strip()) )
                print("\tScanning started at : " + strftime("%Y-%m-%d %H:%M:%S") )
                print('\t'+("-" * 50))
                print()
                print("\tScanning ports...")
                print("\tPlease wait!")
                print()
                #
                for port in range( int(entered_list[1].strip()), int(entered_list[2].strip())+1 ):
                    #
                    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = tmp_socket.connect_ex((target_ip, port))
                    if result == 0:
                        ports.append(port)
                        print("\tPort {} is open".format(port))
                    else:
                        print(f"\t{port} - *")
                    tmp_socket.close()
            except socket.gaierror:
                print("\tHostname Could Not Be Resolved !!!!")
                print()
            except socket.error:
                print("\tServer not responding !!!!")
                print()
            except:
                print("\tAn error occurred")
            #
            if len(ports) > 0:
                print('')
                print('')
                print('')
                print('\tOpen Ports')
                print('\t----------')
                for port_tmp in ports:
                    print(f'\t  {str(port_tmp)}')
                print()
        #
        else:
            print("\tWrong input. Please enter valid content!")
    else:
        print("\tWrong input. Please enter valid content!")