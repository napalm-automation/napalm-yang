.. raw:: html

    <div><table border="1" class="docutils" width="100px">
        <col style="width:10%">
        <col style="width:20%">
        <col style="width:10%">
        <col style="width:60%">
        <thead>
            <tr>
                <th class="head">name</th>
                <th class="head">Available on</th>
                <th class="head">description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <th style="vertical-align: top;">    when</th>
            <td style="vertical-align: top;">    list, container, leaf</td>
            <td style="vertical-align: top;">    If this field is <code class="docutils literal">True</code> the rule will be executed. Otherwise it won't.</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    from</th>
            <td style="vertical-align: top;">    list, container, leaf</td>
            <td style="vertical-align: top;">    Under normal circumstances</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    path</th>
            <td style="vertical-align: top;">    list, container, leaf</td>
            <td style="vertical-align: top;">    Which attributes to advanced. See <a href="examples_list.html">examples_lists</a> for details.</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    default</th>
            <td style="vertical-align: top;">    list, container, leaf</td>
            <td style="vertical-align: top;">    If ``path`` fails to resolve assign this value to the resolved object</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    key</th>
            <td style="vertical-align: top;">    list</td>
            <td style="vertical-align: top;">    Post processing/formatting of the key value</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    regexp</th>
            <td style="vertical-align: top;">    list, leaf</td>
            <td style="vertical-align: top;">    On <b>lists</b> regexp will be applied over the key. Use it to filter results and capture extra data.</br>
    On <b>leaves</b>, regexp will assign as value the capture group <code class="docutils literal">value</code></td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    pre</th>
            <td style="vertical-align: top;">    leaf</td>
            <td style="vertical-align: top;">    Pre processing/formatting of the value. Useful when you want to statically set it based on ``when`` conditions or from values extracted previously in parent containers/leaves/lists.</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    value</th>
            <td style="vertical-align: top;">    leaf</td>
            <td style="vertical-align: top;">    Post processing/formatting of the value. Useful when you need to combine data extracted in a regular expression or post-process it with a jinja2 filter to transform the value.</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    map</th>
            <td style="vertical-align: top;">    leaf</td>
            <td style="vertical-align: top;">    When a map (dictionary) is provided, the value will be *resolved* using it assigning the
    new corresponding value.</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    present</th>
            <td style="vertical-align: top;">    leaf</td>
            <td style="vertical-align: top;">    If <code class="docutils literal">present: yes</code> value will be <code class="docutils literal">True</code> if <code class="docutils literal">path</code> resolves properly. If <code class="docutils literal">present: no</code> value
    will be <code class="docutils literal">True</code> if <code class="docutils literal">path</code> can't find the attribute. In the rest of the cases the value
    will be <code class="docutils literal">False</code></td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    gate</th>
            <td style="vertical-align: top;">    leaf, container, leaf</td>
            <td style="vertical-align: top;">    If <code class="docutils literal">gate</code> is present with any value we will stop traversing the tree. This is mostly useful in containers
    as you can stop processing a branch under conditions where you know you will not find a match.</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    attribute</th>
            <td style="vertical-align: top;">    leaf</td>
            <td style="vertical-align: top;">    This attribute is specific to the XMLParser. XML documents can add information in the form of attributes.
    You can complement a <code class="docutils literal">path</code> with this field to extract the attribute from the element found in <code class="docutils literal">path</code>.</td>
        </tr>
            </tbody>
    </table></div>