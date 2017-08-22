
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/sessions/session/record-route-objects/record-route-object/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Information related to RRO objects. The hop, label, and
optional flags are present for each entry in the list.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__index','__address','__reported_label','__reported_flags',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reported_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="reported-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__reported_flags = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reported-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'sessions', u'session', u'record-route-objects', u'record-route-object', u'state']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/index (uint8)

    YANG Description: Index of object in the list. Used for ordering.
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/index (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Index of object in the list. Used for ordering.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/address (inet:ip-address)

    YANG Description: IP router hop for RRO entry
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: IP router hop for RRO entry
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)


  def _get_reported_label(self):
    """
    Getter method for reported_label, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/reported_label (oc-mplst:mpls-label)

    YANG Description: Label reported for RRO hop
    """
    return self.__reported_label
      
  def _set_reported_label(self, v, load=False):
    """
    Setter method for reported_label, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/reported_label (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reported_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reported_label() directly.

    YANG Description: Label reported for RRO hop
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="reported-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reported_label must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="reported-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)""",
        })

    self.__reported_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reported_label(self):
    self.__reported_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="reported-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)


  def _get_reported_flags(self):
    """
    Getter method for reported_flags, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/reported_flags (uint8)

    YANG Description: Subobject flags for MPLS label
    """
    return self.__reported_flags
      
  def _set_reported_flags(self, v, load=False):
    """
    Setter method for reported_flags, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/reported_flags (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reported_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reported_flags() directly.

    YANG Description: Subobject flags for MPLS label
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reported-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reported_flags must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reported-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__reported_flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reported_flags(self):
    self.__reported_flags = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reported-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  index = __builtin__.property(_get_index)
  address = __builtin__.property(_get_address)
  reported_label = __builtin__.property(_get_reported_label)
  reported_flags = __builtin__.property(_get_reported_flags)


  _pyangbind_elements = {'index': index, 'address': address, 'reported_label': reported_label, 'reported_flags': reported_flags, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/sessions/session/record-route-objects/record-route-object/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Information related to RRO objects. The hop, label, and
optional flags are present for each entry in the list.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__index','__address','__reported_label','__reported_flags',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reported_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="reported-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__reported_flags = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reported-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'sessions', u'session', u'record-route-objects', u'record-route-object', u'state']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/index (uint8)

    YANG Description: Index of object in the list. Used for ordering.
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/index (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Index of object in the list. Used for ordering.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/address (inet:ip-address)

    YANG Description: IP router hop for RRO entry
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: IP router hop for RRO entry
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)


  def _get_reported_label(self):
    """
    Getter method for reported_label, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/reported_label (oc-mplst:mpls-label)

    YANG Description: Label reported for RRO hop
    """
    return self.__reported_label
      
  def _set_reported_label(self, v, load=False):
    """
    Setter method for reported_label, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/reported_label (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reported_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reported_label() directly.

    YANG Description: Label reported for RRO hop
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="reported-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reported_label must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="reported-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)""",
        })

    self.__reported_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reported_label(self):
    self.__reported_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="reported-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)


  def _get_reported_flags(self):
    """
    Getter method for reported_flags, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/reported_flags (uint8)

    YANG Description: Subobject flags for MPLS label
    """
    return self.__reported_flags
      
  def _set_reported_flags(self, v, load=False):
    """
    Setter method for reported_flags, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object/state/reported_flags (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reported_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reported_flags() directly.

    YANG Description: Subobject flags for MPLS label
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reported-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reported_flags must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reported-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__reported_flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reported_flags(self):
    self.__reported_flags = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reported-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  index = __builtin__.property(_get_index)
  address = __builtin__.property(_get_address)
  reported_label = __builtin__.property(_get_reported_label)
  reported_flags = __builtin__.property(_get_reported_flags)


  _pyangbind_elements = {'index': index, 'address': address, 'reported_label': reported_label, 'reported_flags': reported_flags, }


