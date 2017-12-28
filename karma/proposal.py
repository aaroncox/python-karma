from .instance import shared_karma_instance
from .account import Account
from .exceptions import ProposalDoesNotExistException
import logging
log = logging.getLogger(__name__)


class Proposal(dict):
    """ Read data about a Proposal Balance in the chain

        :param str id: Id of the proposal
        :param karma karma_instance: karma() instance to use when accesing a RPC

    """
    def __init__(
        self,
        id,
        karma_instance=None,
    ):
        self.id = id

        self.karma = karma_instance or shared_karma_instance()
        self.refresh()

    def refresh(self):
        a, b, c = self.id.split(".")
        assert int(a) == 1 and int(b) == 10, "Valid proposal ids are 1.10.x"
        proposal = self.karma.rpc.get_objects([self.id])
        if not any(proposal):
            raise ProposalDoesNotExistException
        super(Proposal, self).__init__(proposal[0])


class Proposals(list):
    """ Obtain a list of pending proposals for an account

        :param str account: Account name
        :param karma karma_instance: karma() instance to use when accesing a RPC
    """
    def __init__(self, account, karma_instance=None):
        self.karma = karma_instance or shared_karma_instance()

        account = Account(account)
        proposals = self.karma.rpc.get_proposed_transactions(account["id"])

        super(Proposals, self).__init__(
            [
                Proposal(x, karma_instance=self.karma)
                for x in proposals
            ]
        )
