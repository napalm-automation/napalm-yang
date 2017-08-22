
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

from . import table
class tables(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/tables. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The routing tables that are managed by this network
instance
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__table',)

  _yang_name = 'tables'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__table = YANGDynClass(base=YANGListType("protocol address_family",table.table, yang_name="table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='protocol address-family', extensions=None), is_container='list', yang_name="table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'tables']

  def _get_table(self):
    """
    Getter method for table, mapped from YANG variable /network_instances/network_instance/tables/table (list)

    YANG Description: A network instance manages one or more forwarding or
routing tables. These may reflect a Layer 2 forwarding
information base, a Layer 3 routing table, or an MPLS
LFIB.

The table populated by a protocol within an instance is
identified by the protocol identifier (e.g., BGP, IS-IS)
and the address family (e.g., IPv4, IPv6) supported by
that protocol. Multiple instances of the same protocol
populate a single table -- such that
a single IS-IS or OSPF IPv4 table exists per network
instance.

An implementation is expected to create entries within
this list when the relevant protocol context is enabled.
i.e., when a BGP instance is created with IPv4 and IPv6
address families enabled, the protocol=BGP,
address-family=IPv4 table is created by the system.
    """
    return self.__table
      
  def _set_table(self, v, load=False):
    """
    Setter method for table, mapped from YANG variable /network_instances/network_instance/tables/table (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_table() directly.

    YANG Description: A network instance manages one or more forwarding or
routing tables. These may reflect a Layer 2 forwarding
information base, a Layer 3 routing table, or an MPLS
LFIB.

The table populated by a protocol within an instance is
identified by the protocol identifier (e.g., BGP, IS-IS)
and the address family (e.g., IPv4, IPv6) supported by
that protocol. Multiple instances of the same protocol
populate a single table -- such that
a single IS-IS or OSPF IPv4 table exists per network
instance.

An implementation is expected to create entries within
this list when the relevant protocol context is enabled.
i.e., when a BGP instance is created with IPv4 and IPv6
address families enabled, the protocol=BGP,
address-family=IPv4 table is created by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("protocol address_family",table.table, yang_name="table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='protocol address-family', extensions=None), is_container='list', yang_name="table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """table must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("protocol address_family",table.table, yang_name="table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='protocol address-family', extensions=None), is_container='list', yang_name="table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_table(self):
    self.__table = YANGDynClass(base=YANGListType("protocol address_family",table.table, yang_name="table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='protocol address-family', extensions=None), is_container='list', yang_name="table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  table = __builtin__.property(_get_table, _set_table)


  _pyangbind_elements = {'table': table, }


from . import table
class tables(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/tables. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The routing tables that are managed by this network
instance
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__table',)

  _yang_name = 'tables'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__table = YANGDynClass(base=YANGListType("protocol address_family",table.table, yang_name="table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='protocol address-family', extensions=None), is_container='list', yang_name="table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'tables']

  def _get_table(self):
    """
    Getter method for table, mapped from YANG variable /network_instances/network_instance/tables/table (list)

    YANG Description: A network instance manages one or more forwarding or
routing tables. These may reflect a Layer 2 forwarding
information base, a Layer 3 routing table, or an MPLS
LFIB.

The table populated by a protocol within an instance is
identified by the protocol identifier (e.g., BGP, IS-IS)
and the address family (e.g., IPv4, IPv6) supported by
that protocol. Multiple instances of the same protocol
populate a single table -- such that
a single IS-IS or OSPF IPv4 table exists per network
instance.

An implementation is expected to create entries within
this list when the relevant protocol context is enabled.
i.e., when a BGP instance is created with IPv4 and IPv6
address families enabled, the protocol=BGP,
address-family=IPv4 table is created by the system.
    """
    return self.__table
      
  def _set_table(self, v, load=False):
    """
    Setter method for table, mapped from YANG variable /network_instances/network_instance/tables/table (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_table() directly.

    YANG Description: A network instance manages one or more forwarding or
routing tables. These may reflect a Layer 2 forwarding
information base, a Layer 3 routing table, or an MPLS
LFIB.

The table populated by a protocol within an instance is
identified by the protocol identifier (e.g., BGP, IS-IS)
and the address family (e.g., IPv4, IPv6) supported by
that protocol. Multiple instances of the same protocol
populate a single table -- such that
a single IS-IS or OSPF IPv4 table exists per network
instance.

An implementation is expected to create entries within
this list when the relevant protocol context is enabled.
i.e., when a BGP instance is created with IPv4 and IPv6
address families enabled, the protocol=BGP,
address-family=IPv4 table is created by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("protocol address_family",table.table, yang_name="table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='protocol address-family', extensions=None), is_container='list', yang_name="table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """table must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("protocol address_family",table.table, yang_name="table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='protocol address-family', extensions=None), is_container='list', yang_name="table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_table(self):
    self.__table = YANGDynClass(base=YANGListType("protocol address_family",table.table, yang_name="table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='protocol address-family', extensions=None), is_container='list', yang_name="table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  table = __builtin__.property(_get_table, _set_table)


  _pyangbind_elements = {'table': table, }


