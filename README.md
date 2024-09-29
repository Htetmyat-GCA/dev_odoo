# ODOO DEVELOPER SHORTCUT
___
## Description

This program is good enough to run the odoo server for all structures right now. The program's goal is to allow projects to have many versions; for instance, a project may have a version shift from 13 to 17, etc. Thus, the developer **finds** the project directory, **needs to activate** the python environment that is reliable for Odoo version, then **_resets and restarts_** the server. The program can reduce your time; just configure your customized settings in [```settings.py```](settings.py)

### New Feature [28/09/2024]

It's include ___autocomplete Tab feature___ for the project name and odoo versions that are available on machine. But this feature is not supported for Windows Platform.
If __WSL__, the feature will work.

## DEFAULT ODOO Project Structure
The developer can use his/her project structure changing the settings.py
```
ODOO DEFAUT ROOT            :   /home/username/.odoo/
DEFAULT Projects DIR        :   /home/username/Projects/Odoo/{project_name}
DEFAULT Python Env Path     :   /home/username/pyenv/env{version}
Odoo Configuration file     :   /home/username/Projects/Odoo/{project_name}/config/odoo{version}.conf
```

## Man page
```bash
usage: run [-h] [-v {11,13,16,17}] -p {will,show,the,list,of,projects} [-u MODULE] [-d DATABASE] [-s]

options:
  -h, --help            show this help message and exit
  -v {11,13,16,17}      Odoo Version (default == 17)
  -p {will,show,the,list,of,projects}
                        Project Directories
  -u MODULE             To Upgrade Module
  -d DATABASE           Select the Database
  -s                    Odoo Shell


```
# Installation
## Install argcomplete
First we need to install argcomplete on the system. 
```bash
$ sudo apt update && sudo apt upgrade
$ sudo apt install python-argcomplete
```
## Setup argcomplete
***
```bash
$ dev_odoo/setup.sh
```
## Run Server
### Bash Shell (Linux / MacOS)
```bash
    $ dev_odoo/run -p project_[tab] -u upgrade_module # to run default odoo version
    $ dev_odoo/run -v ver[tab] -p project_name -d database -u upgrade_module -s # odoo shell
```
***
### Python and Windows users
```bash
    $ python3 dev_odoo/run -v version -p project_name -d database -u upgrade_module -s 
    $ python3 dev_odoo/run -v version -p project_name -u upgrade_module 
```
