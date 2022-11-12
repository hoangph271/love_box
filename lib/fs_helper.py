import os

def read_text_file(path):
    with open(path, 'r') as fd:
        return fd.read()

def write_text_file(path, text):
    with open(path, 'w') as fd:
        return fd.write(text)

def is_dir(path):
        try:
            return (os.stat(path)[0] & 0x4000) != 0
        except:
            return False

def is_file(path):
        try:
            return (os.stat(path)[0] & 0x4000) == 0
        except:
            return False

def ensure_dir(path):
    if not is_dir(path):
        os.mkdir(path)

def rm(path):
    if is_dir(path):
        os.rmdir(path)

    if is_file(path):
        os.remove(path)
