Below you can find all the YANG models supported and which profiles implements which ones. Note that all the iplementations are not necessarily complete, in the next section you can find links to each individual profile so you can instpect them yourself

.. raw:: html


    <div><table border="1" class="docutils">
        <tr>
            <th>Model</th>
                        <th class="head">eos</th>
                        <th class="head">ios</th>
                        <th class="head">junos</th>
                        <th class="head">ios_router</th>
                        <th class="head">nxos</th>
                    </tr>
        <tbody>
                
        <tr>
            <td><a href="http://ops.openconfig.net/branches/master/docs/openconfig-interfaces.html">openconfig-interfaces</a></td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x2705</td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x2705</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x2705</td>
                    </tr>



        
        <tr>
            <td><a href="http://ops.openconfig.net/branches/master/docs/openconfig-network-instance.html">openconfig-network-instance</a></td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                    </tr>



        
        <tr>
            <td><a href="http://ops.openconfig.net/branches/master/docs/openconfig-platform.html">openconfig-platform</a></td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                    </tr>



        
        <tr>
            <td><a href="http://ops.openconfig.net/branches/master/docs/openconfig-vlan.html">openconfig-vlan</a></td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x274C</td>
                    </tr>



        
        <tr>
            <td><a href="http://ops.openconfig.net/branches/master/docs/openconfig-system.html">openconfig-system</a></td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x2705</br>
                state: &nbsp;&nbsp;&#x2705</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                        <td>config: &#x274C</br>
                state: &nbsp;&nbsp;&#x274C</td>
                    </tr>



        </tr>
        </tbody>
    </table></div>

Profiles
========

Profiles are responsible from mapping native data/configuration to a YANG model and viceversa. Below you can find links to all the profiles so you can inspect what each one does.

.. raw:: html

    <div><table border="1" class="docutils">
        <tr>
                        <th class="head">eos</th>
                        <th class="head">ios</th>
                        <th class="head">junos</th>
                        <th class="head">ios_router</th>
                        <th class="head">nxos</th>
                    </tr>
        <tbody>
        <tr>
                        <td>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/eos/parsers/config">parser:config</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/eos/parsers/state">parser:state</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/eos/translators">translator</a>
            </td>
                        <td>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/ios/parsers/config">parser:config</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/ios/parsers/state">parser:state</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/ios/translators">translator</a>
            </td>
                        <td>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/junos/parsers/config">parser:config</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/junos/parsers/state">parser:state</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/junos/translators">translator</a>
            </td>
                        <td>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/ios_router/parsers/config">parser:config</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/ios_router/parsers/state">parser:state</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/ios_router/translators">translator</a>
            </td>
                        <td>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/nxos/parsers/config">parser:config</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/nxos/parsers/state">parser:state</a></br>
                <a href="https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings/nxos/translators">translator</a>
            </td>
                    </tr>
        </tbody>
    </table></div>