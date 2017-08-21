
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/bandwidth/auto-bandwidth/underflow/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Config information for MPLS underflow bandwidth
adjustment
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__underflow_threshold','__trigger_event_count',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__trigger_event_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="trigger-event-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__underflow_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="underflow-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'bandwidth', u'auto-bandwidth', u'underflow', u'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/enabled (boolean)

    YANG Description: enables bandwidth underflow
adjustment on the lsp
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: enables bandwidth underflow
adjustment on the lsp
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_underflow_threshold(self):
    """
    Getter method for underflow_threshold, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/underflow_threshold (oc-types:percentage)

    YANG Description: bandwidth percentage change to trigger
and underflow event
    """
    return self.__underflow_threshold
      
  def _set_underflow_threshold(self, v, load=False):
    """
    Setter method for underflow_threshold, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/underflow_threshold (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_underflow_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_underflow_threshold() directly.

    YANG Description: bandwidth percentage change to trigger
and underflow event
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="underflow-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """underflow_threshold must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="underflow-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)""",
        })

    self.__underflow_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_underflow_threshold(self):
    self.__underflow_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="underflow-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)


  def _get_trigger_event_count(self):
    """
    Getter method for trigger_event_count, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/trigger_event_count (uint16)

    YANG Description: number of consecutive underflow sample
events needed to trigger an underflow adjustment
    """
    return self.__trigger_event_count
      
  def _set_trigger_event_count(self, v, load=False):
    """
    Setter method for trigger_event_count, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/trigger_event_count (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trigger_event_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trigger_event_count() directly.

    YANG Description: number of consecutive underflow sample
events needed to trigger an underflow adjustment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="trigger-event-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trigger_event_count must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="trigger-event-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)""",
        })

    self.__trigger_event_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trigger_event_count(self):
    self.__trigger_event_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="trigger-event-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  underflow_threshold = __builtin__.property(_get_underflow_threshold, _set_underflow_threshold)
  trigger_event_count = __builtin__.property(_get_trigger_event_count, _set_trigger_event_count)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('underflow_threshold', underflow_threshold), ('trigger_event_count', trigger_event_count), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/bandwidth/auto-bandwidth/underflow/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Config information for MPLS underflow bandwidth
adjustment
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__underflow_threshold','__trigger_event_count',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__trigger_event_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="trigger-event-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__underflow_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="underflow-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'bandwidth', u'auto-bandwidth', u'underflow', u'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/enabled (boolean)

    YANG Description: enables bandwidth underflow
adjustment on the lsp
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: enables bandwidth underflow
adjustment on the lsp
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_underflow_threshold(self):
    """
    Getter method for underflow_threshold, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/underflow_threshold (oc-types:percentage)

    YANG Description: bandwidth percentage change to trigger
and underflow event
    """
    return self.__underflow_threshold
      
  def _set_underflow_threshold(self, v, load=False):
    """
    Setter method for underflow_threshold, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/underflow_threshold (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_underflow_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_underflow_threshold() directly.

    YANG Description: bandwidth percentage change to trigger
and underflow event
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="underflow-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """underflow_threshold must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="underflow-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)""",
        })

    self.__underflow_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_underflow_threshold(self):
    self.__underflow_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="underflow-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)


  def _get_trigger_event_count(self):
    """
    Getter method for trigger_event_count, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/trigger_event_count (uint16)

    YANG Description: number of consecutive underflow sample
events needed to trigger an underflow adjustment
    """
    return self.__trigger_event_count
      
  def _set_trigger_event_count(self, v, load=False):
    """
    Setter method for trigger_event_count, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/auto_bandwidth/underflow/config/trigger_event_count (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trigger_event_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trigger_event_count() directly.

    YANG Description: number of consecutive underflow sample
events needed to trigger an underflow adjustment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="trigger-event-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trigger_event_count must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="trigger-event-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)""",
        })

    self.__trigger_event_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trigger_event_count(self):
    self.__trigger_event_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="trigger-event-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  underflow_threshold = __builtin__.property(_get_underflow_threshold, _set_underflow_threshold)
  trigger_event_count = __builtin__.property(_get_trigger_event_count, _set_trigger_event_count)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('underflow_threshold', underflow_threshold), ('trigger_event_count', trigger_event_count), ])


