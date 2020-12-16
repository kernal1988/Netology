import datetime
import hashlib


def decorator(file):
    def replacement(old_func):
        def new_func(*args, **kwargs):
            start = datetime.datetime.now()
            name = old_func.__name__
            result = old_func(*args, **kwargs)
            res = str(result)
            with open(file, 'w') as f:
                f.write(f'{start}\n {name}\n {args}\n {res}\n')
            for item in old_func(*args, **kwargs):
                with open(file, 'a') as f:
                    f.write(f'{item} \n')
        return new_func
    return replacement


@decorator('logs.txt')
def generator(file):
    with open(file, 'r') as f:
        for line in f:
            str = line.encode('utf-8')
            hash_str = hashlib.md5(str)
            yield hash_str.hexdigest()

generator('country.txt')