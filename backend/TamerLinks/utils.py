import os


def use_path(path):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        file = open(path, 'a+')
        file.close()

    return path
