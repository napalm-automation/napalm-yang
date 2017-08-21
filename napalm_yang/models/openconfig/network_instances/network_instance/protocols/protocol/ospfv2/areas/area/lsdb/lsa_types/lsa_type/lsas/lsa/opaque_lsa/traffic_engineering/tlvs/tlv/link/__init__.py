
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

from . import sub_tlvs
class link(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/link. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters included in the Link TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__sub_tlvs',)

  _yang_name = 'link'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sub_tlvs = YANGDynClass(base=sub_tlvs.sub_tlvs, is_container='container', yang_name="sub-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'traffic-engineering', u'tlvs', u'tlv', u'link']

  def _get_sub_tlvs(self):
    """
    Getter method for sub_tlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs (container)

    YANG Description: Sub-TLVs included in the Link TLV
    """
    return self.__sub_tlvs
      
  def _set_sub_tlvs(self, v, load=False):
    """
    Setter method for sub_tlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sub_tlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sub_tlvs() directly.

    YANG Description: Sub-TLVs included in the Link TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sub_tlvs.sub_tlvs, is_container='container', yang_name="sub-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sub_tlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sub_tlvs.sub_tlvs, is_container='container', yang_name="sub-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__sub_tlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sub_tlvs(self):
    self.__sub_tlvs = YANGDynClass(base=sub_tlvs.sub_tlvs, is_container='container', yang_name="sub-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  sub_tlvs = __builtin__.property(_get_sub_tlvs)


  _pyangbind_elements = OrderedDict([('sub_tlvs', sub_tlvs), ])


from . import sub_tlvs
class link(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/link. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters included in the Link TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__sub_tlvs',)

  _yang_name = 'link'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sub_tlvs = YANGDynClass(base=sub_tlvs.sub_tlvs, is_container='container', yang_name="sub-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'traffic-engineering', u'tlvs', u'tlv', u'link']

  def _get_sub_tlvs(self):
    """
    Getter method for sub_tlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs (container)

    YANG Description: Sub-TLVs included in the Link TLV
    """
    return self.__sub_tlvs
      
  def _set_sub_tlvs(self, v, load=False):
    """
    Setter method for sub_tlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sub_tlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sub_tlvs() directly.

    YANG Description: Sub-TLVs included in the Link TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sub_tlvs.sub_tlvs, is_container='container', yang_name="sub-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sub_tlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sub_tlvs.sub_tlvs, is_container='container', yang_name="sub-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__sub_tlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sub_tlvs(self):
    self.__sub_tlvs = YANGDynClass(base=sub_tlvs.sub_tlvs, is_container='container', yang_name="sub-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  sub_tlvs = __builtin__.property(_get_sub_tlvs)


  _pyangbind_elements = OrderedDict([('sub_tlvs', sub_tlvs), ])


