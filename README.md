# ODOO DEVELOPER SHORTCUT
___
## Description

Odoo Manager is a Python-based tool designed to manage Odoo projects, including version management, database selection, and module upgrades. The tool leverages argparse for command-line argument parsing and argcomplete for autocompletion. The tool is designed to work on Linux and MacOS systems.
### Features
- [x] __Version Management__: Automatically detects available versions on the machine.
- [x] __Database Selection__: List of databases for a specific depending on the Odoo version.
- [x] __Module Upgrade__: Provides autocompletion for available modules in a project.

___
## Requirements
- Python 3.6+
- argcomplete
- PostgreSQL

## Installation
```bash
$ git clone https://github.com/Htetmyat-GCA/dev_odoo.git
$ sudo apt install python-argcomplete
$ cd dev_odoo
$ chmod +x setup.sh
$ ./setup.sh
```
## Configuration
Update the [`settings.py `](settings.py) file with your Odoo specific paths and environment settings:
```python
# settings.py
import pathlib
import os

USER = os.getenv('USER')

HOME = os.getenv('HOME')

ODOO_ROOT = pathlib.Path(HOME, '.odoo')

PROJECTS_DIR = pathlib.Path(HOME, 'Projects/Odoo')

PYTHON_ENV = pathlib.Path(HOME, 'pyenv')

ENV_PREFIX = 'env'

ENV_POSTFIX = None

ODOO_VERSION_PREFIX = 'odoo'

ODOO_VERSION_POSTFIX = None

SHELL = os.getenv('SHELL')

```
___
### Default Project Structure
The developer can customize his/her project structure by changing the settings.py
```
ODOO DEFAUT ROOT            :   /home/username/.odoo/
DEFAULT Projects DIR        :   /home/username/Projects/Odoo/{project_name}
DEFAULT Python Env Path     :   /home/username/pyenv/env{version}
Odoo Configuration file     :   /home/username/Projects/Odoo/{project_name}/config/odoo{version}.conf
```
___
### Usage
```bash
$ ./run -v <version> -p <project> [-d <database>] [-u <module>] [-s]
```
### Options

```bash
options:
  -h, --help            show this help message and exit
  -v {11,13,16,17}      Odoo Version (default == 17)
  -p {will,show,the,list,of,projects}
                        Project Directories
  -u MODULE             To Upgrade Module
  -d DATABASE           Select the Database
  -s                    Odoo Shell


```
___
## Example
### Linux and MacOS
```bash
    $ dev_odoo/run -p project_[tab] -u upgrade_module # to run default odoo version
    $ dev_odoo/run -v ver[tab] -p project_name -d database -u upgrade_module -s # odoo shell
```
### Windows
Autocompletation is not natively supported on Windows. You can still run the Odoo Manager tool, but you will need to manually type the arguments without autocomplete assistance.
```bash
    $ python3 dev_odoo/run -v version -p project_name -d database -u upgrade_module -s 
    $ python3 dev_odoo/run -v version -p project_name -u upgrade_module 
```
