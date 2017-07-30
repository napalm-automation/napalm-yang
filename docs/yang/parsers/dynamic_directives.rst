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
            <td style="vertical-align: top;">    If this field is ``True`` the rule will be executed. Otherwise it won't.</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    from</th>
            <td style="vertical-align: top;">    list, container, leaf</td>
            <td style="vertical-align: top;">    Under normal circumstances</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    path</th>
            <td style="vertical-align: top;">    list, container, leaf</td>
            <td style="vertical-align: top;">    Which attributes to advanced. See (link here to blah) for details.</td>
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
    On <b>leaves</b>, regexp will assign as value the capture group ``value``</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    value</th>
            <td style="vertical-align: top;">    leaf</td>
            <td style="vertical-align: top;">    Post processing/formatting of the value</td>
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
            <td style="vertical-align: top;">    If ``present: yes`` value will be ``True`` if ``path`` resolves properly. If ``present: no`` value
    will be ``True`` if ``path`` can't find the attribute. In the rest of the cases the value
    will be ``False``</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    gate</th>
            <td style="vertical-align: top;">    leaf, container, leaf</td>
            <td style="vertical-align: top;">    If ``gate`` is present with any value we will stop traversing the tree. This is mostly useful in containers
    as you can stop processing a branch under conditions where you know you will not find a match.</td>
        </tr>
            <tr>
            <th style="vertical-align: top;">    attribute</th>
            <td style="vertical-align: top;">    leaf</td>
            <td style="vertical-align: top;">    This attribute is specific to the XMLParser. XML documents can add information in the form of attributes.
    You can complement a ``path`` with this field to extract the attribute from the element found in ``path``.</td>
        </tr>
            </tbody>
    </table></div>