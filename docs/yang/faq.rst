FAQ
===

Some YAML files are insanely largely. Can I break them down into multiple files?
________________________________________________________________________________

    Yes, you can with the ``!include relative/path/to/file.yaml`` directive. For example::

        # ./main.yaml
        my_key:
            blah: asdasdasd
            bleh: !include includes/bleh.yaml

        # ./includes/bleh.yaml
        qwe: 1
        asd: 2

    Will result in the final object::

        my_key:
            blah: asdasdasd
            bleh:
                qwe: 1
                asd: 2
