
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/global/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Global configuration parameters for OSPFv2
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__router_id','__summary_route_cost_mode','__igp_shortcuts','__log_adjacency_changes','__hide_transit_only_networks',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=True)
    self.__igp_shortcuts = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-shortcuts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__log_adjacency_changes = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-adjacency-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__hide_transit_only_networks = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hide-transit-only-networks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__summary_route_cost_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'RFC1583_COMPATIBLE': {}, u'RFC2328_COMPATIBLE': {}},), default=unicode("RFC2328_COMPATIBLE"), is_leaf=True, yang_name="summary-route-cost-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'global', u'config']

  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/router_id (yang:dotted-quad)

    YANG Description: A 32-bit number represented as a dotted quad assigned to
each router running the OSPFv2 protocol. This number should
be unique within the autonomous system
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/router_id (yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: A 32-bit number represented as a dotted quad assigned to
each router running the OSPFv2 protocol. This number should
be unique within the autonomous system
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with yang:dotted-quad""",
          'defined-type': "yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=True)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=True)


  def _get_summary_route_cost_mode(self):
    """
    Getter method for summary_route_cost_mode, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/summary_route_cost_mode (enumeration)

    YANG Description: Specify how costs for the summary routes should be specified
as per the behaviour in the original OSPF specification
RFC1583, or alternatively whether the revised behaviour
described in RFC2328 should be utilised
    """
    return self.__summary_route_cost_mode
      
  def _set_summary_route_cost_mode(self, v, load=False):
    """
    Setter method for summary_route_cost_mode, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/summary_route_cost_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_route_cost_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_route_cost_mode() directly.

    YANG Description: Specify how costs for the summary routes should be specified
as per the behaviour in the original OSPF specification
RFC1583, or alternatively whether the revised behaviour
described in RFC2328 should be utilised
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'RFC1583_COMPATIBLE': {}, u'RFC2328_COMPATIBLE': {}},), default=unicode("RFC2328_COMPATIBLE"), is_leaf=True, yang_name="summary-route-cost-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_route_cost_mode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'RFC1583_COMPATIBLE': {}, u'RFC2328_COMPATIBLE': {}},), default=unicode("RFC2328_COMPATIBLE"), is_leaf=True, yang_name="summary-route-cost-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=True)""",
        })

    self.__summary_route_cost_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_route_cost_mode(self):
    self.__summary_route_cost_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'RFC1583_COMPATIBLE': {}, u'RFC2328_COMPATIBLE': {}},), default=unicode("RFC2328_COMPATIBLE"), is_leaf=True, yang_name="summary-route-cost-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=True)


  def _get_igp_shortcuts(self):
    """
    Getter method for igp_shortcuts, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/igp_shortcuts (boolean)

    YANG Description: When this leaf is set to true, OSPFv2 will route traffic to
a remote system via any LSP to the system that is marked as
shortcut eligible.
    """
    return self.__igp_shortcuts
      
  def _set_igp_shortcuts(self, v, load=False):
    """
    Setter method for igp_shortcuts, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/igp_shortcuts (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igp_shortcuts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igp_shortcuts() directly.

    YANG Description: When this leaf is set to true, OSPFv2 will route traffic to
a remote system via any LSP to the system that is marked as
shortcut eligible.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igp-shortcuts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igp_shortcuts must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-shortcuts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__igp_shortcuts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igp_shortcuts(self):
    self.__igp_shortcuts = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-shortcuts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_log_adjacency_changes(self):
    """
    Getter method for log_adjacency_changes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/log_adjacency_changes (boolean)

    YANG Description: When this leaf is set to true, a log message will be
generated when the state of an OSPFv2 neighbour changes.
    """
    return self.__log_adjacency_changes
      
  def _set_log_adjacency_changes(self, v, load=False):
    """
    Setter method for log_adjacency_changes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/log_adjacency_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_adjacency_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_adjacency_changes() directly.

    YANG Description: When this leaf is set to true, a log message will be
generated when the state of an OSPFv2 neighbour changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log-adjacency-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_adjacency_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-adjacency-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__log_adjacency_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_adjacency_changes(self):
    self.__log_adjacency_changes = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-adjacency-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_hide_transit_only_networks(self):
    """
    Getter method for hide_transit_only_networks, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/hide_transit_only_networks (boolean)

    YANG Description: When this leaf is set to true, do not advertise prefixes
into OSPFv2 that correspond to transit interfaces, as per
the behaviour discussed in RFC6860.
    """
    return self.__hide_transit_only_networks
      
  def _set_hide_transit_only_networks(self, v, load=False):
    """
    Setter method for hide_transit_only_networks, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/hide_transit_only_networks (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hide_transit_only_networks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hide_transit_only_networks() directly.

    YANG Description: When this leaf is set to true, do not advertise prefixes
into OSPFv2 that correspond to transit interfaces, as per
the behaviour discussed in RFC6860.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="hide-transit-only-networks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hide_transit_only_networks must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hide-transit-only-networks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__hide_transit_only_networks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hide_transit_only_networks(self):
    self.__hide_transit_only_networks = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hide-transit-only-networks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  router_id = __builtin__.property(_get_router_id, _set_router_id)
  summary_route_cost_mode = __builtin__.property(_get_summary_route_cost_mode, _set_summary_route_cost_mode)
  igp_shortcuts = __builtin__.property(_get_igp_shortcuts, _set_igp_shortcuts)
  log_adjacency_changes = __builtin__.property(_get_log_adjacency_changes, _set_log_adjacency_changes)
  hide_transit_only_networks = __builtin__.property(_get_hide_transit_only_networks, _set_hide_transit_only_networks)


  _pyangbind_elements = {'router_id': router_id, 'summary_route_cost_mode': summary_route_cost_mode, 'igp_shortcuts': igp_shortcuts, 'log_adjacency_changes': log_adjacency_changes, 'hide_transit_only_networks': hide_transit_only_networks, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/global/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Global configuration parameters for OSPFv2
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__router_id','__summary_route_cost_mode','__igp_shortcuts','__log_adjacency_changes','__hide_transit_only_networks',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=True)
    self.__igp_shortcuts = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-shortcuts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__log_adjacency_changes = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-adjacency-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__hide_transit_only_networks = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hide-transit-only-networks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__summary_route_cost_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'RFC1583_COMPATIBLE': {}, u'RFC2328_COMPATIBLE': {}},), default=unicode("RFC2328_COMPATIBLE"), is_leaf=True, yang_name="summary-route-cost-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'global', u'config']

  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/router_id (yang:dotted-quad)

    YANG Description: A 32-bit number represented as a dotted quad assigned to
each router running the OSPFv2 protocol. This number should
be unique within the autonomous system
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/router_id (yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: A 32-bit number represented as a dotted quad assigned to
each router running the OSPFv2 protocol. This number should
be unique within the autonomous system
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with yang:dotted-quad""",
          'defined-type': "yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=True)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=True)


  def _get_summary_route_cost_mode(self):
    """
    Getter method for summary_route_cost_mode, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/summary_route_cost_mode (enumeration)

    YANG Description: Specify how costs for the summary routes should be specified
as per the behaviour in the original OSPF specification
RFC1583, or alternatively whether the revised behaviour
described in RFC2328 should be utilised
    """
    return self.__summary_route_cost_mode
      
  def _set_summary_route_cost_mode(self, v, load=False):
    """
    Setter method for summary_route_cost_mode, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/summary_route_cost_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_route_cost_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_route_cost_mode() directly.

    YANG Description: Specify how costs for the summary routes should be specified
as per the behaviour in the original OSPF specification
RFC1583, or alternatively whether the revised behaviour
described in RFC2328 should be utilised
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'RFC1583_COMPATIBLE': {}, u'RFC2328_COMPATIBLE': {}},), default=unicode("RFC2328_COMPATIBLE"), is_leaf=True, yang_name="summary-route-cost-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_route_cost_mode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'RFC1583_COMPATIBLE': {}, u'RFC2328_COMPATIBLE': {}},), default=unicode("RFC2328_COMPATIBLE"), is_leaf=True, yang_name="summary-route-cost-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=True)""",
        })

    self.__summary_route_cost_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_route_cost_mode(self):
    self.__summary_route_cost_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'RFC1583_COMPATIBLE': {}, u'RFC2328_COMPATIBLE': {}},), default=unicode("RFC2328_COMPATIBLE"), is_leaf=True, yang_name="summary-route-cost-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=True)


  def _get_igp_shortcuts(self):
    """
    Getter method for igp_shortcuts, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/igp_shortcuts (boolean)

    YANG Description: When this leaf is set to true, OSPFv2 will route traffic to
