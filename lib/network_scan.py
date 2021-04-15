############################################################################
#
#   network_scan.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import networkscan

def func_networkscan():
    #
    title = '\t{:^40}'.format('Network Scanner')
    title_line = '\t{:^40}'.format('-'*16)
    #
    print()
    print(title)
    print(title_line)
    print()
    #
    host = input('\t[Example: 192.168.1.0/24] ?: ')
    #
    try:
        my_scan = networkscan.Networkscan(host.strip())
        network = host.split(sep='/')
        print()
        print("\tNetwork Address         : " + network[0])
        print("\tPrefix                  : " + network[1])
        print("\tNumber of hosts to scan : " + str(my_scan.nbr_host))
        #
        print()
        print("\tScanning hosts...")
        print("\tPlease wait!")
        print()
        #
        my_scan.run()
        #
        if len(my_scan.list_of_hosts_found) > 0:
            print('\t    IP(S)    ')
            print('\t--------------')
            for ip in my_scan.list_of_hosts_found:
                txt_tmp = '\t{}'.format(ip)
                print(txt_tmp)
        else:
            print('\tNo IP address was found.')
    except:
        print('\tWrong input. Example Network Address "192.168.1.0/24"')

