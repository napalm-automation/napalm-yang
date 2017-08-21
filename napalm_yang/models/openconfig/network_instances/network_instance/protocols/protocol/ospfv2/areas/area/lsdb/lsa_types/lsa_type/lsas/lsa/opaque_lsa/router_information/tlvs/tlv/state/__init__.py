
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/router-information/tlvs/tlv/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-TLV state parameters of the RI LSA
  """
  __slots__ = ('_path_helper', '_extmethods', '__type',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'router-information', u'tlvs', u'tlv', u'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/state/type (union)

    YANG Description: The type of sub-TLV of the Router Information opaque LSA
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/state/type (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of sub-TLV of the Router Information opaque LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  type = __builtin__.property(_get_type)


  _pyangbind_elements = OrderedDict([('type', type), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/router-information/tlvs/tlv/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-TLV state parameters of the RI LSA
  """
  __slots__ = ('_path_helper', '_extmethods', '__type',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'router-information', u'tlvs', u'tlv', u'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/state/type (union)

    YANG Description: The type of sub-TLV of the Router Information opaque LSA
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/state/type (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of sub-TLV of the Router Information opaque LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_INFORMATIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_NODE_ADMIN_TAG': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospft:RI_SR_SID_LABEL_RANGE': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_FUNCTIONAL_CAPABILITIES': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}, u'oc-ospf-types:RI_SR_ALGORITHM': {'@namespace': u'http://openconfig.net/yang/ospf-types', '@module': u'openconfig-ospf-types'}},),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UNKNOWN': {}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  type = __builtin__.property(_get_type)


  _pyangbind_elements = OrderedDict([('type', type), ])


