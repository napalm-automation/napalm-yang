from napalm_yang.parsers.jsonp import JSONParser
from napalm_yang.parsers.text import TextParser
from napalm_yang.parsers.text_tree import TextTree
from napalm_yang.parsers.xml import XMLParser

from napalm_yang.translators.text import TextTranslator
from napalm_yang.translators.xml import XMLTranslator
from napalm_yang.translators.jsont import JSONTranslator


def get_parser(parser):
    parsers = {
        "JSONParser": JSONParser,
        "TextParser": TextParser,
        "TextTree": TextTree,
        "XMLParser": XMLParser,
        "TextTranslator": TextTranslator,
        "XMLTranslator": XMLTranslator,
        "JSONTranslator": JSONTranslator
    }
    return parsers[parser]
