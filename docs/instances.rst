Instances
~~~~~~~~~

Default instance to be used when no ``karma_instance`` is given to
the Objects!

.. code-block:: python

   from karma.instance import shared_karma_instance

   account = Account("xeroc")
   # is equivalent with 
   account = Account("xeroc", karma_instance=shared_karma_instance())

.. automethod:: karma.instance.shared_karma_instance
.. automethod:: karma.instance.set_shared_karma_instance
