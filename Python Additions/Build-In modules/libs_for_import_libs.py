# importlib

import importlib

importlib.import_module('some_module')

# ---
# Check module importing
# "EAFP: Easier to ask for forgiveness than permission"

import importlib.util


def check_module(module_name):
    """Check module importing without import it"""
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module not found: {}'.format(module_name))
        return False
    else:
        print('Module found: {}'.format(module_name))
        return module_spec

# ---


# -----------------------

# ctypes
