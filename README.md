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

### dev_odoo.py man page
```bash
options:
  -h, --help            show this help message and exit
  -v {13,16,17}, --version {13,16,17}
                        odoo version(default is 17)
  -p {will,be,show,the,project_list,of,project,root}, --project {will,be,show,the,project_list,of,project,root}
                        Odoo Project file name
  -u UPGRADE, --upgrade UPGRADE
                        To upgrade modules
  -d DATABASE, --database DATABASE
                        Select the database
  -s, --shell           Odoo Shell

```
***

### Bash Shell (Linux)
```bash
    $ chmod +x dev_odoo/dev_odoo.py
    run server in odoo 17 version
    $ ./dev_odoo.py -p project_name -u upgrade_module 
    odoo shell 
    $ ./dev_odoo.py -v version -p project_name -d database -u upgrade_module -s
```
***
### Python
```bash
    $ python3 dev_odoo.py -v version -p project_name
```
