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
      present: true
      value: WIDE_METRIC



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