a remote system via any LSP to the system that is marked as
shortcut eligible.
    """
    return self.__igp_shortcuts
      
  def _set_igp_shortcuts(self, v, load=False):
    """
    Setter method for igp_shortcuts, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/igp_shortcuts (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igp_shortcuts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igp_shortcuts() directly.

    YANG Description: When this leaf is set to true, OSPFv2 will route traffic to
a remote system via any LSP to the system that is marked as
shortcut eligible.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igp-shortcuts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igp_shortcuts must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-shortcuts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__igp_shortcuts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igp_shortcuts(self):
    self.__igp_shortcuts = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-shortcuts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_log_adjacency_changes(self):
    """
    Getter method for log_adjacency_changes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/log_adjacency_changes (boolean)

    YANG Description: When this leaf is set to true, a log message will be
generated when the state of an OSPFv2 neighbour changes.
    """
    return self.__log_adjacency_changes
      
  def _set_log_adjacency_changes(self, v, load=False):
    """
    Setter method for log_adjacency_changes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/log_adjacency_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_adjacency_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_adjacency_changes() directly.

    YANG Description: When this leaf is set to true, a log message will be
generated when the state of an OSPFv2 neighbour changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log-adjacency-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_adjacency_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-adjacency-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__log_adjacency_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_adjacency_changes(self):
    self.__log_adjacency_changes = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-adjacency-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_hide_transit_only_networks(self):
    """
    Getter method for hide_transit_only_networks, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/hide_transit_only_networks (boolean)

    YANG Description: When this leaf is set to true, do not advertise prefixes
into OSPFv2 that correspond to transit interfaces, as per
the behaviour discussed in RFC6860.
    """
    return self.__hide_transit_only_networks
      
  def _set_hide_transit_only_networks(self, v, load=False):
    """
    Setter method for hide_transit_only_networks, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config/hide_transit_only_networks (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hide_transit_only_networks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hide_transit_only_networks() directly.

    YANG Description: When this leaf is set to true, do not advertise prefixes
into OSPFv2 that correspond to transit interfaces, as per
the behaviour discussed in RFC6860.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="hide-transit-only-networks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hide_transit_only_networks must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hide-transit-only-networks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__hide_transit_only_networks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hide_transit_only_networks(self):
    self.__hide_transit_only_networks = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hide-transit-only-networks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  router_id = __builtin__.property(_get_router_id, _set_router_id)
  summary_route_cost_mode = __builtin__.property(_get_summary_route_cost_mode, _set_summary_route_cost_mode)
  igp_shortcuts = __builtin__.property(_get_igp_shortcuts, _set_igp_shortcuts)
  log_adjacency_changes = __builtin__.property(_get_log_adjacency_changes, _set_log_adjacency_changes)
  hide_transit_only_networks = __builtin__.property(_get_hide_transit_only_networks, _set_hide_transit_only_networks)


  _pyangbind_elements = {'router_id': router_id, 'summary_route_cost_mode': summary_route_cost_mode, 'igp_shortcuts': igp_shortcuts, 'log_adjacency_changes': log_adjacency_changes, 'hide_transit_only_networks': hide_transit_only_networks, }


