import ast


from napalm_yang.supported_models import SUPPORTED_MODELS
from napalm_yang.parser import Parser
from napalm_yang.translator import Translator

from napalm_base import validate


from pyangbind.lib import yangtypes


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

    def add_model(self, model, force=False):
        """
        Add a model.

        The model will be asssigned to a class attribute with the YANG name of the model.

        Args:
            model (PybindBase): Model to add.
            force (bool): If not set, verify the model is in SUPPORTED_MODELS

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

        if model._yang_name not in [a[0] for a in SUPPORTED_MODELS]:
            raise ValueError("Only models in SUPPORTED_MODELS can be added without `force=True`")

        for k, v in model:
            self._elements[k] = v
            setattr(self, k, v)

    def get(self, filter=False):
        """
        Returns a dictionary with the values of the model. Note that the values
        of the leafs are YANG classes.

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
            _load_dict(attr, v)

    def to_dict(self, filter=True):
        """
        Returns a dictionary with the values of the model. Note that the values
        of the leafs are evaluated to python types.

        Args:
            filter (bool): If set to ``True``, show only values that have been set.

        Returns:
            dict: A dictionary with the values of the model.

        Example:

            >>> pretty_print(config.to_dict(filter=True))
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
        for k, v in self:
            r = _to_dict(v, filter)
            if r:
                result[k] = r
        return result

    def parse_config(self, device=None, profile=None, native=None, attrs=None):
        """
        Parse native configuration and load it into the corresponding models. Only models
        that have been added to the root object will be parsed.

        If ``native`` is passed to the method that's what we will parse, otherwise, we will use the
        ``device`` to retrieve it.

        Args:
            device (NetworkDriver): Device to load the configuration from.
            profile (list): Profiles that the device supports. If no ``profile`` is passed it will
              be read from ``device``.
            native (list of strings): Native configuration to parse.

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
            >>> running_config.parse_config(native=config, profile="junos")
        """
        if attrs is None:
            attrs = self.elements().values()

        for v in attrs:
            parser = Parser(v, device=device, profile=profile, native=native, is_config=True)
            parser.parse()

    def parse_state(self, device=None, profile=None, native=None, attrs=None):
        """
        Parse native state and load it into the corresponding models. Only models
        that have been added to the root object will be parsed.

        If ``native`` is passed to the method that's what we will parse, otherwise, we will use the
        ``device`` to retrieve it.

        Args:
            device (NetworkDriver): Device to load the configuration from.
            profile (list): Profiles that the device supports. If no ``profile`` is passed it will
              be read from ``device``.
            native (list string): Native output to parse.

        Examples:

            >>> # Load from device
            >>> state = napalm_yang.base.Root()
            >>> state.add_model(napalm_yang.models.openconfig_interfaces)
            >>> state.parse_config(device=d)

            >>> # Load from file
            >>> with open("junos.state", "r") as f:
            >>>     state_data = f.read()
            >>>
            >>> state = napalm_yang.base.Root()
            >>> state.add_model(napalm_yang.models.openconfig_interfaces)
            >>> state.parse_config(native=state_data, profile="junos")
        """
        if attrs is None:
            attrs = self.elements().values()

        for v in attrs:
            parser = Parser(v, device=device, profile=profile, native=native, is_config=False)
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

    def compliance_report(self, validation_file='validate.yml'):
        """
        Return a compliance report.
        Verify that the device complies with the given validation file and writes a compliance
        report file. See https://napalm.readthedocs.io/en/latest/validate.html.
        """
        return validate.compliance_report(self, validation_file=validation_file)


def _load_dict(cls, data):
    for k, v in data.items():
        if cls._yang_type == "list":
            try:
                attr = cls[k]
            except KeyError:
                attr = cls.add(k)
            _load_dict(attr, v)
        elif isinstance(v, dict):
            attr = getattr(cls, yangtypes.safe_name(k))
            _load_dict(attr, v)
        else:
            model = getattr(cls, yangtypes.safe_name(k))

            # We can't set attributes that are keys
            if model._is_keyval:
                continue

            setter = getattr(cls, "_set_{}".format(yangtypes.safe_name(k)))
            setter(v)

            model = getattr(model._parent, yangtypes.safe_name(k))
            model._mchanged = True


def _to_dict(element, filter):
    if isinstance(element, Root) or element._yang_type in ("container", None):
        result = _to_dict_container(element, filter)
    elif element._yang_type in ("list", ):
        result = _to_dict_list(element, filter)
    else:
        result = _to_dict_leaf(element, filter)

    return result


def _to_dict_container(element, filter):
    result = {}

    for k in element.elements():
        v = getattr(element, k)
        r = _to_dict(v, filter)
        if r not in [None, {}]:
            result[k] = r
    return result


def _to_dict_list(element, filter):
    result = {}

    for k, v in element.items():
        r = _to_dict(v, filter)
        if r not in [None, {}]:
            result[k] = r
    return result


def _to_dict_leaf(element, filter):
    value = None
    if element._changed() or not filter:
        try:
            value = ast.literal_eval(element.__repr__())
        except Exception:
            value = element.__repr__()

    return value
