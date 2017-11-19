from napalm_yang.translators.xml import XMLTranslator

from lxml import etree
import json
from collections import defaultdict

import logging
logger = logging.getLogger("napalm-yang")

class JSONTranslator(XMLTranslator):

    def post_processing(self, translator):
        data = etree_to_dict(translator.translation)
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.iteritems():
                dd[k].append(v)
        d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in sorted(dd.iteritems(), key=lambda (k,v): (v,k))}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in sorted(t.attrib.iteritems()))
    if t.text:
        text = t.text.strip()
        if text == "True":
            text = True
        if text == "False":
            text = False
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d
