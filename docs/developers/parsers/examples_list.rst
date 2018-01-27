.. _examples_lists:

Examples - Lists
================

Parsing interfaces in industry standard CLIs (simple case)
----------------------------------------------------------

When TexTree parses industry standard CLIs it will generate a dictionary similar to::

    interface:
        Fa1:
            '#standalone': true
            '#text': no shutdown
            'no':
              '#text': shutdown
              shutdown:
                '#standalone': true
            # other data relevant to the interface
        Fa2:
            '#standalone': true
            '#text': shutdown
            shutdown:
              '#standalone': true
            # other data relevant to the interface

This means that to parse the interfaces we only have to advance to the ``interface``
key and map the keys to the YANG model key and get the block for further processing.


Original data
_____________

.. code::

    interface Port-Channel1
       shutdown
    !
    interface Port-Channel1.1
       shutdown
    !
    interface Ethernet1
       shutdown
    !
    interface Ethernet2
       no shutdown
    !
    interface Ethernet2.1
       no shutdown
    !
    interface Ethernet2.2
       no shutdown
    !
    interface Loopback1
       no shutdown
    !
    interface Management1
       no shutdown
    !



Parser rule
___________

.. code-block:: yaml

    - from: root_interfaces.0
      path: interface
      regexp: ^(?P<value>(\w|-)*\d+(\/\d+)*)$

* ``regexp`` is useful to filter out data that we don't want to process. For example,
  in the example above we are basically filtering subinterfaces as they will be
  processed later. Note that the regular expression has to capture a ``value``.
* ``path`` is simply telling the parser that the data is looking for is inside the
  ``interface`` key.
* ``from`` is just telling the parser where to get the data from. This is the first
  element processed by the profile so there is no information that can be inferred yet.


Result
______

Note that ``extra_vars`` will be populated with anything you capture with the regular
expression. This might be handier when parsing more complex keys like ip addresses
which might include the prefix length.

Note as well that we didn't get any subinterface thanks to ``regexp``.



Example 1
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys: {}

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">interface_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">Port-Channel1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': shutdown
    shutdown:
      '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: Port-Channel1</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">Ethernet1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': shutdown
    shutdown:
      '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: Ethernet1</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">Ethernet2</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': no shutdown
    'no':
      '#text': shutdown
      shutdown:
        '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: Ethernet2</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">Loopback1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': no shutdown
    'no':
      '#text': shutdown
      shutdown:
        '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: Loopback1</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">Management1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': no shutdown
    'no':
      '#text': shutdown
      shutdown:
        '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: Management1</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>

Parsing subinterfaces in industry standard CLIs (variables)
-----------------------------------------------------------

When we were parsing interfaces we skipped the subinterfaces. In order to pass
subinterfaces we can leverage on the ``interface_key`` to build a dynamic regular
expression.


Original data
_____________

.. code::

    interface Port-Channel1
       shutdown
    !
    interface Port-Channel1.1
       shutdown
    !
    interface Ethernet1
       shutdown
    !
    interface Ethernet2
       no shutdown
    !
    interface Ethernet2.1
       no shutdown
    !
    interface Ethernet2.2
       no shutdown
    !
    interface Loopback1
       no shutdown
    !
    interface Management1
       no shutdown
    !



Parser rule
___________

.. code-block:: yaml

    - path: interface
      regexp: '{{interface_key}}\.(?P<value>\d+)'

Because we are parsing a `subinterface` which is a child
of an `interface`, all the keys and extra_vars that we previously collected in the current
interface will be available.
We will use ``{{ interface_key }}`` in our regular expression to match only
our current parent interface.


Result
______

Note that thanks to the variable used in the regular expression we are only capturing
the relevant subinterface for the current interface. In the second case it turns out
there are no subinterfaces.



Example 1
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys:
      interface_key: Ethernet2

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">subinterface_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': no shutdown
    'no':
      '#text': shutdown
      shutdown:
        '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: '1'</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">2</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': no shutdown
    'no':
      '#text': shutdown
      shutdown:
        '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: '2'</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>


