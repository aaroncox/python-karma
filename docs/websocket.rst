******************
KarmaWebsocket
******************

This class allows subscribe to push notifications from the karma
node.

.. code-block:: python

    from pprint import pprint
    from karmaapi.websocket import KarmaWebsocket

    ws = KarmaWebsocket(
        "wss://node.testnet.karma.eu",
        markets=[["1.3.0", "1.3.172"]],
        accounts=["xeroc"],
        objects=["2.0.x", "2.1.x"],
        on_market=pprint,
        on_account=print,
    )

    ws.run_forever()

Defintion
=========
.. autoclass:: karmaapi.websocket.KarmaWebsocket
    :members:
    :undoc-members:
    :private-members:
    :special-members:
