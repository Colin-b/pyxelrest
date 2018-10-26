import logging

logger = logging.getLogger(__name__)
caches = {}


def create_cache(max_nb_results, ttl):
    """
    Create a new in-memory cache.

    :param max_nb_results: Maximum number of results that can be stored.
    :param ttl: max time to live for items in seconds
    :return The newly created memory cache or None if not created.
    """
    try:
        import cachetools
        return cachetools.TTLCache(max_nb_results, ttl)
    except ImportError:
        logger.warning('cachetools module is required to initialize a memory cache.')


def cache_result(f):
    def wrapper(*args, **kwargs):
        # key must be hashable
        global caches
        key = f.__name__ + '(' + str(args) + ',' + str(kwargs) + ')'
        cache = caches[f.__xlfunc__['category']]
        if key in cache:
            logger.debug('Using cache for {}'.format(key))
            return cache[key]
        res = f(*args, **kwargs)
        cache[key] = res
        return res
    return wrapper
