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
This program isn't good enough for all structures right now. The program's goal is to allow projects to have many versions; for instance, a project may have a version shift from 13 to 17, etc. Thus, the server was reset and restarted by the developer. The program can reduce your time but your project structure should follow as shown at Project Infrastructure.