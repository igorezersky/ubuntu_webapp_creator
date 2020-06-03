Ubuntu WebApp Creator
=====================

Ubuntu WebApp Creator allows creating Ubuntu desktop applications from any website.

It's a simple command-line tool written on Python based on [`imagemagick`](https://imagemagick.org/index.php) and [`nativefier`](https://github.com/jiahaog/nativefier)

Requirements
------------

- [Ubuntu 16.04+](https://ubuntu.com/)

- [Python 3.6+](https://www.python.org/)

- [Node.js 8+](https://nodejs.org/)

- Admin privileges (required for dependencies installation)

Installation
----------

```shell script
wget https://github.com/igorezersky/ubuntu_webapp_creator/archive/master.zip
unzip master.zip
cd ubuntu_webapp_creator-master
source install.sh
```

Usage
-----

```text
usage: ubuntu_webapp_creator.py [-h] --config CONFIG

optional arguments:
  -h, --help       show this help message and exit
  --config CONFIG  Path to config.yml file. Required fields: ["app_dir",
                   "name", "url", "icon"]
```

Check [`nativefier` docs](https://github.com/jiahaog/nativefier/blob/master/docs/api.md#command-line) for more details.

config.yml example
------------------

```yaml
app_dir: /home/user/Software/Outlook
name: Outlook
url: https://outlook.office.com/mail
icon: /home/user/Pictures/outlook.png
```

License
-------

[MIT License](https://github.com/igorezersky/ubuntu_webapp_creator/blob/master/LICENSE)
