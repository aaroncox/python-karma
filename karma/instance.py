import karma as dct

_shared_karma_instance = None


def shared_karma_instance():
    """ This method will initialize ``_shared_karma_instance`` and return it.
        The purpose of this method is to have offer single default
        karma instance that can be reused by multiple classes.
    """
    global _shared_karma_instance
    if not _shared_karma_instance:
        _shared_karma_instance = dct.karma()
    return _shared_karma_instance


def set_shared_karma_instance(karma_instance):
    """ This method allows us to override default karma instance for all users of
        ``_shared_karma_instance``.

        :param karma.karma.karma karma_instance: karma instance
    """
    global _shared_karma_instance
    _shared_karma_instance = karma_instance
