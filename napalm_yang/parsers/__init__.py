from napalm_yang.parsers.jsonp import JSONParser
from napalm_yang.parsers.junos_config import JunosConfig
from napalm_yang.parsers.text import TextParser
from napalm_yang.parsers.text_tree import TextTree
from napalm_yang.parsers.xml import XMLParser

from napalm_yang.translators.text import TextTranslator
from napalm_yang.translators.junos import JunosTranslator
from napalm_yang.translators.xml import XMLTranslator


def get_parser(parser):
    parsers = {
        "JSONParser": JSONParser,
        "JunosConfig": JunosConfig,
        "TextParser": TextParser,
        "TextTree": TextTree,
        "XMLParser": XMLParser,
        "TextTranslator": TextTranslator,
        "JunosTranslator": JunosTranslator,
        "XMLTranslator": XMLTranslator,
    }
    return parsers[parser]
