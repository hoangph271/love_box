from pathlib import Path, PurePath
from fs_helper import read_text_file

_db_dir = ''

def _ensure_db_dir():
    if _db_dir == '':
        raise IOError('init_db() NOT executed...?')

def init_db(db_dir):
    Path(db_dir).mkdir(parents=True, exist_ok=True)
    _db_dir = db_dir

def get_json(key):
    _ensure_db_dir()

    json_path = PurePath(_db_dir, key)
    print(f'{json_path}')
