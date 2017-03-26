from pyangbind.lib.serialise import pybindJSONDecoder

from napalm_yang.parser import Parser
from napalm_yang.translator import Translator


class Root(object):
    """
    This is a container you can use as root for your other models.

    Examples:

        >>> config = napalm_yang.base.Root()
        >>>
        >>> # Adding models to the object
        >>> config.add_model(napalm_yang.models.openconfig_interfaces())
        >>> config.add_model(napalm_yang.models.openconfig_vlan())

    """
    _yang_type = "container"
    _defining_module = ""

    def __init__(self):
        self._elements = {}

    def elements(self):
        return self._elements
    "base",

    def add_model(self, model):
        """
        Add a model.

        The model will be asssigned to a class attribute with the YANG name of the model.

        Args:
            model (PybindBase): Model to add.

        Examples:

            >>> import napalm_yang
            >>> config = napalm_yang.base.Root()
            >>> config.add_model(napalm_yang.models.openconfig_interfaces)
            >>> config.interfaces
            <pyangbind.lib.yangtypes.YANGBaseClass object at 0x10bef6680>
        """
        try:
            model = model()
        except Exception:
            pass

        for k, v in model:
            self._elements[k] = v
            setattr(self, k, v)

    def get(self, filter=False):
        """
        Returns a dictionary with the values of the model.

        Args:
            filter (bool): If set to ``True``, show only values that have been set.

        Returns:
            dict: A dictionary with the values of the model.

        Example:

            >>> pretty_print(config.get(filter=True))
            >>> {
            >>>     "interfaces": {
            >>>         "interface": {
            >>>             "et1": {
            >>>                 "config": {
            >>>                     "description": "My description",
            >>>                     "mtu": 1500
            >>>                 },
            >>>                 "name": "et1"
            >>>             },
            >>>             "et2": {
            >>>                 "config": {
            >>>                     "description": "Another description",
            >>>                     "mtu": 9000
            >>>                 },
            >>>                 "name": "et2"
            >>>             }
            >>>         }
            >>>     }
            >>> }

        """
        result = {}

        for k, v in self.elements().items():
            intermediate = v.get(filter=filter)
            if intermediate:
                result[k] = intermediate

        return result

    def __iter__(self):
        for k, v in self.elements().items():
            yield k, v

    def load_dict(self, data, overwrite=False):
        """
        Load a dictionary into the model.

        Args:
            data(dict): Dictionary to loead
            overwrite(bool): Whether the data present in the model should be overwritten by the
            data in the dict or not.

        Examples:

            >>> vlans_dict = {
            >>>     "vlans": { "vlan": { 100: {
            >>>                             "config": {
            >>>                                 "vlan_id": 100, "name": "production"}},
            >>>                          200: {
            >>>                             "config": {
            >>>                                 "vlan_id": 200, "name": "dev"}}}}}
            >>> config.load_dict(vlans_dict)
            >>> print(config.vlans.vlan.keys())
            ... [200, 100]
            >>> print(100, config.vlans.vlan[100].config.name)
            ... (100, u'production')
            >>> print(200, config.vlans.vlan[200].config.name)
            ... (200, u'dev')
        """
        for k, v in data.items():
            if k not in self._elements.keys():
                raise AttributeError("Model {} is not loaded".format(k))
            attr = getattr(self, k)
            pybindJSONDecoder.load_json(v, None, None, obj=attr, overwrite=overwrite)

    def parse_config(self, device=None, profile=None, config=None):
        """
        Parse native configuration and load it into the corresponding models. Only models
        that have been added to the root object will be parsed.

        If ``config`` is passed to the method that's what we will parse, otherwise, we will use the
        ``device`` to retrieve it.

        Args:
            device (NetworkDriver): Device to load the configuration from.
            profile (list): Profiles that the device supports. If no ``profile`` is passed it will
              be read from ``device``.
            config (string): Configuration to parse.

        Examples:

            >>> # Load from device
            >>> running_config = napalm_yang.base.Root()
            >>> running_config.add_model(napalm_yang.models.openconfig_interfaces)
            >>> running_config.parse_config(device=d)

            >>> # Load from file
            >>> with open("junos.config", "r") as f:
            >>>     config = f.read()
            >>>
            >>> running_config = napalm_yang.base.Root()
            >>> running_config.add_model(napalm_yang.models.openconfig_interfaces)
            >>> running_config.parse_config(config=config, profile="junos")
        """

        for k, v in self:
            parser = Parser(v, device=device, profile=profile, config=config, is_config=True)
            parser.parse()

    def translate_config(self, profile, merge=None, replace=None):
        """
        Translate the object to native configuration.

        In this context, merge and replace means the following:

        * **Merge** - Elements that exist in both ``self`` and ``merge`` will use by default the
          values in ``merge`` unless ``self`` specifies a new one. Elements that exist only
          in ``self`` will be translated as they are and elements present only in ``merge``
          will be removed.
        * **Replace** - All the elements in ``replace`` will either be removed or replaced by
          elements in ``self``.

        You can specify one of ``merge``, ``replace`` or none of them. If none of them are set we
        will just translate configuration.

        Args:
            profile (list): Which profiles to use.
            merge (Root): Object we want to merge with.
            replace (Root): Object we want to replace.
        """
        result = []
        for k, v in self:
            other_merge = getattr(merge, k) if merge else None
            other_replace = getattr(replace, k) if replace else None
            translator = Translator(v, profile, merge=other_merge, replace=other_replace)
            result.append(translator.translate())

        return "\n".join(result)
