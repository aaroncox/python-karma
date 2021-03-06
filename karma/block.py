from karma.instance import shared_karma_instance
from .exceptions import BlockDoesNotExistsException
from .utils import parse_time


class Block(dict):
    """ Read a single block from the chain

        :param int block: block number
        :param karma.karma.karma karma_instance: karma instance

        Instances of this class are dictionaries that come with additional
        methods (see below) that allow dealing with a block and it's
        corresponding functions.

        .. code-block:: python

            from karma.block import Block
            block = Block(1)
            print(block)

        .. note:: This class comes with its own caching function to reduce the
                  load on the API server. Instances of this class can be
                  refreshed with ``Account.refresh()``.

    """
    def __init__(
        self,
        block,
        karma_instance=None,
    ):
        self.karma = karma_instance or shared_karma_instance()
        self.block = block

        if isinstance(block, Block):
            super(Block, self).__init__(block)
        else:
            self.refresh()

    def refresh(self):
        """ Even though blocks never change, you freshly obtain its contents
            from an API with this method
        """
        block = self.karma.rpc.get_block(self.block)
        if not block:
            raise BlockDoesNotExistsException
        super(Block, self).__init__(block)

    def time(self):
        """ Return a datatime instance for the timestamp of this block
        """
        return parse_time(self['timestamp'])
