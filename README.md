# Shortcut for odoo-bin
    Automatic run the odoo projects for various version for developer 
    This app is written with python.

## Description
### Project Infrastructure
```html
Odoo DEFAULT Project DIR    :   /var/lib/odoo/o_{version}
Projects DIR                :   /home/username/Projects/Odoo/{project_name}
Python Environment Path     :   /home/username/Env/
Odoo Configuration file     :   /home/username/Projects/Odoo/project_name/config/odoo{version}.conf
```

```bash
    Usage: odoo_start.py -v version -n project_name
```
Currently, This program is not satisfied for all structures. Anyone can edit. The purpose of the program is that a project 
may have different versions, for examples, version change from 13 to 17, etc. So the developer should restart the server resetting the server. 
The program can reduce your time but your infrastructure should follow as shown at **Project Infrastructure**.