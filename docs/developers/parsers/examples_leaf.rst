.. _examples_leaf:

Examples - leaf
===============

Parsing metric style for junos ISIS level
-----------------------------------------

Junos sometimes indicates the value of something not by using an element with a specific value but by the presence of it. For instance, the metric style of an ISIS level can either be NARROW or WIDE but instead of indicating explicitly junos will do it with the presence or not of the element ``</wide-metrics-only>``.


Original data
_____________

.. code::

    <configuration>
        <isis>
            <level>
                <name>1</name>
                <wide-metrics-only/>
            </level>
            <level>
                <name>2</name>
                <preference>50</preference>
            </level>
            <interface>
                <name>ge-0/0/0.0</name>
                <point-to-point/>
            </interface>
            <interface>
                <name>ge-0/0/1.0</name>
                <point-to-point/>
            </interface>
            <interface>
                <name>ge-0/0/2.0</name>
                <point-to-point/>
            </interface>
            <interface>
                <name>ge-0/0/3.0</name>
                <point-to-point/>
            </interface>
            <interface>
                <name>lo0.0</name>
            </interface>
        </isis>
    </configuration>



Parser rule
___________

.. code-block:: yaml

    - default: NARROW_METRIC
      path: wide-metrics-only
      post: WIDE_METRIC
      present: true



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
            <th class="head">block</th>
            <th class="head">value</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">&lt;level&gt; &lt;name&gt;1&lt;/name&gt; &lt;wide-metrics-only/&gt; &lt;/level&gt;</pre></td>
            <td style="vertical-align: top;">WIDE_METRIC</pre></td>
        </tr>
            <tr>
            <td style="vertical-align: top;">&lt;level&gt; &lt;name&gt;2&lt;/name&gt; &lt;preference&gt;50&lt;/preference&gt; &lt;/level&gt;</pre></td>
            <td style="vertical-align: top;">NARROW_METRIC</pre></td>
        </tr>
            </tbody>
    </table></div>

Parse EOS privilege:role
------------------------

The role in eos is the combination of the privilege level and the role itself. In this example we should how to use a regular expression to capture data and postprocess it to set the correct role.


Original data
_____________

.. code::

    username test1 privilege 1 nopassword
    username test2 privilege 1 secret sha512 $6$WL/ibPpzPJ/C7c/E$.bVF08dYhlNp0rxER0P3SNdsA2wUtK2Ru1YuKkRRZQGl609DA1JvX.dSFgKXaq.LWjDRlZoHudfk7hamod0Th/
    username test3 privilege 15 role network-operator secret sha512 $6$Vd6.7k2FybfsTKKp$S.AHfdwicaWEoA41sPd6ZXOOdruJMrKJh70WNfiX/eZKH1oYBtFz9VbrPlYNDkhM/pi54gcYKH2hviy/xrUav.
    username test4 privilege 1 secret 5 $1$NKhJ$PUfYNtJF2tIneEBZztchy.
    username test5 privilege 15 secret sha512 $6$d3fdbbZBrhplknVB$FILKNelLURwd/xT74ktjxJ4XP1vTfJ53H7OWJHgAqeuY/lF3BDyP3SWpH/MeBRnl7lLi8hU2oy6hkbnB7jvtA.
    username test6 privilege 1 role network-admin secret sha512 $6$zaalm5RTm6/26XVS$I/f3kmOqfvTbjwjzepCe1O9eYfPJRdUrRLe9NoMsbgNz9T48nj0AlOsm2LmoFp6aI5B6Q/xlseJdNrTL/jiXH0
    username test7 privilege 15 role network-admin secret 5 $1$NKhJ$PUfYNtJF2tIneEBZztchy. 



Parser rule
___________

.. code-block:: yaml

    - path: privilege
      post: '{{ extra_vars.privilege }}:{{ extra_vars.role }}'
      regexp: (?P<value>(?P<privilege>\d+).*role (?P<role>\S+)) secret
    - path: privilege
      post: '{{ value }}:network-operator'
      regexp: (?P<value>\d+)



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
            <th class="head">block</th>
            <th class="head">value</th>
        </tr>
        <tbody>
            <tr>
            <td style="vertical-align: top;">username test1 privilege 1 nopassword</pre></td>
            <td style="vertical-align: top;">1:network-operator</pre></td>
        </tr>
            <tr>
            <td style="vertical-align: top;">username test2 privilege 1 secret sha512 $6$WL/ibPpzPJ/C7c/E$.bVF08dYhlNp0rxER0P3SNdsA2wUtK2Ru1YuKkRRZQGl609DA1JvX.dSFgKXaq.LWjDRlZoHudfk7hamod0Th/</pre></td>
            <td style="vertical-align: top;">1:network-operator</pre></td>
        </tr>
            <tr>
            <td style="vertical-align: top;">username test3 privilege 15 role network-operator secret sha512 $6$Vd6.7k2FybfsTKKp$S.AHfdwicaWEoA41sPd6ZXOOdruJMrKJh70WNfiX/eZKH1oYBtFz9VbrPlYNDkhM/pi54gcYKH2hviy/xrUav.</pre></td>
            <td style="vertical-align: top;">15:network-operator</pre></td>
        </tr>
            <tr>
            <td style="vertical-align: top;">username test4 privilege 1 secret 5 $1$NKhJ$PUfYNtJF2tIneEBZztchy.</pre></td>
            <td style="vertical-align: top;">1:network-operator</pre></td>
        </tr>
            <tr>
            <td style="vertical-align: top;">username test5 privilege 15 secret sha512 $6$d3fdbbZBrhplknVB$FILKNelLURwd/xT74ktjxJ4XP1vTfJ53H7OWJHgAqeuY/lF3BDyP3SWpH/MeBRnl7lLi8hU2oy6hkbnB7jvtA.</pre></td>
            <td style="vertical-align: top;">15:network-operator</pre></td>
        </tr>
            <tr>
            <td style="vertical-align: top;">username test6 privilege 1 role network-admin secret sha512 $6$zaalm5RTm6/26XVS$I/f3kmOqfvTbjwjzepCe1O9eYfPJRdUrRLe9NoMsbgNz9T48nj0AlOsm2LmoFp6aI5B6Q/xlseJdNrTL/jiXH0</pre></td>
            <td style="vertical-align: top;">1:network-admin</pre></td>
        </tr>
            <tr>
            <td style="vertical-align: top;">username test7 privilege 15 role network-admin secret 5 $1$NKhJ$PUfYNtJF2tIneEBZztchy.</pre></td>
            <td style="vertical-align: top;">15:network-admin</pre></td>
        </tr>
            </tbody>
    </table></div>

