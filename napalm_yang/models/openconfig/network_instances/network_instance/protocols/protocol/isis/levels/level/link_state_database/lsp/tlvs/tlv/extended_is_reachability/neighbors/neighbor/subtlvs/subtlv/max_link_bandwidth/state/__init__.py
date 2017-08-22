
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/extended-is-reachability/neighbors/neighbor/subtlvs/subtlv/max-link-bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of sub-TLV 9.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__bandwidth',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'extended-is-reachability', u'neighbors', u'neighbor', u'subtlvs', u'subtlv', u'max-link-bandwidth', u'state']

  def _get_bandwidth(self):
    """
    Getter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/subtlvs/subtlv/max_link_bandwidth/state/bandwidth (oc-types:ieeefloat32)

    YANG Description: The maximum bandwidth that can be used on this link
in this direction (from the system originating the LSP
to its neighbors).  It is encoded in 32 bits in IEEE
floating point format.  The units are bytes (not
bits!) per second.
    """
    return self.__bandwidth
      
  def _set_bandwidth(self, v, load=False):
    """
    Setter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/subtlvs/subtlv/max_link_bandwidth/state/bandwidth (oc-types:ieeefloat32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth() directly.

    YANG Description: The maximum bandwidth that can be used on this link
in this direction (from the system originating the LSP
to its neighbors).  It is encoded in 32 bits in IEEE
floating point format.  The units are bytes (not
bits!) per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth must be of a type compatible with oc-types:ieeefloat32""",
          'defined-type': "oc-types:ieeefloat32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)""",
        })

    self.__bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth(self):
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

  bandwidth = __builtin__.property(_get_bandwidth)


  _pyangbind_elements = {'bandwidth': bandwidth, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/extended-is-reachability/neighbors/neighbor/subtlvs/subtlv/max-link-bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of sub-TLV 9.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__bandwidth',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'extended-is-reachability', u'neighbors', u'neighbor', u'subtlvs', u'subtlv', u'max-link-bandwidth', u'state']

  def _get_bandwidth(self):
    """
    Getter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/subtlvs/subtlv/max_link_bandwidth/state/bandwidth (oc-types:ieeefloat32)

    YANG Description: The maximum bandwidth that can be used on this link
in this direction (from the system originating the LSP
to its neighbors).  It is encoded in 32 bits in IEEE
floating point format.  The units are bytes (not
bits!) per second.
    """
    return self.__bandwidth
      
  def _set_bandwidth(self, v, load=False):
    """
    Setter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/subtlvs/subtlv/max_link_bandwidth/state/bandwidth (oc-types:ieeefloat32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth() directly.

    YANG Description: The maximum bandwidth that can be used on this link
in this direction (from the system originating the LSP
to its neighbors).  It is encoded in 32 bits in IEEE
floating point format.  The units are bytes (not
bits!) per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth must be of a type compatible with oc-types:ieeefloat32""",
          'defined-type': "oc-types:ieeefloat32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)""",
        })

    self.__bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth(self):
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

  bandwidth = __builtin__.property(_get_bandwidth)


  _pyangbind_elements = {'bandwidth': bandwidth, }


