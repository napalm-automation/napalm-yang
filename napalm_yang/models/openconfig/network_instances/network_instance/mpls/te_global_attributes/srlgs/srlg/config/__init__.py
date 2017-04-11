
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/te-global-attributes/srlgs/srlg/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters related to the SRLG
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__value','__cost','__flooding_type',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    self.__flooding_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FLOODED_SRLG': {}, u'STATIC_SRLG': {}},), default=unicode("FLOODED_SRLG"), is_leaf=True, yang_name="flooding-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='mpls-srlg-flooding-type', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'te-global-attributes', u'srlgs', u'srlg', u'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/name (string)

    YANG Description: SRLG group identifier
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: SRLG group identifier
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/value (uint32)

    YANG Description: group ID for the SRLG
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: group ID for the SRLG
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _get_cost(self):
    """
    Getter method for cost, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/cost (uint32)

    YANG Description: The cost of the SRLG to the computation
algorithm
    """
    return self.__cost
      
  def _set_cost(self, v, load=False):
    """
    Setter method for cost, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/cost (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cost is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cost() directly.

    YANG Description: The cost of the SRLG to the computation
algorithm
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cost must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__cost = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cost(self):
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _get_flooding_type(self):
    """
    Getter method for flooding_type, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/flooding_type (mpls-srlg-flooding-type)

    YANG Description: The type of SRLG, either flooded in the IGP or
statically configured
    """
    return self.__flooding_type
      
  def _set_flooding_type(self, v, load=False):
    """
    Setter method for flooding_type, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/flooding_type (mpls-srlg-flooding-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flooding_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flooding_type() directly.

    YANG Description: The type of SRLG, either flooded in the IGP or
statically configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FLOODED_SRLG': {}, u'STATIC_SRLG': {}},), default=unicode("FLOODED_SRLG"), is_leaf=True, yang_name="flooding-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='mpls-srlg-flooding-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flooding_type must be of a type compatible with mpls-srlg-flooding-type""",
          'defined-type': "openconfig-network-instance:mpls-srlg-flooding-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FLOODED_SRLG': {}, u'STATIC_SRLG': {}},), default=unicode("FLOODED_SRLG"), is_leaf=True, yang_name="flooding-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='mpls-srlg-flooding-type', is_config=True)""",
        })

    self.__flooding_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flooding_type(self):
    self.__flooding_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FLOODED_SRLG': {}, u'STATIC_SRLG': {}},), default=unicode("FLOODED_SRLG"), is_leaf=True, yang_name="flooding-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='mpls-srlg-flooding-type', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  value = __builtin__.property(_get_value, _set_value)
  cost = __builtin__.property(_get_cost, _set_cost)
  flooding_type = __builtin__.property(_get_flooding_type, _set_flooding_type)


  _pyangbind_elements = {'name': name, 'value': value, 'cost': cost, 'flooding_type': flooding_type, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/te-global-attributes/srlgs/srlg/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters related to the SRLG
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__value','__cost','__flooding_type',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    self.__flooding_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FLOODED_SRLG': {}, u'STATIC_SRLG': {}},), default=unicode("FLOODED_SRLG"), is_leaf=True, yang_name="flooding-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='mpls-srlg-flooding-type', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'te-global-attributes', u'srlgs', u'srlg', u'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/name (string)

    YANG Description: SRLG group identifier
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: SRLG group identifier
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/value (uint32)

    YANG Description: group ID for the SRLG
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: group ID for the SRLG
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _get_cost(self):
    """
    Getter method for cost, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/cost (uint32)

    YANG Description: The cost of the SRLG to the computation
algorithm
    """
    return self.__cost
      
  def _set_cost(self, v, load=False):
    """
    Setter method for cost, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/cost (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cost is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cost() directly.

    YANG Description: The cost of the SRLG to the computation
algorithm
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cost must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__cost = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cost(self):
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _get_flooding_type(self):
    """
    Getter method for flooding_type, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/flooding_type (mpls-srlg-flooding-type)

    YANG Description: The type of SRLG, either flooded in the IGP or
statically configured
    """
    return self.__flooding_type
      
  def _set_flooding_type(self, v, load=False):
    """
    Setter method for flooding_type, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes/srlgs/srlg/config/flooding_type (mpls-srlg-flooding-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flooding_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flooding_type() directly.

    YANG Description: The type of SRLG, either flooded in the IGP or
statically configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FLOODED_SRLG': {}, u'STATIC_SRLG': {}},), default=unicode("FLOODED_SRLG"), is_leaf=True, yang_name="flooding-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='mpls-srlg-flooding-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flooding_type must be of a type compatible with mpls-srlg-flooding-type""",
          'defined-type': "openconfig-network-instance:mpls-srlg-flooding-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FLOODED_SRLG': {}, u'STATIC_SRLG': {}},), default=unicode("FLOODED_SRLG"), is_leaf=True, yang_name="flooding-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='mpls-srlg-flooding-type', is_config=True)""",
        })

    self.__flooding_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flooding_type(self):
    self.__flooding_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FLOODED_SRLG': {}, u'STATIC_SRLG': {}},), default=unicode("FLOODED_SRLG"), is_leaf=True, yang_name="flooding-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='mpls-srlg-flooding-type', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  value = __builtin__.property(_get_value, _set_value)
  cost = __builtin__.property(_get_cost, _set_cost)
  flooding_type = __builtin__.property(_get_flooding_type, _set_flooding_type)


  _pyangbind_elements = {'name': name, 'value': value, 'cost': cost, 'flooding_type': flooding_type, }


