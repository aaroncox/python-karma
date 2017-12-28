Amount
~~~~~~

For the sake of easier handling of Assets on the blockchain

.. code-block:: python

   from karma.amount import Amount
   from karma.asset import Asset
   a = Amount("1 USD")
   b = Amount(1, "USD")
   c = Amount("20", Asset("USD"))
   a + b
   a * 2
   a += b
   a /= 2.0

.. autoclass:: karma.amount.Amount
   :members:
