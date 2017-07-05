"""
Global caching decorator
- init_disk_cache(filename) => stores all the data in the shelve file <filename>, marshalling is done via pickle
- init_memory_cache(size,ttl) => stores up to <size> results for <ttl> seconds
- nothing or no_cache() => no decoration and no caching
"""

global_caching = None


def init_disk_cache(filename):
    """
    Initialize for a disk cache
    :param filename: filename for the cache
    """
    import shelve
    global global_caching
    global_caching = shelve.open(filename)


def init_memory_cache(size, ttl):
    """
    Initialize for a memory lru cache
    :param size: max number of items
    :param ttl: max time to live for items in seconds
    """
    import cachetools
    global global_caching
    global_caching = cachetools.TTLCache(size, ttl)


def no_cache():
    """
    Deactivate caching
    """
    global global_caching
    global_caching = None


def clear_cache():
    """
    Clear the cache if initialized
    """
    global global_caching
    if global_caching is not None:
        del global_caching[:]


def caching(f):
    """
    Decorator for caching results
    :param f: the function to decorate
    :return: the decorated function if caching is activated before
    """
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
