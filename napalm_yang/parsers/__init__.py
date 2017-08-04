from napalm_yang.parsers.jsonp import JSONParser
from napalm_yang.parsers.text import TextParser
from napalm_yang.parsers.text_tree import TextTree
from napalm_yang.parsers.xml import XMLParser

from napalm_yang.translators.text import TextTranslator
from napalm_yang.translators.xml import XMLTranslator


def get_parser(parser):
    parsers = {
        "JSONParser": JSONParser,
        "TextParser": TextParser,
        "TextTree": TextTree,
        "XMLParser": XMLParser,
        "TextTranslator": TextTranslator,
        "XMLTranslator": XMLTranslator,
    }
    return parsers[parser]
