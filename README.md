# SubShot

SubShot is a python tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers and bug hunters to collect and gather subdomains for a particular domain, apply HTTP & HTTPS Probing to filter working URLs and also capture a screenshot of every website.

The screenshot utility uses Selenium's Chrome Headless driver.

Sublist3r enumerates subdomains using the following search engines: 
> Google, Yahoo, Bing, Baidu and Ask. 
> Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS.

Libraries used: 
> PyQt5, Selenium, argparse, dnspython, requests

Based on Python 3.8.3 and compiled using python's own virtualenv.

To install dependencies:

~~~
sudo pacman -Syu tcpdump
sudo pip install PyQt5 scapy psutil
~~~

To run SubShot:

1. Using source file:
~~~
python3 run.py
~~~

2. Using Windows executable:
~~~
!!! Coming Soon !!!
~~~