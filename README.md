# Shortcut for odoo-bin
***
## Description

This program is not good enough for all structures right now. The program's goal is to allow projects to have many versions; for instance, a project may have a version shift 13 to 17, etc. Thus, the server was reset and restarted by the developer. The program can reduce your time just configure your customize setting in [```settings.py```](https://github.com/Htetmyat-GCA/dev_odoo/blob/master/settings.py)


### My Odoo Project Infrastructure
```
ODOO DEFAUT ROOT            :   /home/username/.odoo/
Projects DIR                :   /home/username/Projects/Odoo/{project_name}
Python Environment Path     :   /home/username/pyenv/
Odoo Configuration file     :   /home/username/Projects/Odoo/{project_name}/config/odoo{version}.conf

```
***

### Bash Shell (Linux)
```shell
$./dev_odoo.py -v version -p project_name
```
***
### Python Shell
```shell
$python3 dev_odoo.py -v version -p project_name
```
