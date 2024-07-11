#!/usr/bin/python3

import argparse
import subprocess
import sys
import re
from settings import *


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
    parser = argparse.ArgumentParser(description='''
    Start the odoo server
    Project Infrastructure: 
    Odoo DEFAULT Projects DIR -> /var/lib/odoo/
    Projects DIR -> /home/itachi/Projects/Odoo\n
    Python Environment Path -> /home/itachi/Env/\n
    Odoo configuration file -> /home/itachi/Projects/Odoo/Project_file/config/odoo_version.conf file\n
    ''')
    parser.add_argument('-v', '--version', type=int, choices=[13, 16, 17], default=13, help='odoo version(default is 13)')
    parser.add_argument('-p', '--project', required=True, help='Odoo Project file name')
    args = parser.parse_args()
    version = args.version
    name = args.project
    if version and name:
        venv_path = os.path.join(VIRTUAL[0], f'{ENV_PREFIX[0] if ENV_PREFIX is not None else ''}{version}{ENV_POSTFIX[0] if ENV_POSTFIX is not None else ''}/bin/activate')
        odoo_bin = os.path.join(ODOO_ROOT_DIR, f'{ODOO_VERSION_PREFIX}{version}{ODOO_VERSION_POSTFIX if ENV_POSTFIX is not None else ''}/odoo-bin')
        project_dir = os.path.join(PROJECT[0], name)
        config_path = f"{find_conf_file(project_dir, version)[0]}"

    else:
        print(f"Unsupported version: {version} or Project: {name} are not found")
        sys.exit(1)
    cmd = f"source {venv_path} && {odoo_bin} -c {config_path}"
    subprocess.run(cmd, shell=True, check=True, executable=SHELL[0])


if __name__ == '__main__':
    main()


