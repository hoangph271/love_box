import ujson
import fs_helper as fs

_db_dir = ''

def _ensure_db_dir():
    if _db_dir == '':
        raise OSError('init_db() NOT executed...?')

def _json_path(key):
    _ensure_db_dir()
    return _db_dir + key

def init_db(db_dir):
    global _db_dir

    fs.ensure_dir(db_dir)
    _db_dir = db_dir

def get_val(key):
    if not fs.is_file(_json_path(key)):
        return None

    json = fs.read_text_file(_json_path(key))
    return ujson.loads(json)

def set_val(key, value):
    json = ujson.dumps(value)
    return fs.write_text_file(_json_path(key), json)

def detete_key(key):
    fs.rm(_json_path(key))
