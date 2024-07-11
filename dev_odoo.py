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


# Check the directory is present and can be accessed by current user.
def is_root(path):
    if type(path) == str:
        return os.path.isdir(path) and os.access(path, os.R_OK)
    for d in path:
        return os.path.isdir(d) and os.access(d, os.R_OK)


def main():
    parser = argparse.ArgumentParser(description='''
    Start the odoo server
    Project Infrastructure: 
    Odoo DEFAULT Projects DIR -> /var/lib/odoo/
    Projects DIR -> /home/itachi/Projects/Odoo\n
    Python Environment Path -> /home/itachi/Env/\n
    Odoo configuration file -> /home/itachi/Projects/Odoo/Project_file/config/odoo_version.conf file\n
    ''')
    parser.add_argument('-v', '--version', type=int, choices=[13, 16, 17], default=13,
                        help='odoo version(default is 13)')
    parser.add_argument('-p', '--project', required=True, help='Odoo Project file name')
    args = parser.parse_args()
    version = args.version
    name = args.project
    venv = odoo_bin = config_file = None
    if version and name:
        if is_root(ODOO_ROOT_DIR) and is_root(PROJECT_ROOT) and is_root(VIRTUAL):
            venv = os.path.join(VIRTUAL[0],
                                f'{ENV_PREFIX[0] if ENV_PREFIX is not None else ''}{version}{ENV_POSTFIX[0] if 
                                ENV_POSTFIX is not None else ''}/bin/activate')
            odoo_bin = os.path.join(ODOO_ROOT_DIR[0],
                                    f'{ODOO_VERSION_PREFIX}{version}{ODOO_VERSION_POSTFIX if ENV_POSTFIX is not None else ''}/odoo-bin')
            project_dir = os.path.join(PROJECT_ROOT[0], name)
            config_file = f"{find_conf_file(project_dir, version)[0]}"
        else:
            for root in [ODOO_ROOT_DIR, PROJECT_ROOT, VIRTUAL]:
                if not is_root(root):
                    print(f'"{root[0]}" directory was not found in the your system path')
    else:
        print(f"Unsupported version: {version} or Project: {name} are not found")
        sys.exit(1)
    if venv and odoo_bin and config_file:
        cmd = f"source {venv} && {odoo_bin} -c {config_file}"
        try:
            subprocess.run(cmd, shell=True, check=True, executable=SHELL[0])
        except subprocess.CalledProcessError as e:
            print(f"Command failed: with exit status {e.returncode}: {e.cmd}")
            exit(e.returncode)
    else:
        exit(1)


if __name__ == '__main__':
    main()
