
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/global/reserved-label-blocks/reserved-label-block/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the label block.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_id','__lower_bound','__upper_bound',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lower_bound = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="lower-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    self.__upper_bound = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="upper-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global', u'reserved-label-blocks', u'reserved-label-block', u'config']

  def _get_local_id(self):
    """
    Getter method for local_id, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/local_id (string)

    YANG Description: A local identifier for the global label block allocation.
    """
    return self.__local_id
      
  def _set_local_id(self, v, load=False):
    """
    Setter method for local_id, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/local_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_id() directly.

    YANG Description: A local identifier for the global label block allocation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__local_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_id(self):
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)


  def _get_lower_bound(self):
    """
    Getter method for lower_bound, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/lower_bound (oc-mplst:mpls-label)

    YANG Description: Lower bound of the global label block. The block is defined to include
this label.
    """
    return self.__lower_bound
      
  def _set_lower_bound(self, v, load=False):
    """
    Setter method for lower_bound, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/lower_bound (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lower_bound is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lower_bound() directly.

    YANG Description: Lower bound of the global label block. The block is defined to include
this label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="lower-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lower_bound must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="lower-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)""",
        })

    self.__lower_bound = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lower_bound(self):
    self.__lower_bound = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="lower-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)


  def _get_upper_bound(self):
    """
    Getter method for upper_bound, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/upper_bound (oc-mplst:mpls-label)

    YANG Description: Upper bound for the global label block. The block is defined to include
this label.
    """
    return self.__upper_bound
      
  def _set_upper_bound(self, v, load=False):
    """
    Setter method for upper_bound, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/upper_bound (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_upper_bound is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_upper_bound() directly.

    YANG Description: Upper bound for the global label block. The block is defined to include
this label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="upper-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """upper_bound must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="upper-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)""",
        })

    self.__upper_bound = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_upper_bound(self):
    self.__upper_bound = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="upper-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)

  local_id = __builtin__.property(_get_local_id, _set_local_id)
  lower_bound = __builtin__.property(_get_lower_bound, _set_lower_bound)
  upper_bound = __builtin__.property(_get_upper_bound, _set_upper_bound)


  _pyangbind_elements = {'local_id': local_id, 'lower_bound': lower_bound, 'upper_bound': upper_bound, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/global/reserved-label-blocks/reserved-label-block/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the label block.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_id','__lower_bound','__upper_bound',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lower_bound = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="lower-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    self.__upper_bound = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="upper-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global', u'reserved-label-blocks', u'reserved-label-block', u'config']

  def _get_local_id(self):
    """
    Getter method for local_id, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/local_id (string)

    YANG Description: A local identifier for the global label block allocation.
    """
    return self.__local_id
      
  def _set_local_id(self, v, load=False):
    """
    Setter method for local_id, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/local_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_id() directly.

    YANG Description: A local identifier for the global label block allocation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__local_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_id(self):
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)


  def _get_lower_bound(self):
    """
    Getter method for lower_bound, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/lower_bound (oc-mplst:mpls-label)

    YANG Description: Lower bound of the global label block. The block is defined to include
this label.
    """
    return self.__lower_bound
      
  def _set_lower_bound(self, v, load=False):
    """
    Setter method for lower_bound, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/lower_bound (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lower_bound is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lower_bound() directly.

    YANG Description: Lower bound of the global label block. The block is defined to include
this label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="lower-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lower_bound must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="lower-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)""",
        })

    self.__lower_bound = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lower_bound(self):
    self.__lower_bound = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="lower-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)


  def _get_upper_bound(self):
    """
    Getter method for upper_bound, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/upper_bound (oc-mplst:mpls-label)

    YANG Description: Upper bound for the global label block. The block is defined to include
this label.
    """
    return self.__upper_bound
      
  def _set_upper_bound(self, v, load=False):
    """
    Setter method for upper_bound, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block/config/upper_bound (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_upper_bound is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_upper_bound() directly.

    YANG Description: Upper bound for the global label block. The block is defined to include
this label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="upper-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """upper_bound must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="upper-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)""",
        })

    self.__upper_bound = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_upper_bound(self):
    self.__upper_bound = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="upper-bound", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=True)

  local_id = __builtin__.property(_get_local_id, _set_local_id)
  lower_bound = __builtin__.property(_get_lower_bound, _set_lower_bound)
  upper_bound = __builtin__.property(_get_upper_bound, _set_upper_bound)


  _pyangbind_elements = {'local_id': local_id, 'lower_bound': lower_bound, 'upper_bound': upper_bound, }


