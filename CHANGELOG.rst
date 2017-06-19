0.0.2
+++++

    - Translators now accept ``continue_negating`` option
    - YAML files can now include other files via the ``!include relative/path/to/file.yaml`` directive
    - ``TextParser``, ``list - block`` supports manual keys via the ``key`` argument
    - ``TextParser``, ``list - block`` now supports flat list of commands (i.e. BGP neighbors and static routes) via the ``flat`` argument
    - ``TextParser``, ``list - block`` now supports composite keys via the ``composite_key`` argument
    - ``TextParser``, ``list - block`` now supports creating elements manually via the ``mandatory`` argument

    - Move mandatory elements previously on the default action to a dedicated action
    - from is optional, by default it will always follow the parent
    - from is now a pointer, no need to keep serializing/deserializing
    - mode is optional. All parsers have a main "default" action now.
    - JSONParser added

0.0.1
+++++

    - Initial version
