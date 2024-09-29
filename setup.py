#!/usr/bin/python3

import subprocess
from pathlib import Path
from settings import *


class Str(str):
    def __sub__(self, *args):
        res = self
        for arg in args:
            if arg in self:
                res = self.replace(arg, '')
        return Str(res)

program_dir = Path(__file__).resolve().parent
run = f'{program_dir}/run'
home_to_script = Str(program_dir) - Str(HOME+'/')
global_auto_complete = 'activate-global-python-argcomplete --user'
chmod = f'chmod +x {run}'
to_register = f'eval "$(register-python-argcomplete {home_to_script}/run)"'
add_bashrc = f'echo \'eval "$(register-python-argcomplete {home_to_script}/run)"\' >> ~/.bashrc'
reload = f'source {HOME}/.bashrc'
ex = 'exit'
for cmd in [global_auto_complete, chmod, to_register, add_bashrc, reload, ex]:
    try:
        subprocess.run(cmd, shell=True, check=True, executable=SHELL)
    except subprocess.CalledProcessError as e:
        print(e)

# print("The shell will be terminated to sure.")
# cmd += " && exit"
# print(cmd)
# # subprocess.run(cmd, shell=True, check=True, executable=SHELL)

