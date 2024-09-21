#!/usr/bin/python3

import argparse
import subprocess
import sys
# import argcomplete
import re

from attr.validators import optional

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
    return os.path.isdir(path) and os.access(path, os.R_OK)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', type=int, choices=[13, 16, 17], default=17,
                        help='odoo version(default is 17)')
    parser.add_argument('-p', '--project', type=str, choices=[i for i in os.listdir(PROJECT_ROOT[0]) if '.' not in i],
                        required=True, help='Odoo Project file name')
    parser.add_argument('-u', '--upgrade', type=str, required=False, help='To upgrade modules')
    parser.add_argument('-d', '--database', type=str, required=False, help='Select the database')
    parser.add_argument('-s', '--shell', action='store_true', required=False, help='Odoo Shell')
    # argcomplete.autocomplete(parser)
    args = parser.parse_args()
    version = args.version
    name = args.project
    upgrade = args.upgrade
    db = args.database
    shell = 'shell' if args.shell else ''
    venv = odoo_bin = config_file = None
    if version and name:
        if all(map(is_root, [ODOO_ROOT_DIR[0], PROJECT_ROOT[0], VIRTUAL[0]])):
            venv = os.path.join(VIRTUAL[0],
                                f'{ENV_PREFIX[0] if ENV_PREFIX is not None else ''}{version}{ENV_POSTFIX[0] if 
                                ENV_POSTFIX is not None else ''}/bin/activate')
            odoo_bin = os.path.join(ODOO_ROOT_DIR[0],
                                    f'{ODOO_VERSION_PREFIX}{version}{ODOO_VERSION_POSTFIX if ENV_POSTFIX is not None else ''}/odoo-bin {shell}')
            project_dir = os.path.join(PROJECT_ROOT[0], name)
            config_file = f"{find_conf_file(project_dir, version)[0]}"
        else:
            p = ['ODOO_ROOT_DIR', 'PROJECT_ROOT', 'VIRTUAL']
            for i, root in enumerate([ODOO_ROOT_DIR, PROJECT_ROOT, VIRTUAL]):
                if not is_root(root):
                    print(f'"{root[0]}"  directory was not found in the your system path or cannot access the directory.')
                    print(f'Please re-config your {p[i]} at settings.py!')
    else:
        print(f"Unsupported version: {version} or Project: {name} are not found")
        sys.exit(1)
    if venv and odoo_bin and config_file:
        cmd = f"source {venv} && {odoo_bin} -c {config_file}"
        if upgrade:
            cmd += f" -u {upgrade}"
        if db:
            cmd += f" -d {db}"
        if shell and not db:
            raise ValueError("Database must be selected")
        try:
            subprocess.run(cmd, shell=True, check=True, executable=SHELL[0])
        except subprocess.CalledProcessError as e:
            print(f"Command failed: with exit status {e.returncode}: {e.cmd}")
            exit(e.returncode)
        except KeyboardInterrupt:
            print(f"Keyboard interrupt received, exiting...")
            exit(0)
    else:
        exit(1)


if __name__ == '__main__':
    main()
