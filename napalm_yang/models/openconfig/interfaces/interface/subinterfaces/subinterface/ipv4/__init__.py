
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

from . import addresses
from . import neighbors
from . import unnumbered
from . import config
from . import state
class ipv4(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/ipv4. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters for the IPv4 address family.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__addresses','__neighbors','__unnumbered','__config','__state',)

  _yang_name = 'ipv4'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    self.__unnumbered = YANGDynClass(base=unnumbered.unnumbered, is_container='container', yang_name="unnumbered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    self.__addresses = YANGDynClass(base=addresses.addresses, is_container='container', yang_name="addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)

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
      return [u'interfaces', u'interface', u'subinterfaces', u'subinterface', u'ipv4']

  def _get_addresses(self):
    """
    Getter method for addresses, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses (container)

    YANG Description: Enclosing container for address list
    """
    return self.__addresses
      
  def _set_addresses(self, v, load=False):
    """
    Setter method for addresses, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addresses is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addresses() directly.

    YANG Description: Enclosing container for address list
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=addresses.addresses, is_container='container', yang_name="addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addresses must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=addresses.addresses, is_container='container', yang_name="addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)""",
        })

    self.__addresses = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addresses(self):
    self.__addresses = YANGDynClass(base=addresses.addresses, is_container='container', yang_name="addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)


  def _get_neighbors(self):
    """
    Getter method for neighbors, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/neighbors (container)

    YANG Description: Enclosing container for neighbor list
    """
    return self.__neighbors
      
  def _set_neighbors(self, v, load=False):
    """
    Setter method for neighbors, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: Enclosing container for neighbor list
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)""",
        })

    self.__neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbors(self):
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)


  def _get_unnumbered(self):
    """
    Getter method for unnumbered, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/unnumbered (container)

    YANG Description: Top-level container for setting unnumbered interfaces.
Includes reference the interface that provides the
address information
    """
    return self.__unnumbered
      
  def _set_unnumbered(self, v, load=False):
    """
    Setter method for unnumbered, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/unnumbered (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unnumbered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unnumbered() directly.

    YANG Description: Top-level container for setting unnumbered interfaces.
Includes reference the interface that provides the
address information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unnumbered.unnumbered, is_container='container', yang_name="unnumbered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unnumbered must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unnumbered.unnumbered, is_container='container', yang_name="unnumbered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)""",
        })

    self.__unnumbered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unnumbered(self):
    self.__unnumbered = YANGDynClass(base=unnumbered.unnumbered, is_container='container', yang_name="unnumbered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/config (container)

    YANG Description: Top-level IPv4 configuration data for the interface
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Top-level IPv4 configuration data for the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/state (container)

    YANG Description: Top level IPv4 operational state data
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Top level IPv4 operational state data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)

  addresses = __builtin__.property(_get_addresses, _set_addresses)
  neighbors = __builtin__.property(_get_neighbors, _set_neighbors)
  unnumbered = __builtin__.property(_get_unnumbered, _set_unnumbered)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = {'addresses': addresses, 'neighbors': neighbors, 'unnumbered': unnumbered, 'config': config, 'state': state, }