Example 2
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys:
      interface_key: Loopback1

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">subinterface_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            </tbody>
    </table></div>

Parsing IP addresses in EOS (extracting extra information from a key)
---------------------------------------------------------------------

IP addresses in EOS contain two pieces of information; the address and it's
prefix-length. You can use ``regexp`` to select the relevant part
for the key and any additional information you may need.


Original data
_____________

.. code::

    ip address 192.168.1.1/24
    ip address 192.168.2.1/24 secondary
    ip address 172.20.0.1/24 secondary



Parser rule
___________

.. code-block:: yaml

    - path: ip.address
      regexp: (?P<value>(?P<ip>.*))\/(?P<prefix>\d+)

The regular expression is doing two things; use the ``<value>`` to capture
which part should be used for the key and then capture as well all the useful
information so we have it available for later use in the ``extra_vars`` field.


Result
______

Note that ``extra_vars`` is populated with the information we captured with ``regexp.``.



Example 1
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys: {}

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">address_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">192.168.1.1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    ip: 192.168.1.1
    prefix: '24'
    value: 192.168.1.1</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">192.168.2.1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': secondary
    secondary:
      '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    ip: 192.168.2.1
    prefix: '24'
    value: 192.168.2.1</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">172.20.0.1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': secondary
    secondary:
      '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    ip: 172.20.0.1
    prefix: '24'
    value: 172.20.0.1</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>

Parsing IP addresses in IOS (flattening dictionaries)
-----------------------------------------------------

Sometimes the information is unnecessarily nested. This is the case for the ip
address configuration in IOS. Let's see how that data might look like after
processing it with the TextParser::

    ip:
        address:
            192.168.2.1:
                255.255.255.0:
                    secondary:
                        "#standalone": true
            192.168.1.1": {
                255.255.255.0:
                    "#standalone": true
            172.20.0.1:
                255.255.255.0:
                secondary":
                    "#standalone": true

Luckily, we can solve this issue with the ``path`` resolver.


Original data
_____________

.. code::

    ip address 192.168.1.1 255.255.255.0
    ip address 192.168.2.1 255.255.255.0 secondary
    ip address 172.20.0.1 255.255.255.0 secondary



Parser rule
___________

.. code-block:: yaml

    - key: prefix
      path: ip.address.?prefix.?mask
      regexp: ^(?P<value>\d+\.\d+\.\d+\.\d+)

We specify a ``regexp`` here to make sure we don't parse lines like ``ip address dhcp``.

When path contains ``?identifier`` what it actually does is flatten that key and assign
the value of that key to a new key named ``identifier``. For example, with the nested
structure and the path we have right now we would get the following::

    - prefix: 192.168.1.1
      mask: 255.255.255.0
      '#standalone': true
    - prefix: 192.168.2.1
      mask: 255.255.255.0
      secondary:
        '#standalone': true
    - prefix: 172.20.0.1
      mask: 255.255.255.0
      prefix: 172.20.0.1
      secondary:
        '#standalone': true


Result
______




Example 1
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys: {}

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">address_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">192.168.1.1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    mask: 255.255.255.0
    prefix: 192.168.1.1</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: 192.168.1.1</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">192.168.2.1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': secondary
    mask: 255.255.255.0
    prefix: 192.168.2.1
    secondary:
      '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: 192.168.2.1</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">172.20.0.1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': secondary
    mask: 255.255.255.0
    prefix: 172.20.0.1
    secondary:
      '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: 172.20.0.1</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>

Parse BGP neighbors in Junos (nested lists)
-------------------------------------------

XML often consists of lists of lists of lists which sometimes makes it challenging
to nest things in a sane manner. Hopefully, the ``path`` can solve this issue as well.


Original data
_____________

