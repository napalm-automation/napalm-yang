
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

from . import mt
from . import state
from . import subTLVs
from . import undefined_subtlvs
class prefix(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv4-reachability/prefixes/prefix. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv4 prefixes that are contained within MT reachability TLV.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mt','__state','__subTLVs','__undefined_subtlvs',)

  _yang_name = 'prefix'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subTLVs = YANGDynClass(base=subTLVs.subTLVs, is_container='container', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__mt = YANGDynClass(base=mt.mt, is_container='container', yang_name="mt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__undefined_subtlvs = YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-ipv4-reachability', u'prefixes', u'prefix']

  def _get_mt(self):
    """
    Getter method for mt, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/mt (container)

    YANG Description: Multi-topology parameters.
    """
    return self.__mt
      
  def _set_mt(self, v, load=False):
    """
    Setter method for mt, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/mt (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mt() directly.

    YANG Description: Multi-topology parameters.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mt.mt, is_container='container', yang_name="mt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mt must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mt.mt, is_container='container', yang_name="mt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__mt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mt(self):
    self.__mt = YANGDynClass(base=mt.mt, is_container='container', yang_name="mt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/state (container)

    YANG Description: State parameters of an IPv4 extended prefix.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of an IPv4 extended prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_subTLVs(self):
    """
    Getter method for subTLVs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subTLVs (container)

    YANG Description: This container describes IS prefix sub-TLVs.
    """
    return self.__subTLVs
      
  def _set_subTLVs(self, v, load=False):
    """
    Setter method for subTLVs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subTLVs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subTLVs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subTLVs() directly.

    YANG Description: This container describes IS prefix sub-TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=subTLVs.subTLVs, is_container='container', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subTLVs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=subTLVs.subTLVs, is_container='container', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__subTLVs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subTLVs(self):
    self.__subTLVs = YANGDynClass(base=subTLVs.subTLVs, is_container='container', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_undefined_subtlvs(self):
    """
    Getter method for undefined_subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs (container)

    YANG Description: This container describes undefined ISIS TLVs.
    """
    return self.__undefined_subtlvs
      
  def _set_undefined_subtlvs(self, v, load=False):
    """
    Setter method for undefined_subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_undefined_subtlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_undefined_subtlvs() directly.

    YANG Description: This container describes undefined ISIS TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """undefined_subtlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__undefined_subtlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_undefined_subtlvs(self):
    self.__undefined_subtlvs = YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  mt = __builtin__.property(_get_mt)
  state = __builtin__.property(_get_state)
  subTLVs = __builtin__.property(_get_subTLVs)
  undefined_subtlvs = __builtin__.property(_get_undefined_subtlvs)


  _pyangbind_elements = OrderedDict([('mt', mt), ('state', state), ('subTLVs', subTLVs), ('undefined_subtlvs', undefined_subtlvs), ])


from . import mt
from . import state
from . import subTLVs
from . import undefined_subtlvs
class prefix(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv4-reachability/prefixes/prefix. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv4 prefixes that are contained within MT reachability TLV.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mt','__state','__subTLVs','__undefined_subtlvs',)

  _yang_name = 'prefix'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subTLVs = YANGDynClass(base=subTLVs.subTLVs, is_container='container', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__mt = YANGDynClass(base=mt.mt, is_container='container', yang_name="mt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__undefined_subtlvs = YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-ipv4-reachability', u'prefixes', u'prefix']

  def _get_mt(self):
    """
    Getter method for mt, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/mt (container)

    YANG Description: Multi-topology parameters.
    """
    return self.__mt
      
  def _set_mt(self, v, load=False):
    """
    Setter method for mt, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/mt (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mt() directly.

    YANG Description: Multi-topology parameters.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mt.mt, is_container='container', yang_name="mt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mt must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mt.mt, is_container='container', yang_name="mt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__mt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mt(self):
    self.__mt = YANGDynClass(base=mt.mt, is_container='container', yang_name="mt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/state (container)

    YANG Description: State parameters of an IPv4 extended prefix.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of an IPv4 extended prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_subTLVs(self):
    """
    Getter method for subTLVs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subTLVs (container)

    YANG Description: This container describes IS prefix sub-TLVs.
    """
    return self.__subTLVs
      
  def _set_subTLVs(self, v, load=False):
    """
    Setter method for subTLVs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subTLVs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subTLVs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subTLVs() directly.

    YANG Description: This container describes IS prefix sub-TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=subTLVs.subTLVs, is_container='container', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subTLVs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=subTLVs.subTLVs, is_container='container', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__subTLVs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subTLVs(self):
    self.__subTLVs = YANGDynClass(base=subTLVs.subTLVs, is_container='container', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_undefined_subtlvs(self):
    """
    Getter method for undefined_subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs (container)

    YANG Description: This container describes undefined ISIS TLVs.
    """
    return self.__undefined_subtlvs
      
  def _set_undefined_subtlvs(self, v, load=False):
    """
    Setter method for undefined_subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_undefined_subtlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_undefined_subtlvs() directly.

    YANG Description: This container describes undefined ISIS TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """undefined_subtlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__undefined_subtlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_undefined_subtlvs(self):
    self.__undefined_subtlvs = YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  mt = __builtin__.property(_get_mt)
  state = __builtin__.property(_get_state)
  subTLVs = __builtin__.property(_get_subTLVs)
  undefined_subtlvs = __builtin__.property(_get_undefined_subtlvs)


  _pyangbind_elements = OrderedDict([('mt', mt), ('state', state), ('subTLVs', subTLVs), ('undefined_subtlvs', undefined_subtlvs), ])


