import os

USER = os.environ.get('USER'),

HOME = os.environ.get('HOME'),

PROJECT_ROOT = os.path.join(os.environ.get('HOME'), 'Projects/Odoo/'),  # set your project root directory

VIRTUAL = os.path.join(os.environ.get('HOME'), 'pyenv'),  # change your python environment root directory

# 'pre_version_post'

ENV_PREFIX = 'odoo',  # if ENV_PREFIX is not None: pre_version -> {pre}{version}

ENV_POSTFIX = None  # if ENV_POSTFIX is not none: version_postfix -> {version}{post}

ODOO_ROOT_DIR = os.path.join(HOME[0], '.odoo'),  # change your odoo root directory

ODOO_VERSION_PREFIX = 'o'

ODOO_VERSION_POSTFIX = None

SHELL = os.environ.get('SHELL'),
