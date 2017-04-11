
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/use-multiple-paths/ebgp/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to eBGP multipath
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__allow_multiple_as','__maximum_paths',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__maximum_paths = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    self.__allow_multiple_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'use-multiple-paths', u'ebgp', u'config']

  def _get_allow_multiple_as(self):
    """
    Getter method for allow_multiple_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp/config/allow_multiple_as (boolean)

    YANG Description: Allow multipath to use paths from different neighbouring
ASes.  The default is to only consider multiple paths from
the same neighbouring AS.
    """
    return self.__allow_multiple_as
      
  def _set_allow_multiple_as(self, v, load=False):
    """
    Setter method for allow_multiple_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp/config/allow_multiple_as (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allow_multiple_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allow_multiple_as() directly.

    YANG Description: Allow multipath to use paths from different neighbouring
ASes.  The default is to only consider multiple paths from
the same neighbouring AS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allow_multiple_as must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__allow_multiple_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allow_multiple_as(self):
    self.__allow_multiple_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_maximum_paths(self):
    """
    Getter method for maximum_paths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp/config/maximum_paths (uint32)

    YANG Description: Maximum number of parallel paths to consider when using
BGP multipath. The default is use a single path.
    """
    return self.__maximum_paths
      
  def _set_maximum_paths(self, v, load=False):
    """
    Setter method for maximum_paths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp/config/maximum_paths (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maximum_paths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maximum_paths() directly.

    YANG Description: Maximum number of parallel paths to consider when using
BGP multipath. The default is use a single path.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maximum_paths must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__maximum_paths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maximum_paths(self):
    self.__maximum_paths = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)

  allow_multiple_as = __builtin__.property(_get_allow_multiple_as, _set_allow_multiple_as)
  maximum_paths = __builtin__.property(_get_maximum_paths, _set_maximum_paths)


  _pyangbind_elements = {'allow_multiple_as': allow_multiple_as, 'maximum_paths': maximum_paths, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/use-multiple-paths/ebgp/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to eBGP multipath
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__allow_multiple_as','__maximum_paths',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__maximum_paths = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    self.__allow_multiple_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'use-multiple-paths', u'ebgp', u'config']

  def _get_allow_multiple_as(self):
    """
    Getter method for allow_multiple_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp/config/allow_multiple_as (boolean)

    YANG Description: Allow multipath to use paths from different neighbouring
ASes.  The default is to only consider multiple paths from
the same neighbouring AS.
    """
    return self.__allow_multiple_as
      
  def _set_allow_multiple_as(self, v, load=False):
    """
    Setter method for allow_multiple_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp/config/allow_multiple_as (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allow_multiple_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allow_multiple_as() directly.

    YANG Description: Allow multipath to use paths from different neighbouring
ASes.  The default is to only consider multiple paths from
the same neighbouring AS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allow_multiple_as must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__allow_multiple_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allow_multiple_as(self):
    self.__allow_multiple_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_maximum_paths(self):
    """
    Getter method for maximum_paths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp/config/maximum_paths (uint32)

    YANG Description: Maximum number of parallel paths to consider when using
BGP multipath. The default is use a single path.
    """
    return self.__maximum_paths
      
  def _set_maximum_paths(self, v, load=False):
    """
    Setter method for maximum_paths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp/config/maximum_paths (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maximum_paths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maximum_paths() directly.

    YANG Description: Maximum number of parallel paths to consider when using
BGP multipath. The default is use a single path.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maximum_paths must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__maximum_paths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maximum_paths(self):
    self.__maximum_paths = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)

  allow_multiple_as = __builtin__.property(_get_allow_multiple_as, _set_allow_multiple_as)
  maximum_paths = __builtin__.property(_get_maximum_paths, _set_maximum_paths)


  _pyangbind_elements = {'allow_multiple_as': allow_multiple_as, 'maximum_paths': maximum_paths, }


