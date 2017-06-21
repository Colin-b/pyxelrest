"""
Global caching decorator
- init_dbm(filename) => stores all the data in the shelve file <filename>, marshalling is done via pickle
- init_lru(size,ttl) => stores up to <size> results for <ttl> seconds
- nothing or init_nothing() => no decoration and no caching
"""

global_caching = None


def init_shelve(filename):
    import shelve
    global global_caching
    global_caching = shelve.open(filename, 'c')


def init_lru(size, ttl):
    import cachetools
    global global_caching
    global_caching = cachetools.TTLCache(size, ttl)


def init_nothing():
    global global_caching
    global_caching = None


def caching(f):
    if global_caching is not None:
        def wrapper(*args, **kwargs):
            global global_caching
            # key must be hashable
            key = f.__name__ + '(' + str(args) + ',' + str(kwargs) + ')'
            if key in global_caching:
                return global_caching[key]
            res = f(*args, **kwargs)
            global_caching[key] = res
            return res
        return wrapper
    return f
