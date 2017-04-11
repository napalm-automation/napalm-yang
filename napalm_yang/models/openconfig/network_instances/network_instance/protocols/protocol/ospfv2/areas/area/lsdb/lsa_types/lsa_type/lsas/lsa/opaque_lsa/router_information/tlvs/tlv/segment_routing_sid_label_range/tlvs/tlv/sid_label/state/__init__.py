
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/router-information/tlvs/tlv/segment-routing-sid-label-range/tlvs/tlv/sid-label/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the SID/Label sub-TLV of the SR/Label
range TLV of the RI LSA
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__entry_type','__first_value',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__entry_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SID': {}, u'LABEL': {}},), is_leaf=True, yang_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    self.__first_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="first-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'router-information', u'tlvs', u'tlv', u'segment-routing-sid-label-range', u'tlvs', u'tlv', u'sid-label', u'state']

  def _get_entry_type(self):
    """
    Getter method for entry_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label/state/entry_type (oc-ospf-types:sr-sid-type)

    YANG Description: The type of entry that is contained within the sub-TLV. The range may
be represented as either a range of MPLS labels, or numeric segment
identifiers
    """
    return self.__entry_type
      
  def _set_entry_type(self, v, load=False):
    """
    Setter method for entry_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label/state/entry_type (oc-ospf-types:sr-sid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entry_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entry_type() directly.

    YANG Description: The type of entry that is contained within the sub-TLV. The range may
be represented as either a range of MPLS labels, or numeric segment
identifiers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SID': {}, u'LABEL': {}},), is_leaf=True, yang_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entry_type must be of a type compatible with oc-ospf-types:sr-sid-type""",
          'defined-type': "oc-ospf-types:sr-sid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SID': {}, u'LABEL': {}},), is_leaf=True, yang_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)""",
        })

    self.__entry_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entry_type(self):
    self.__entry_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SID': {}, u'LABEL': {}},), is_leaf=True, yang_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)


  def _get_first_value(self):
    """
    Getter method for first_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label/state/first_value (uint32)

    YANG Description: The first value within the SRGB range being specified. The type of the
entry is determined based on the value of the entry type as this value
may represent either a segment identifier or an MPLS label.
    """
    return self.__first_value
      
  def _set_first_value(self, v, load=False):
    """
    Setter method for first_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label/state/first_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_first_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_first_value() directly.

    YANG Description: The first value within the SRGB range being specified. The type of the
entry is determined based on the value of the entry type as this value
may represent either a segment identifier or an MPLS label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="first-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """first_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="first-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__first_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_first_value(self):
    self.__first_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="first-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  entry_type = __builtin__.property(_get_entry_type)
  first_value = __builtin__.property(_get_first_value)


  _pyangbind_elements = {'entry_type': entry_type, 'first_value': first_value, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/router-information/tlvs/tlv/segment-routing-sid-label-range/tlvs/tlv/sid-label/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the SID/Label sub-TLV of the SR/Label
range TLV of the RI LSA
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__entry_type','__first_value',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__entry_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SID': {}, u'LABEL': {}},), is_leaf=True, yang_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    self.__first_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="first-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'router-information', u'tlvs', u'tlv', u'segment-routing-sid-label-range', u'tlvs', u'tlv', u'sid-label', u'state']

  def _get_entry_type(self):
    """
    Getter method for entry_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label/state/entry_type (oc-ospf-types:sr-sid-type)

    YANG Description: The type of entry that is contained within the sub-TLV. The range may
be represented as either a range of MPLS labels, or numeric segment
identifiers
    """
    return self.__entry_type
      
  def _set_entry_type(self, v, load=False):
    """
    Setter method for entry_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label/state/entry_type (oc-ospf-types:sr-sid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entry_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entry_type() directly.

    YANG Description: The type of entry that is contained within the sub-TLV. The range may
be represented as either a range of MPLS labels, or numeric segment
identifiers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SID': {}, u'LABEL': {}},), is_leaf=True, yang_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entry_type must be of a type compatible with oc-ospf-types:sr-sid-type""",
          'defined-type': "oc-ospf-types:sr-sid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SID': {}, u'LABEL': {}},), is_leaf=True, yang_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)""",
        })

    self.__entry_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entry_type(self):
    self.__entry_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SID': {}, u'LABEL': {}},), is_leaf=True, yang_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)


  def _get_first_value(self):
    """
    Getter method for first_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label/state/first_value (uint32)

    YANG Description: The first value within the SRGB range being specified. The type of the
entry is determined based on the value of the entry type as this value
may represent either a segment identifier or an MPLS label.
    """
    return self.__first_value
      
  def _set_first_value(self, v, load=False):
    """
    Setter method for first_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label/state/first_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_first_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_first_value() directly.

    YANG Description: The first value within the SRGB range being specified. The type of the
entry is determined based on the value of the entry type as this value
may represent either a segment identifier or an MPLS label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="first-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """first_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="first-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__first_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_first_value(self):
    self.__first_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="first-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  entry_type = __builtin__.property(_get_entry_type)
  first_value = __builtin__.property(_get_first_value)


  _pyangbind_elements = {'entry_type': entry_type, 'first_value': first_value, }


