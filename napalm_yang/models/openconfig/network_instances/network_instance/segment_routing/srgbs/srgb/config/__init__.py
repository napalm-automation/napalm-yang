
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/segment-routing/srgbs/srgb/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the SRGB.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_id','__dataplane_type','__mpls_label_blocks','__ipv6_prefixes',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mpls_label_blocks = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mpls-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    self.__dataplane_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='sr-dataplane-type', is_config=True)
    self.__ipv6_prefixes = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv6-prefix', is_config=True)

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
      return [u'network-instances', u'network-instance', u'segment-routing', u'srgbs', u'srgb', u'config']

  def _get_local_id(self):
    """
    Getter method for local_id, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/local_id (string)

    YANG Description: Unique identifier for the segment routing global block on
the local system.
    """
    return self.__local_id
      
  def _set_local_id(self, v, load=False):
    """
    Setter method for local_id, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/local_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_id() directly.

    YANG Description: Unique identifier for the segment routing global block on
the local system.
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


  def _get_dataplane_type(self):
    """
    Getter method for dataplane_type, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/dataplane_type (sr-dataplane-type)

    YANG Description: The dataplane being used to instantiate the SRGB. When MPLS is specified
the set of MPLS label blocks that are defined in the mpls-label-blocks
list are used to make up the SRGB. When IPv6 is specified, the set of IPv6
prefixes specified in the ipv6-prefixes list are used.
    """
    return self.__dataplane_type
      
  def _set_dataplane_type(self, v, load=False):
    """
    Setter method for dataplane_type, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/dataplane_type (sr-dataplane-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dataplane_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dataplane_type() directly.

    YANG Description: The dataplane being used to instantiate the SRGB. When MPLS is specified
the set of MPLS label blocks that are defined in the mpls-label-blocks
list are used to make up the SRGB. When IPv6 is specified, the set of IPv6
prefixes specified in the ipv6-prefixes list are used.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='sr-dataplane-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dataplane_type must be of a type compatible with sr-dataplane-type""",
          'defined-type': "openconfig-network-instance:sr-dataplane-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='sr-dataplane-type', is_config=True)""",
        })

    self.__dataplane_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dataplane_type(self):
    self.__dataplane_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='sr-dataplane-type', is_config=True)


  def _get_mpls_label_blocks(self):
    """
    Getter method for mpls_label_blocks, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/mpls_label_blocks (leafref)

    YANG Description: A list of refences to the label blocks that are used to make
up the SRGB.
    """
    return self.__mpls_label_blocks
      
  def _set_mpls_label_blocks(self, v, load=False):
    """
    Setter method for mpls_label_blocks, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/mpls_label_blocks (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_label_blocks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_label_blocks() directly.

    YANG Description: A list of refences to the label blocks that are used to make
up the SRGB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mpls-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_label_blocks must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mpls-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__mpls_label_blocks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_label_blocks(self):
    self.__mpls_label_blocks = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mpls-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_ipv6_prefixes(self):
    """
    Getter method for ipv6_prefixes, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/ipv6_prefixes (inet:ipv6-prefix)

    YANG Description: A list of IPv6 prefixes which are to be used for segment routing using
