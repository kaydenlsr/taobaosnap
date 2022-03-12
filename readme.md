============================================================================
Taobaosnap script - Taobao panic buying script
============================================================================

Taobaosnap is a completely open tool, which is used to buy goods in seconds on Taobao. This is a project created with python, using selenium and requests module to achieve login and snap-up. The project integrates network script ideas and improves them, using selenium to realize remote login and login verification problems. Use requests for snapping without rendering, reducing the time required for access and snapping. Use the countdown idea to realize automatic snapping when the time is up. The number of times of use is set, which is convenient for reading and analyzing the program log after the snap-up is over.

 The Taobaosnap distribution is available from:
https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files

Taobaosnap should run on any platform that supports 
Python (http://www.python.org)

NOTE: For precautions please refer to the guide at the link below

    https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/master/readme.md

Compatibility
Windows:
Windows 95
Windows 98
Windows ME
Windows 2000
Windows 2003
Windows XP
Windows Vista
Windows 7
Windows 8
Windows 8.1
Windows 10
Server version:
WindowsServer2003
WindowsServer2008
WindowsServer2012
WindowsServer2016
Mobile Edition:
WindowsMobile
WindowsPhone
Windows10Mobile

Note: This solution is currently not compatible with linux systems and mac systems

Taobaosnap does not provide memory sample collection capabilities. If you need advice on suitable
For solutions, please contact us by:
WeChat Official Accounts:红客突击队

Example Data
===========

If you want to give Taobaosnap a try, you can download exemplar
memory images from the following url:

   https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files/master/example

Author
=============
仰望·星空
K龙
Charles

Mailing Lists
=============

Mailing lists to support the users and developers of Taobaosnap
can be found at the following address:

   kaydenlsr@163.com
   1015468607@qq.com
   hhsc_2019@163.com

Contact
=======
For information or requests, contact:

Taobaosnap Foundation

Web: http://hsc_2019.site
     http://hsc_2019.club
     
Email: hsc_2019@163.com

INS: @honkersecuritycommando

WeChat Official Accounts:红客突击队

Micro-blog:@红客突击队

Requirements
===========
- Python 3.10 or later, but not 3.9. http://www.python.org

Python module library necessary dependencies
-requests
-urllib
-pyttsx3
-prettytable
-argparse
-elenium

Necessary drive
chromedriver.exe https://registry.npmmirror.com/binary.html?path=chromedriver/

Some plugins may have other requirements which can be found at:
    https://pypi.tuna.tsinghua.edu.cn/simple

Quick Start
===========
1. Unpack the latest version of taobaosnap from
    https://kaydenlsr.coding.net/public/taobaosnap/taobaosnap/git/files
   
2. Install related dependencies
    pip install [modules]

3. Download the chrome browser and the corresponding chromedriver and place them in the python.exe directory.
The project provides chromedriver version = 99.0.4844.51

4. run cmd and run ' python taobaosnap.py --interval [time interval] --time [Starting time] -l [frequency] '

   Example:

$ python taobaosnap.py --interval 0.1 --time 15:59:59:90000000 -l 5

   Help:

   usage : python taobaosnap.py
       --time        Buying time.
       --interval    Buying time interval.
       --l           Buying frequency.


Version
===========
Last update 2022.3.12 by K龙 version=3.1.5

Disclaimer 
===========
This project is open source and aims to learn from each other. Use of this program in violation of laws and regulations is prohibited. The author has nothing to do with any consequences or related regulations caused by the use of this program.