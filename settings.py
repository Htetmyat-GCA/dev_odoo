import os

USER = os.environ.get('USER'),

HOME = os.environ.get('HOME'),

PROJECT = os.path.join(os.environ.get('HOME'), 'Projects/Odoo/'),

VIRTUAL = os.path.join(os.environ.get('HOME'), 'Env'),

# 'pre_version_post'

ENV_PREFIX = 'odoo',  # odoo -> odoo16, env_ -> env_16, env -> env16 version will be variable

ENV_POSTFIX = None  # ENV_POSTFIX = env ->

ODOO_ROOT_DIR = os.path.join(HOME[0], '.odoo'),

ODOO_VERSION_PREFIX = 'o'

ODOO_VERSION_POSTFIX = None

SHELL = os.environ.get('SHELL'),