the IPv6 dataplane.
    """
    return self.__ipv6_prefixes
      
  def _set_ipv6_prefixes(self, v, load=False):
    """
    Setter method for ipv6_prefixes, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/ipv6_prefixes (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_prefixes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_prefixes() directly.

    YANG Description: A list of IPv6 prefixes which are to be used for segment routing using
the IPv6 dataplane.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_prefixes must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__ipv6_prefixes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_prefixes(self):
    self.__ipv6_prefixes = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv6-prefix', is_config=True)

  local_id = __builtin__.property(_get_local_id, _set_local_id)
  dataplane_type = __builtin__.property(_get_dataplane_type, _set_dataplane_type)
  mpls_label_blocks = __builtin__.property(_get_mpls_label_blocks, _set_mpls_label_blocks)
  ipv6_prefixes = __builtin__.property(_get_ipv6_prefixes, _set_ipv6_prefixes)


  _pyangbind_elements = {'local_id': local_id, 'dataplane_type': dataplane_type, 'mpls_label_blocks': mpls_label_blocks, 'ipv6_prefixes': ipv6_prefixes, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/segment-routing/srgbs/srgb/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the SRGB.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_id','__dataplane_type','__mpls_label_blocks','__ipv6_prefixes',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mpls_label_blocks = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mpls-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__local_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    self.__dataplane_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='sr-dataplane-type', is_config=True)
    self.__ipv6_prefixes = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv6-prefix', is_config=True)

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
      return [u'network-instances', u'network-instance', u'segment-routing', u'srgbs', u'srgb', u'config']

  def _get_local_id(self):
    """
    Getter method for local_id, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/local_id (string)

    YANG Description: Unique identifier for the segment routing global block on
the local system.
    """
    return self.__local_id
      
  def _set_local_id(self, v, load=False):
    """
    Setter method for local_id, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/local_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_id() directly.

    YANG Description: Unique identifier for the segment routing global block on
the local system.
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


  def _get_dataplane_type(self):
    """
    Getter method for dataplane_type, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/dataplane_type (sr-dataplane-type)

    YANG Description: The dataplane being used to instantiate the SRGB. When MPLS is specified
the set of MPLS label blocks that are defined in the mpls-label-blocks
list are used to make up the SRGB. When IPv6 is specified, the set of IPv6
prefixes specified in the ipv6-prefixes list are used.
    """
    return self.__dataplane_type
      
  def _set_dataplane_type(self, v, load=False):
    """
    Setter method for dataplane_type, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/dataplane_type (sr-dataplane-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dataplane_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dataplane_type() directly.

    YANG Description: The dataplane being used to instantiate the SRGB. When MPLS is specified
the set of MPLS label blocks that are defined in the mpls-label-blocks
list are used to make up the SRGB. When IPv6 is specified, the set of IPv6
prefixes specified in the ipv6-prefixes list are used.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='sr-dataplane-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dataplane_type must be of a type compatible with sr-dataplane-type""",
          'defined-type': "openconfig-network-instance:sr-dataplane-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='sr-dataplane-type', is_config=True)""",
        })

    self.__dataplane_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dataplane_type(self):
    self.__dataplane_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MPLS': {}, u'IPV6': {}},), is_leaf=True, yang_name="dataplane-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='sr-dataplane-type', is_config=True)


  def _get_mpls_label_blocks(self):
    """
    Getter method for mpls_label_blocks, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/mpls_label_blocks (leafref)

    YANG Description: A list of refences to the label blocks that are used to make
up the SRGB.
    """
    return self.__mpls_label_blocks
      
  def _set_mpls_label_blocks(self, v, load=False):
    """
    Setter method for mpls_label_blocks, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/mpls_label_blocks (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_label_blocks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_label_blocks() directly.

    YANG Description: A list of refences to the label blocks that are used to make
up the SRGB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mpls-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_label_blocks must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mpls-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__mpls_label_blocks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_label_blocks(self):
    self.__mpls_label_blocks = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mpls-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_ipv6_prefixes(self):
    """
    Getter method for ipv6_prefixes, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/ipv6_prefixes (inet:ipv6-prefix)

    YANG Description: A list of IPv6 prefixes which are to be used for segment routing using
the IPv6 dataplane.
    """
    return self.__ipv6_prefixes
      
  def _set_ipv6_prefixes(self, v, load=False):
    """
    Setter method for ipv6_prefixes, mapped from YANG variable /network_instances/network_instance/segment_routing/srgbs/srgb/config/ipv6_prefixes (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_prefixes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_prefixes() directly.

    YANG Description: A list of IPv6 prefixes which are to be used for segment routing using
the IPv6 dataplane.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_prefixes must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__ipv6_prefixes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_prefixes(self):
    self.__ipv6_prefixes = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv6-prefix', is_config=True)

  local_id = __builtin__.property(_get_local_id, _set_local_id)
  dataplane_type = __builtin__.property(_get_dataplane_type, _set_dataplane_type)
  mpls_label_blocks = __builtin__.property(_get_mpls_label_blocks, _set_mpls_label_blocks)
  ipv6_prefixes = __builtin__.property(_get_ipv6_prefixes, _set_ipv6_prefixes)


  _pyangbind_elements = {'local_id': local_id, 'dataplane_type': dataplane_type, 'mpls_label_blocks': mpls_label_blocks, 'ipv6_prefixes': ipv6_prefixes, }


