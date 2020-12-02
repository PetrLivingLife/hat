from os import path, mkdir


def check_or_create_dir(dirpath):
    if not path.exists(dirpath):
        mkdir(dirpath)
