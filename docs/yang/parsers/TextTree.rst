TextParser
==========

Will apply regular expressions to text to extract data from it.

To explain how this parser works, let's use the following configuration::

    interface Ethernet1
        no switchport
    !
    interface Ethernet1.1
        description blah
    !
    interface Loopback1
        no switchport
        ip address 192.168.0.1/24
        ip address 192.168.1.1/24 secondary
    !

.. note:: The regular expressions on this parser have the ``MULTILINE`` and ``IGNORECASE`` flags turned on.
