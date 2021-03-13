from os import mkdir, path

from yaml import safe_load


def check_or_create_dir(dirpath):
    if not path.exists(dirpath):
        mkdir(dirpath)


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return safe_load(f.read())
