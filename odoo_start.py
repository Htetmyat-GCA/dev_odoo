#!/usr/bin/python3

import argparse
import os
import subprocess
import sys
import re

description = '''
Start the odoo server
    Project Infrastructure: 
    Odoo DEFAULT Projects DIR -> /var/lib/odoo/
    Projects DIR -> /home/itachi/Projects/Odoo\n
    Python Environment Path -> /home/itachi/Env/\n
    Odoo configuration file -> /home/itachi/Projects/Odoo/Project_file/config/odoo_version.conf file\n
    '''


def find_conf_file(path, version):
    match = []
    regex = re.compile(f'^(.+){version}\.conf$')
    for root, dirs, files in os.walk(path):
        for file in files:
            if regex.match(file):
                match.append(os.path.join(root, file))
                return match
    else:
        raise ValueError(f'Odoo {version} conf file was not found in {path}')


def main():
    project_route = os.path.dirname('/home/itachi/Projects/Odoo/')
    virtual_env = os.path.dirname('/home/itachi/Env/')
    parser = argparse.ArgumentParser(description='''
    Start the odoo server
    Project Infrastructure: 
    Odoo DEFAULT Projects DIR -> /var/lib/odoo/
    Projects DIR -> /home/itachi/Projects/Odoo\n
    Python Environment Path -> /home/itachi/Env/\n
    Odoo configuration file -> /home/itachi/Projects/Odoo/Project_file/config/odoo_version.conf file\n
    ''')
    parser.add_argument('-v', '--version', type=int, choices=[13, 16, 17], default=13, help='odoo version(default is 13)')
    parser.add_argument('-n', '--name', required=True, help='Odoo Project file name')
    args = parser.parse_args()
    version = args.version
    project_name = args.name

    if len(sys.argv) == 0:
        parser._print_message(description)
        sys.exit(1)

    elif version and project_name:
        venv_path = os.path.join(virtual_env, f'odoo{version}/bin/activate')
        odoo_bin = os.path.join(f'/var/lib/odoo/o{version}/odoo-bin')
        project_path = os.path.join(project_route, project_name)
        config_path = f"{find_conf_file(project_path, version)[0]}"

    else:
        print(f"Unsupported version: {version} or Project: {project_name} are not found")
        sys.exit(1)
    cmd = f"source {venv_path} && {odoo_bin} -c {config_path}"
    subprocess.run(cmd, shell=True, check=True, executable='/bin/bash')


if __name__ == '__main__':
    main()


