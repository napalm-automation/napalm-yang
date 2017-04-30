napalm-yang
===========

`YANG (RFC6020) <https://tools.ietf.org/html/rfc6020>`_ is a data modelling language, it's a way of defining how data is supposed to look like. The `napalm-yang <https://github.com/napalm-automation/napalm-yang>`_ library provides a framework to use models defined with YANG in the context of network management. It provides mechanisms to transform native data/config into YANG and vice versa.

You can take a look to the following `tutorial <https://github.com/napalm-automation/napalm-yang/blob/develop/interactive_demo/tutorial.ipynb>`_ to see what this is about and how to get started.

Installation
------------

To install ``napalm-yang`` you can use pip as with any other driver::

    pip install -U napalm-yang

Documentation
-------------

.. toctree::
   :maxdepth: 1

   yang/profiles
   yang/basics
   yang/writing_profiles
   yang/parsers
   yang/parsers/XMLParser
   yang/parsers/TextParser
   yang/translators
   yang/translators/XMLTranslator
   yang/translators/TextTranslator
   yang/api
   yang/jinja_filters
