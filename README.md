# SubShot

This tool provides the following functionalities:
* Subdomain enumeration using OSINT
* HTTP & HTTPS probing
* Hostile subdomain takeover possibility
* Screenshotting subdomains using Selenium's Chrome Headless driver

SubShot enumerates subdomains using the following search engines and websites: 
> Google, Yahoo, Bing, Baidu, Ask, Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS.

## Installation

To install dependencies:

~~~
pip install pyqt5 argparse requests dnspython chromedriver selenium webdriver_manager
~~~

You'll also need ruby which can be installed using:

~~~
sudo apt install ruby-full          // Debian/Ubuntu-based distros
sudo pacman -S ruby                 // Arch-based distros
~~~

To run SubShot:

1. Using source file: `python3 main.py`

2. Using executable: `Coming Soon`

## Customizaton

For changing the Qt theme of the application on Gnome, install kvantum:

~~~
sudo apt install qt5-style-kvantum qt5-style-kvantum-themes
~~~

Then change to the desired theme. However, you'll need to export the path to the qt platform plugin to actually use the theme.

To apply the Qt theme to the application, you can use this command in the terminal for temporary use or export(paste) it to .bashrc:

~~~
export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins
~~~

## Troubleshooting

If you get the error: `Fix “qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.” Qt Creator`

~~~
sudo apt-get install libxcb-xinerama0
~~~
