
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

from . import segments
class ero_path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/ero-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters for the ERO Path Sub-TLV of the SID/Label
binding TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__segments',)

  _yang_name = 'ero-path'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__segments = YANGDynClass(base=segments.segments, is_container='container', yang_name="segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'extended-prefix', u'tlvs', u'tlv', u'sid-label-binding', u'tlvs', u'tlv', u'ero-path']

  def _get_segments(self):
    """
    Getter method for segments, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments (container)

    YANG Description: Segments of the path described within the SID/Label
Binding sub-TLV
    """
    return self.__segments
      
  def _set_segments(self, v, load=False):
    """
    Setter method for segments, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_segments is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_segments() directly.

    YANG Description: Segments of the path described within the SID/Label
Binding sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=segments.segments, is_container='container', yang_name="segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """segments must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=segments.segments, is_container='container', yang_name="segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__segments = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_segments(self):
    self.__segments = YANGDynClass(base=segments.segments, is_container='container', yang_name="segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  segments = __builtin__.property(_get_segments)


  _pyangbind_elements = OrderedDict([('segments', segments), ])


from . import segments
class ero_path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/ero-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters for the ERO Path Sub-TLV of the SID/Label
binding TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__segments',)

  _yang_name = 'ero-path'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__segments = YANGDynClass(base=segments.segments, is_container='container', yang_name="segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'extended-prefix', u'tlvs', u'tlv', u'sid-label-binding', u'tlvs', u'tlv', u'ero-path']

  def _get_segments(self):
    """
    Getter method for segments, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments (container)

    YANG Description: Segments of the path described within the SID/Label
Binding sub-TLV
    """
    return self.__segments
      
  def _set_segments(self, v, load=False):
    """
    Setter method for segments, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_segments is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_segments() directly.

    YANG Description: Segments of the path described within the SID/Label
Binding sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=segments.segments, is_container='container', yang_name="segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """segments must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=segments.segments, is_container='container', yang_name="segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__segments = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_segments(self):
    self.__segments = YANGDynClass(base=segments.segments, is_container='container', yang_name="segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  segments = __builtin__.property(_get_segments)


  _pyangbind_elements = OrderedDict([('segments', segments), ])


