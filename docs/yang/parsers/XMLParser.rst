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

How-Tos
-------

Navigate the object and extract a list of elements
""""""""""""""""""""""""""""""""""""""""""""""""""

Let's imagine we have the following data:

.. code:: xml

    <configuration>
        <interfaces>
            <interface>
                <name>ge-0/0/0</name>
                ...
            </interface>
            <interface>
                <name>ge-0/0/1</name>
                ...
            </interface>
            <interface>
                <name>ge-0/0/2</name>
                ...
            </interface>
        </interfaces>
    </configuration>

In order to process the configuration and extract each interface individually, assigning the ``name`` subelement as the key for the ``YANG List`` we would do something like this:

.. code:: yaml

    interface:
        _process:
            - mode: xpath
              xpath: "interfaces/interface"
              key: name
              from: "{{ bookmarks.interfaces.0 }}"

Extract a simple element
""""""""""""""""""""""""

Now that we are extracting each element of the list individually we may have something like:

.. code:: xml

            <interface>
                <name>ge-0/0/0</name>
                <description>This is my description</description>
                ...
            </interface>

So in order to extract the description and assign it we would only have to do something like this:

.. code:: yaml

            description:
                _process:
                    - mode: xpath
                      xpath: description
                      from: "{{ bookmarks['parent'] }}"

Checking if an element is absent
""""""""""""""""""""""""""""""""

A disabled interface will have the element ``disabled`` present while an enabled interface will not have any mention of it. For example:


.. code:: xml

            <interface>
                <name>ge-0/0/0</name>
                <description>I am not enabled</description>
                <disabled/>
                ...
            </interface>
            <interface>
                <name>ge-0/0/0</name>
                <description>I am enabled</description>
                ...
            </interface>

So in order to know if the interface is enabled you have to verify if the element is absent. You can do that like this:

.. code:: yaml

            enabled:
                _process:
                    - mode: is_absent
                      xpath: "disable"
                      from: "{{ bookmarks['parent'] }}"

There is also a mode called ``is_present`` that behaves in the exact opposite way.

Extracting information and assigning a known value
""""""""""""""""""""""""""""""""""""""""""""""""""

Sometimes the information is somehow encoded in the configuration. For example, in Junos an interface which name starts with ``ge`` is of type ``ethernetCsmacd`` while an interface which name starts with ``lo`` is of type ``softwareLoopback``. You can extract information from the configuration and assign a known value like this:

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
