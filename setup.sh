#! /bin/bash
pip install -r $(pwd)/requirements.txt
activate-global-python-argcomplete --user
chmod +x $(pwd)/run
eval "$(register-python-argcomplete $(pwd)/run)"
echo eval "$(register-python-argcomplete $(pwd)/run)" >> ~/.bashrc
source ~/.bashrc
exit