.. code::

    <some_configuration_block>
        <group>
            <name>my_peers</name>
            <neighbor>
                <name>192.168.100.2</name>
                <description>adsasd</description>
                <peer-as>65100</peer-as>
            </neighbor>
            <neighbor>
                <name>192.168.100.3</name>
                <peer-as>65100</peer-as>
            </neighbor>
        </group>
        <group>
            <name>my_other_peers</name>
            <neighbor>
                <name>172.20.0.1</name>
                <peer-as>65200</peer-as>
            </neighbor>
        </group>
    </some_configuration_block>



Parser rule
___________

.. code-block:: yaml

    - key: ip
      path: group.?peer_group:name.neighbor.?ip:name

Note that this time the path contains a couple of ``?identifier:field``. That pattern
is used to flatten lists and what it does is assign the contents of that sublist to the
parent object and also assign the value of ``field`` to a new ``key`` called ``identifier``.
For example, the XML above will be converted to the following structure::

    - name:
        '#text': my_peers
      peer-as:
        '#text': 65100
      neighbor: 192.168.100.3
      peer_group: my_peers
    - name:
        '#text': my_peers
      description:
        '#text': adsasd
      peer-as:
        '#text': 65100
      neighbor: 192.168.100.2
      peer_group: my_peers
    - name:
        '#text': my_other_peers
      peer-as:
        '#text': 65200
      neighbor: 172.20.0.1
      peer_group: my_other_peers


Result
______




Example 1
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys: {}

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">neighbor_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">192.168.100.2</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    description:
      '#text': adsasd
    ip:
      '#text': 192.168.100.2
    peer-as:
      '#text': '65100'
    peer_group:
      '#text': my_peers</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    {}</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">192.168.100.3</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    ip:
      '#text': 192.168.100.3
    peer-as:
      '#text': '65100'
    peer_group:
      '#text': my_peers</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    {}</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">172.20.0.1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    ip:
      '#text': 172.20.0.1
    peer-as:
      '#text': '65200'
    peer_group:
      '#text': my_other_peers</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    {}</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>

Parsing protocols (down the rabbit hole)
----------------------------------------

Some parsing might require more complex rules. In this example we can see how to combine
multiple rules ran under different circumstances.


Original data
_____________

.. code::

    ip route 10.0.0.0/24 192.168.0.2 10 tag 0
    ip route vrf devel 10.0.0.0/24 192.168.2.2 1 tag 0
    !
    router bgp 65001
       router-id 1.1.1.1
       address-family ipv4
          default neighbor 192.168.0.200 activate
       !
       address-family ipv6
          default neighbor 192.168.0.200 activate
       vrf devel
          router-id 3.3.3.3
    !
    router pim sparse-mode
       vrf devel
          ip pim log-neighbor-changes
    !



Parser rule
___________

.. code-block:: yaml

    - key: '{{ protocol }} {{ protocol }}'
      path: router.?protocol.?process_id
      regexp: (?P<value>bgp bgp)
      when: '{{ network_instance_key == ''global'' }}'
    - from: root_network-instances.0
      key: '{{ protocol }} {{ protocol }}'
      path: router.?protocol.?process_id.vrf.{{ network_instance_key }}
      regexp: (?P<value>bgp bgp)
      when: '{{ network_instance_key != ''global'' }}'
    - from: root_network-instances.0
      key: '{{ ''static static'' }}'
      path: ip.route

