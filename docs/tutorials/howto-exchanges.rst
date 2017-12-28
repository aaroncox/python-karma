Howto Interface your Exchange with karma
============================================

This Howto serves as an introduction for exchanges that want to
interface with karma to allow trading of assets from the karma
network.

We here start by introducing the overall concept of trusted node setup,
having different APIs that reply in JSON and describe the structure of
the received information (blocks etc).

Afterwards, we will go into more detail w.r.t. to the python-karma
library that helps you deal with the blockchain and can be seen as a
full-featured wallet (to replace the cli-wallet).

.. toctree::

   howto-build-karma.rst
   howto-trusted-node
   ../rpc
   howto-json-rpc
   howto-monitor-blocks
   howto-decode-memo
