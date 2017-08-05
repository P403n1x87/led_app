## Synopsis

`led_app` is a sample IoT web application to control LEDs over the network meant to run on a Raspberry Pi running the Raspbian OS. This repository collects the code that features in [this post](https://p403n1x87.github.io/raspberry%20pi/iot/2017/07/31/intro-to-iot.html) on [The Hub of Heliopolis](https://p403n1x87.github.io/).


## Requirements

- Python 2.7
- RPi
- Apache 2
- mod_wsgi


## Installation

It is enough to clone this repository locally and configure Apache 2 as described in the post on The Hub of Heliopolis linked above. Here is just a brief summary.

Assuming that you have cloned the project in the `/home/pi/Projects/www` local folder, this is a possible minimal Apache2 site configuration.

~~~ apache
# File: led.conf
<VirtualHost *:80>
  ServerAdmin webmaster@localhost

  # Required by static data storage access (e.g. css files)
  DocumentRoot /home/pi/Projects/www

  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined

  # WSGI Configuration
  WSGIScriptAlias /led /home/pi/Projects/www/led_app/bootstrap.wsgi

  <Directory /home/pi/Projects/www/led_app>
    Require all granted
  </Directory>

</VirtualHost>
~~~

## License

GPLv3.
