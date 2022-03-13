#Taobaosnap

=================================================<br>
Taobaosnap script - Taobao panic buying script<br>
=================================================<br>
Author 仰望·星空、K龙、Charles<br>
=================================================<br>

##Taobaosnap
Taobaosnap is a completely open tool, which is used to buy goods in seconds on Taobao. This is a project created with python, using selenium and requests module to achieve login and snap-up. The project integrates network script ideas and improves them, using selenium to realize remote login and login verification problems. Use requests for snapping without rendering, reducing the time required for access and snapping. Use the countdown idea to realize automatic snapping when the time is up. The number of times of use is set, which is convenient for reading and analyzing the program log after the snap-up is over.(This description is for versions higher than 3.1.5)

 The Taobaosnap distribution is available from:
https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files

Taobaosnap should run on any platform that supports 
Python (http://www.python.org)

NOTE: For precautions please refer to the guide at the link below

    https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/master/readme.md


##Compatibility(version=1.1.15,2.1.5,3.1.5)
Windows:<br>
Windows 95<br>
Windows 98<br>
Windows ME<br>
Windows 2000<br>
Windows 2003<br>
Windows XP<br>
Windows Vista<br>
Windows 7<br>
Windows 8<br>
Windows 8.1<br>
Windows 10<br>
Server version:<br>
WindowsServer2003<br>
WindowsServer2008<br>
WindowsServer2012<br>
WindowsServer2016<br>
Mobile Edition:<br>
WindowsMobile<br>
WindowsPhone<br>
Windows10Mobile<br>

Compatibility(version=1.1.15,3.3.5-linux)
Asianux4<br>
Asianux Server 3<br>
Centos 8 64-bit<br>
Centos5 and earlier 64-bit centos5 and later<br>
Debian 5/6/7.x/8.x/9.x/10.x<br>
Fedora<br>
Mardriva Linux<br>
Novell Linux Desktop 9<br>
OpenSUSE<br>
Oracle Linux 6/7/8<br>
Oracle Linux 5 earlier 64-bit centos5 and later<br>
Red Hat Enterprise Linux 2/3/4/5/6/7/8<br>
Sun Java Desktop System<br>
SUSE Linux Enterprise 7/8/9/10/11/12/15<br>
ITurbolinux 64-bit<br>
ubuntu 64 bit ubuntu<br>
Mware Photon Os 64-bit Other Linux 5. Kernel 64-bit Other Linux 5.x Kernel<br>
Other Linux 4.x Kernels 64-bit Other Linux 4.x Kernels<br>
Other Linux 3.x Kernel 64-bit Other Linux 3.x Kernel<br>
Other Linux 2.6.x Kernel 64-bit Other Linux 2.6.x Kernel<br>
Other Lirux 2.4.x Kernel 64-bit Kei He Linux 2.4.x Kernel<br>
Other Linux 2.2.x kernel pensUSE 64 bit<br>

macOS Big Sur<br>
macOS Catalina<br>
macOS Mojave<br>
macOS High Sierra<br>
macOS Sierra<br>
OS X El Capitan<br>
OS X Yosemite<br>
OS X Mavericks<br>
OS X Mountain Lion<br>
OS X Lion<br>
Mac OS X Snow Leopard<br>
Mac OS X Leopard<br>
Mac OS X Tiger<br>
Mac OS X Panther<br>
Mac OS X Jaguar<br>
Mac OS X Puma<br>
Mac OS X Cheetah<br>

Note: This solution is currently not compatible with linux systems and mac systems

Taobaosnap does not provide memory sample collection capabilities. If you need advice on suitable
For solutions, please contact us by:
WeChat Official Accounts:红客突击队

Example Data
=============

If you want to give Taobaosnap a try, you can download exemplar
memory images from the following url:

   https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/master/example

Author
=============
仰望·星空<br>
K龙<br>
Charles<br>

Mailing Lists
=============

Mailing lists to support the users and developers of Taobaosnap
can be found at the following address:<br>

   kaydenlsr@163.com<br>
   1015468607@qq.com<br>
   hhsc_2019@163.com<br>

Contact
=============
For information or requests, contact:

Taobaosnap Foundation

Web: http://hsc_2019.site<br>
     http://hsc_2019.club<br>
     
Email: hsc_2019@163.com

INS: @honkersecuritycommando

WeChat Official Accounts:红客突击队

Micro-blog:@红客突击队

Requirements
=============
- Python 3.10 or later, but not 3.9. http://www.python.org

Python module library necessary dependencies
-requests
-urllib
-pyttsx3
-prettytable
-argparse
-selenium

Necessary drive
chromedriver.exe https://registry.npmmirror.com/binary.html?path=chromedriver/

Some plugins may have other requirements which can be found at:
    https://pypi.tuna.tsinghua.edu.cn/simple

Quick Start(version=1.0.5)
=============
1. Unpack the latest version of taobaosnap from
    https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/taobaosnap-1.0.5
   
2. Install related dependencies
    pip install [modules]

3. Change the time value of time_seckill to panic buying time at line 73 of the program

4. run cmd and run 'python taobaosnap.py --interval [time interval]'

    Example:

        $ python taobaosnap-1.0.5.py --interval 0.1

    Help:

    usage : python taobaosnap.py
        --interval    Buying time interval.

Quick Start(version=2.0.3)
=============
1. Unpack the latest version of taobaosnap from
    https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/taobaosnap-2.0.3
   
2. Install related dependencies
    pip install [modules]

3. Change the time value of times to panic buying time at line 49 of the program

4. run cmd and run 'python taobaosnap-2.0.3.py'

Quick Start(version=3.1.5)
=============
1. Unpack the latest version of taobaosnap from
    https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/taobaosnap-3.1.5
   
2. Install related dependencies
    pip install [modules]

3. Download the chrome browser and the corresponding chromedriver and place them in the python.exe directory.
The project provides chromedriver version = 99.0.4844.51

4. run cmd and run ' python taobaosnap.py --interval [time interval] --time [Starting time] --l [frequency] '

    Example:

        $ python taobaosnap.py --interval 0.1 --time 15:59:59:90000000 --l 5

    Help:

    usage : python taobaosnap-3.1.5.py
        --time        Buying time and format: 00:00:00:00000000.
        -interval    Buying time interval.
        --l           Buying frequency.

Quick Start(version=3.2.5)
=============
1. Unpack the latest version of taobaosnap from
    https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/taobaosnap-3.2.5
   
2. Install related dependencies
    pip install [modules]

3. Download the chrome browser and the corresponding chromedriver and place them in the python.exe directory.
The project provides chromedriver version = 99.0.4844.51

4. run taobaosnap-3.2.5.py
Enter as prompted:
--interval [time interval] --time [Starting time] --l [frequency] '

    Example:
        --interval 0.1 --time 15:59:59:90000000 --l 5

    Help:

    usage : python taobaosnap.py
        --time        Buying time and format: 00:00:00:00000000.
        --interval    Buying time interval.
        --l           Buying frequency.

Quick Start(version=3.3.5-linux)
=============
1. Unpack the latest version of taobaosnap from
    https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/taobaosnap-3.3.5-linux
   
2. Install related dependencies
    pip install [modules]

3. run taobaosnap-linux-linux.py
Enter as prompted:
--interval [time interval] --time [Starting time] --l [frequency] '

    Example:
        --interval 0.1 --time 15:59:59:90000000 --l 5

    Help:

    usage : python taobaosnap.py
        --time        Buying time and format: 00:00:00:00000000.
        --interval    Buying time interval.
        --l           Buying frequency.
        
About version
=============
2022.3.12 by K龙 version=3.1.5(windows,linux,mac)<br>
2022.3.13 by K龙 version=1.0.5(windows)<br>
2022.3.13 by K龙 version=2.0.3(windows)<br>
2022.3.13 by K龙 version=3.2.5(windows)<br>
2022.3.13 by K龙 version=3.3.5-linux(linux)<br>
Last update 2022.3.13 13:25 by K龙 version=3.3.5-linux(linux)<br>

Release Notes
=============
Simplified operation

Disclaimer 
=============
This project is open source and aims to learn from each other. Use of this program in violation of laws and regulations is prohibited. The author has nothing to do with any consequences or related regulations caused by the use of this program.