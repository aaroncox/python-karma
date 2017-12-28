import logging
from events import Events
from karmaapi.websocket import KarmaWebsocket
from karma.instance import shared_karma_instance
from karma.account import Account, AccountUpdate
log = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)


class Notify(Events):
    """ Notifications on Blockchain events.

        :param list accounts: Account names/ids to be notified about when changing
        :param list objects: Object ids to be notified about when changed
        :param fnt on_tx: Callback that will be called for each transaction received
        :param fnt on_block: Callback that will be called for each block received
        :param fnt on_account: Callback that will be called for changes of the listed accounts
        :param karma.karma.karma karma_instance: karma instance

        **Example**

        .. code-block:: python

            from pprint import pprint
            from karma.notify import Notify

            notify = Notify(
                accounts=["xeroc"],
                on_account=print,
                on_block=print,
                on_tx=print
            )
            notify.listen()


    """

    __events__ = [
        'on_tx',
        'on_object',
        'on_block',
        'on_account',
    ]

    def __init__(
        self,
        accounts=[],
        objects=[],
        on_tx=None,
        on_object=None,
        on_block=None,
        on_account=None,
        karma_instance=None,
    ):
        # Events
        super(Notify, self).__init__()
        self.events = Events()

        # karma instance
        self.karma = karma_instance or shared_karma_instance()

        # Accounts
        account_ids = []
        for account_name in accounts:
            account = Account(
                account_name,
                karma_instance=self.karma
            )
            account_ids.append(account["id"])

        # Callbacks
        if on_tx:
            self.on_tx += on_tx
        if on_object:
            self.on_object += on_object
        if on_block:
            self.on_block += on_block
        if on_account:
            self.on_account += on_account

        # Open the websocket
        self.websocket = KarmaWebsocket(
            urls=self.karma.rpc.urls,
            user=self.karma.rpc.user,
            password=self.karma.rpc.password,
            accounts=account_ids,
            objects=objects,
            on_tx=on_tx,
            on_object=on_object,
            on_block=on_block,
            on_account=self.process_account,
        )

    def process_account(self, message):
        """ This is used for processing of account Updates. It will
            return instances of :class:karma.account.AccountUpdate`
        """
        self.on_account(AccountUpdate(message))

    def listen(self):
        """ This call initiates the listening/notification process. It
            behaves similar to ``run_forever()``.
        """
        self.websocket.run_forever()
