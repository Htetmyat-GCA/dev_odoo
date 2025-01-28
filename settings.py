import os

USER = os.getenv('USER')

HOME = os.getenv('HOME')

PROJECT_ROOT = os.path.join(HOME, 'Projects/')  # set your project root directory

VIRTUAL = os.path.join(HOME, '.env')  # change your python environment root directory

# '{prefixword}{version}{postfix}'

ENV_PREFIX = 'env'  #  env17, odoo17...

ENV_POSTFIX = ''  #  17env, 17odoo

ODOO_ROOT_DIR = os.path.join(HOME, 'odoo')  # change your odoo root directory

ODOO_VERSION_PREFIX = '' # Eg: o17, odoo17, od17...

ODOO_VERSION_POSTFIX = 'o' # Eg: 17o, 17odoo, 17od

SHELL = os.environ.get('SHELL')
