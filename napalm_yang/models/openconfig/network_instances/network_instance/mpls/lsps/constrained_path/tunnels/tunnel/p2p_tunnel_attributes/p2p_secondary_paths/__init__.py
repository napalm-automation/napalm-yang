
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import p2p_secondary_path
class p2p_secondary_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-secondary-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Secondary paths for the LSP
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__p2p_secondary_path',)

  _yang_name = 'p2p-secondary-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__p2p_secondary_path = YANGDynClass(base=YANGListType("name",p2p_secondary_path.p2p_secondary_path, yang_name="p2p-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="p2p-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'p2p-tunnel-attributes', u'p2p-secondary-paths']

  def _get_p2p_secondary_path(self):
    """
    Getter method for p2p_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path (list)

    YANG Description: List of p2p primary paths for a tunnel
    """
    return self.__p2p_secondary_path
      
  def _set_p2p_secondary_path(self, v, load=False):
    """
    Setter method for p2p_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_p2p_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_p2p_secondary_path() directly.

    YANG Description: List of p2p primary paths for a tunnel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",p2p_secondary_path.p2p_secondary_path, yang_name="p2p-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="p2p-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """p2p_secondary_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",p2p_secondary_path.p2p_secondary_path, yang_name="p2p-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="p2p-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__p2p_secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_p2p_secondary_path(self):
    self.__p2p_secondary_path = YANGDynClass(base=YANGListType("name",p2p_secondary_path.p2p_secondary_path, yang_name="p2p-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="p2p-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  p2p_secondary_path = __builtin__.property(_get_p2p_secondary_path, _set_p2p_secondary_path)


  _pyangbind_elements = {'p2p_secondary_path': p2p_secondary_path, }


import p2p_secondary_path
class p2p_secondary_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-secondary-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Secondary paths for the LSP
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__p2p_secondary_path',)

  _yang_name = 'p2p-secondary-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__p2p_secondary_path = YANGDynClass(base=YANGListType("name",p2p_secondary_path.p2p_secondary_path, yang_name="p2p-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="p2p-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'p2p-tunnel-attributes', u'p2p-secondary-paths']

  def _get_p2p_secondary_path(self):
    """
    Getter method for p2p_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path (list)

    YANG Description: List of p2p primary paths for a tunnel
    """
    return self.__p2p_secondary_path
      
  def _set_p2p_secondary_path(self, v, load=False):
    """
    Setter method for p2p_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_p2p_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_p2p_secondary_path() directly.

    YANG Description: List of p2p primary paths for a tunnel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",p2p_secondary_path.p2p_secondary_path, yang_name="p2p-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="p2p-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """p2p_secondary_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",p2p_secondary_path.p2p_secondary_path, yang_name="p2p-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="p2p-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__p2p_secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_p2p_secondary_path(self):
    self.__p2p_secondary_path = YANGDynClass(base=YANGListType("name",p2p_secondary_path.p2p_secondary_path, yang_name="p2p-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="p2p-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  p2p_secondary_path = __builtin__.property(_get_p2p_secondary_path, _set_p2p_secondary_path)


  _pyangbind_elements = {'p2p_secondary_path': p2p_secondary_path, }


