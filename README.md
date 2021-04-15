# Gngr_network_tools
It is a tool for Windows operating systems that offer features such as "Show interface, Port scanner, network scanner, tracing route to ip, show registered wi-fi(s) and password" 


![n1](https://user-images.githubusercontent.com/71177413/114878553-09b9d500-9e09-11eb-8b51-16ea77ea7604.JPG)

Kaynak kodun derlenmiş ('exe' uzantılı) dosya hali https://drive.google.com/file/d/1Lf9jBqUvgf1N0CKR8QHuUeG8uiWPkcUQ/view?usp=sharing adresine konulmuştur. Rar şifresi "Gngr-V1.0".

Kaynak kodun derlenmiş çalışır hali ile ilgili video https://www.youtube.com/watch?v=1Tyg7-YywCE adresinden izlenebilir.


Gereksinimler
------------------------
Gerekli kütüphaneler: scapy, networkscan, pyinstaller

Yüklemek için;

>>pip install scapy

>>pip install networkscan

>>pip install pyinstaller

"pyinstaller" kodu tek parça çalıştırılabilir dosya haline getirmek için kullanılacak.


Kaynak Kod
--------------
"Gngr network tools" kodlanırken "Python 3.8.5" kullanıldı. Ana dosya, "Gngr_network_tools.py" adlı dosyadır. Bu dosyanın ihtiya. duyacağı diğer kütüphane dosyaları "lib" adlı klasoru içine knulmuştur. Program derlendikten sonra çalışacak bilgisayarda herhangi bir kütüphaneye ihtiyaç duymamaktadır.


Kaynak Kodu Derlemek İçin
--------------------------
>> pyinstaller --onefile --icon=Gngr_network.ico Gngr_network_tools.py


Derlenmiş Kodun Çalışmasına Ait Görüntüler
------------------------------------------
[1 - show Interface(s)]

![n1](https://user-images.githubusercontent.com/71177413/114880810-13443c80-9e0b-11eb-8d49-616c8afd451d.jpg)



[2 - ip port scanner ]

![n2](https://user-images.githubusercontent.com/71177413/114880898-2b1bc080-9e0b-11eb-96d0-3b8d68e23e11.jpg)



[3 - network scanner ]

![n3](https://user-images.githubusercontent.com/71177413/114880992-44247180-9e0b-11eb-8001-e2a351fc67f6.jpg)



[4 - Tracing route to ip ]

![n4](https://user-images.githubusercontent.com/71177413/114881256-80f06880-9e0b-11eb-9983-754ff615037e.jpg)



[5- Show registered wi-fi(s) and password(s)]

![n5](https://user-images.githubusercontent.com/71177413/114881354-99608300-9e0b-11eb-9947-1353d3fa9624.jpg)



Yasal Uyarı
------------------
Eğitim amacıyla hazırlanmıştır.

Kullanıcıların bazı kullanım şekilleri suça sebep olabilir.

Olumsuz durumlarla karşılaşmamak için "Yasal_Uyarı.txt" dosyasını okuyunuz.
