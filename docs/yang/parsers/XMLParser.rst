XMLParser
=========

This extractor will read an XML an extract data from it.

List Elements
-------------


=========== ======================================= ==============================================
Name        Arguments                               Description
=========== ======================================= ==============================================
xpath       * **xpath** [#f101]_ (mandatory)        Advances in the XML document up to the point
            * **key** [#f102]_ (mandatory)          where the relevant list of elements is found.
=========== ======================================= ==============================================

.. rubric:: Arguments

.. [#f101] **xpath** - Elements to traverse
.. [#f102] **key** - When extracting a list of elements, which subelement is the key element.

Examples
________

Example: xpath
""""""""""""""

When processing interfaces, go to ``interfaces/interface`` to find all the interface element and use the subelement ``name`` as key.

.. code:: yaml

    interface:
        _process:
            - mode: xpath
              xpath: "interfaces/interface"
              key: name
              from: "{{ bookmarks.interfaces.0 }}"



Leaf Elements
-------------

=========== ======================================= =============================================================
Name        Arguments                               Description
=========== ======================================= =============================================================
xpath       * **xpath** [#f201]_ (mandatory)        Extracts a value from an element
            * **regexp** [#f202]_ (optional)
            * **default** [#f203]_ (optional)
            * **attribute** [#f204]_ (optional)
value       * **value** [#f205]_ (mandatory)        Apply a user-defined value to the object.
map         * **xpath** [#f201]_ (mandatory)        Extract value and do a lookup to choose value
            * **regexp** [#f202]_ (optional)
            * **map** [#f206]_ (optional)
is_absent   Same as ``xpath``                       Works exactly like ``xpath`` but if the evaluation **is**
                                                    ``None``, it will return ``True``
is_present  Same as ``xpath``                       Works exactly like ``xpath`` but if the evaluation **is not**
                                                    ``None``, it will return ``True``
=========== ======================================= =============================================================

.. rubric:: Arguments

.. [#f201] **xpath** - element to extract 
.. [#f202] **regexp** - Apply regexp to the value of the element. Must capture value group.
.. [#f203] **default** - Set this value if no element is found.
.. [#f204] **attribute** - Instead of the text of the element extracted, extract this attribute of the element.
.. [#f205] **value** - Value to apply
.. [#f206] **map** - Dictionary where we will do the lookup action.

Examples
________

Example: xpath
""""""""""""""

Extract content of the element ``description`` and assign it to the leaf.

.. code:: yaml

            description:
                _process:
                    - mode: xpath
                      xpath: description
                      from: "{{ bookmarks['parent'] }}"

Example: is_absent
""""""""""""""""""

If the element ``<disable/>`` exists it means the interface is down so we are going to check it's absent in which chase ``enabled`` will be ``True``.

.. code:: yaml

            enabled:
                _process:
                    - mode: is_absent
                      xpath: "disable"
                      from: "{{ bookmarks['parent'] }}"


Example: map
""""""""""""

Use map in combination with regexp to extract the interface type. For example, if the interface name is ``ge-0/0/0`` the regexp will extract ``ge`` and assign the type ``ethernetCsmacd``.

.. code:: yaml

            type:
                _process:
                    - mode: map
                      xpath: name
                      regexp: "(?P<value>[a-z]+).*"
                      from: "{{ bookmarks['parent'] }}"
                      map:
                          ge: ethernetCsmacd
                          xe: ethernetCsmacd
                          et: ethernetCsmacd
                          irb: ethernetCsmacd
                          me: ethernetCsmacd
                          vlan: ethernetCsmacd
                          lo: softwareLoopback
                          ae: ieee8023adLag