When multiple rules are specified all of them will be executed and the results will be
concatenated. You can combine this technique with ``when`` to specify how to parse the
data under different circumstances (see rules ``#1`` and ``#2``) or just to add more ways of
parsing data (see rule ``#3``)

Note also that we are also dynamically building the ``key`` to follow the format that
the YANG model requires, which in this case is as simple (and weird) as just specifying
a name for our protocol (which in our case will be the same as the protocool).

It also worth noting that we are using a regular expression to match only on ``BGP``. We
are doing that to avoid processing protocols that we are not (yet) supporting in this
profile.


Result
______

The results below might look intimidating but it's basically the relevant configuration for BGP and for the static routes for the current ``network_instance``.


Example 1
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys:
      network_instance_key: global

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">protocol_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">bgp bgp</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': vrf devel
    address-family:
      '#text': ipv6
      ipv4:
        '#list':
        - default:
            '#text': neighbor 192.168.0.200 activate
            neighbor:
              '#text': 192.168.0.200 activate
              192.168.0.200:
                '#text': activate
                activate:
                  '#standalone': true
        '#standalone': true
        '#text': default neighbor 192.168.0.200 activate
        default:
          '#text': neighbor 192.168.0.200 activate
          neighbor:
            '#text': 192.168.0.200 activate
            192.168.0.200:
              '#text': activate
              activate:
                '#standalone': true
      ipv6:
        '#list':
        - default:
            '#text': neighbor 192.168.0.200 activate
            neighbor:
              '#text': 192.168.0.200 activate
              192.168.0.200:
                '#text': activate
                activate:
                  '#standalone': true
        '#standalone': true
        '#text': default neighbor 192.168.0.200 activate
        default:
          '#text': neighbor 192.168.0.200 activate
          neighbor:
            '#text': 192.168.0.200 activate
            192.168.0.200:
              '#text': activate
              activate:
                '#standalone': true
    process_id: '65001'
    protocol: bgp
    router-id:
      '#text': 1.1.1.1
      1.1.1.1:
        '#standalone': true
    vrf:
      '#text': devel
      devel:
        '#list':
        - router-id:
            '#text': 3.3.3.3
            3.3.3.3:
              '#standalone': true
        '#standalone': true
        '#text': router-id 3.3.3.3
        router-id:
          '#text': 3.3.3.3
          3.3.3.3:
            '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: bgp bgp</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">static static</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': vrf devel 10.0.0.0/24 192.168.2.2 1 tag 0
    10.0.0.0/24:
      '#text': 192.168.0.2 10 tag 0
      192.168.0.2:
        '#text': 10 tag 0
        '10':
          '#text': tag 0
          tag:
            '#text': '0'
            '0':
              '#standalone': true
    vrf:
      '#text': devel 10.0.0.0/24 192.168.2.2 1 tag 0
      devel:
        '#text': 10.0.0.0/24 192.168.2.2 1 tag 0
        10.0.0.0/24:
          '#text': 192.168.2.2 1 tag 0
          192.168.2.2:
            '#text': 1 tag 0
            '1':
              '#text': tag 0
              tag:
                '#text': '0'
                '0':
                  '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    {}</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>


Example 2
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys:
      network_instance_key: devel

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">protocol_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">bgp bgp</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#standalone': true
    '#text': router-id 3.3.3.3
    process_id: '65001'
    protocol: bgp
    router-id:
      '#text': 3.3.3.3
      3.3.3.3:
        '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: bgp bgp</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">static static</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': vrf devel 10.0.0.0/24 192.168.2.2 1 tag 0
    10.0.0.0/24:
      '#text': 192.168.0.2 10 tag 0
      192.168.0.2:
        '#text': 10 tag 0
        '10':
          '#text': tag 0
          tag:
            '#text': '0'
            '0':
              '#standalone': true
    vrf:
      '#text': devel 10.0.0.0/24 192.168.2.2 1 tag 0
      devel:
        '#text': 10.0.0.0/24 192.168.2.2 1 tag 0
        10.0.0.0/24:
          '#text': 192.168.2.2 1 tag 0
          192.168.2.2:
            '#text': 1 tag 0
            '1':
              '#text': tag 0
              tag:
                '#text': '0'
                '0':
                  '#standalone': true</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    {}</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>

Parsing json interfaces IOS-XE (jsonrpc)
----------------------------------------

IOS-XE groups interfaces by type.


Original data
_____________

.. code::

    {
      "Cisco-IOS-XE-native:interface": {
        "GigabitEthernet": [
          {
            "name": "1",
            "ip": {
              "address": {
                "dhcp": {
                }
              }
            },
            "mop": {
              "enabled": false
            },
            "Cisco-IOS-XE-ethernet:negotiation": {
              "auto": true
            }
          },
          {
            "name": "2",
            "description": "GbE 2",
            "ip": {
              "no-address": {
                "address": false
              }
            },
            "mop": {
              "enabled": false
            },
            "Cisco-IOS-XE-ethernet:negotiation": {
              "auto": true
            }
          },
          {
            "name": "2.10",
            "description": "GbE 2.10",
            "encapsulation": {
              "dot1Q": {
                "vlan-id": 10
              }
            },
            "vrf": {
              "forwarding": "internal"
            },
            "ip": {
              "address": {
                "primary": {
                  "address": "172.16.10.1",
                  "mask": "255.255.255.0"
                }
              }
            }
          }
          ],
        "Loopback": [
          {
            "name": 0,
            "description": "Loopback Zero",
            "ip": {
              "address": {
                "primary": {
                  "address": "100.64.0.1",
                  "mask": "255.255.255.255"
                }
              }
            },
            "ipv6": {
              "address": {
                "prefix-list": [
                  {
                    "prefix": "2001:DB8::1/64"
                  }
                ]
              }
            }
          },
          {
            "name": 1,
            "description": "Loopback One",
            "vrf": {
              "forwarding": "mgmt"
            },
            "ip": {
              "no-address": {
                "address": false
              }
            }
          }
        ]
      }
    }



Parser rule
___________

.. code-block:: yaml

    - from: root_interfaces.0
      key: '{{ type }}{{ name }}'
      path: Cisco-IOS-XE-native:interface.?type
      regexp: ^(?P<value>(\w|-)*\d+(\/\d+)*)$



Result
______




Example 1
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys: {}

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">interface_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">GigabitEthernet1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    Cisco-IOS-XE-ethernet:negotiation:
      auto: true
    ip:
      address:
        dhcp: {}
    mop:
      enabled: false
    name: '1'
    type: GigabitEthernet</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: GigabitEthernet1</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">GigabitEthernet2</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    Cisco-IOS-XE-ethernet:negotiation:
      auto: true
    description: GbE 2
    ip:
      no-address:
        address: false
    mop:
      enabled: false
    name: '2'
    type: GigabitEthernet</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: GigabitEthernet2</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">Loopback0</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    description: Loopback Zero
    ip:
      address:
        primary:
          address: 100.64.0.1
          mask: 255.255.255.255
    ipv6:
      address:
        prefix-list:
        - prefix: 2001:DB8::1/64
    name: 0
    type: Loopback</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: Loopback0</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">Loopback1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    description: Loopback One
    ip:
      no-address:
        address: false
    name: 1
    type: Loopback
    vrf:
      forwarding: mgmt</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    value: Loopback1</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>

Parsing ntp peers Junos
-----------------------

Junos groups ntp servers and peers by type and then lists them


Original data
_____________

.. code::

    <configuration>
            <system>
                <ntp>
                    <peer>
                        <name>172.17.19.1</name>
                    </peer>
                    <server>
                        <name>172.17.19.2</name>
                        <name>172.17.19.3</name>
                    </server>
                </ntp>
            </system>
    </configuration>



Parser rule
___________

.. code-block:: yaml

    - key: '#text'
      path: configuration.system.ntp.?type.name



Result
______




Example 1
^^^^^^^^^^

.. code-block:: yaml

    extra_vars: {}
    keys: {}

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
            <th class="head">ntp_key</th>
            <th class="head">block</th>
            <th class="head">extra_vars</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">172.17.19.1</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': 172.17.19.1
    type: peer</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    {}</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">172.17.19.2</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': 172.17.19.2
    type: server</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    {}</pre></div></div></td>
            </td>
        </tr>
            <tr>
            <td style="vertical-align: top;">172.17.19.3</pre></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    '#text': 172.17.19.3
    type: server</pre></div></div></td>
            <td style="vertical-align: top;">
                <div class="code highlight-default"><div class="highlight" style="background:inherit; border:0px;"><pre>
    {}</pre></div></div></td>
            </td>
        </tr>
            </tbody>
    </table></div>

