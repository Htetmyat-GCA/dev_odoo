#!/usr/bin/python3

import subprocess
from pathlib import Path

class Str(str):
    def __sub__(self, *args):
        res = self
        for arg in args:
            if arg in self:
                res = self.replace(arg, '')
        return Str(res)

program_dir = Path(__file__).resolve().parent
run = program_dir / 'run'
home_to_script = Str(program_dir) - Str(str(Path.home()) + '/')
global_auto_complete = 'activate-global-python-argcomplete3 --user'
chmod = f'chmod +x {run}'
to_register = f'eval "$(register-python-argcomplete3 {home_to_script}/run)"'
add_bashrc = f'echo \'eval "$(register-python-argcomplete3 {home_to_script}/run)"\' >> ~/.bashrc'
reload = f'source {Path.home()}/.bashrc'
ex = 'exit'
for cmd in [global_auto_complete, chmod, to_register, add_bashrc, reload, ex]:
    try:
        subprocess.run(cmd, shell=True, check=True, executable='/bin/bash')
    except subprocess.CalledProcessError as e:
        print(e)
