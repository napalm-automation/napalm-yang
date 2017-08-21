
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/packet-counters/iih/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational counters relating to IIH PDUs
  """
  __slots__ = ('_path_helper', '_extmethods', '__received','__processed','__dropped','__sent','__retransmit',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__retransmit = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    self.__received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    self.__processed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="processed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    self.__sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    self.__dropped = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dropped", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'levels', u'level', u'packet-counters', u'iih', u'state']

  def _get_received(self):
    """
    Getter method for received, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/received (yang:counter32)

    YANG Description: The number of the specified type of PDU received on the interface.
    """
    return self.__received
      
  def _set_received(self, v, load=False):
    """
    Setter method for received, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/received (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_received() directly.

    YANG Description: The number of the specified type of PDU received on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """received must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_received(self):
    self.__received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)


  def _get_processed(self):
    """
    Getter method for processed, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/processed (yang:counter32)

    YANG Description: The number of the specified type of PDU received on the interface
that have been processed by the local system.
    """
    return self.__processed
      
  def _set_processed(self, v, load=False):
    """
    Setter method for processed, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/processed (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_processed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_processed() directly.

    YANG Description: The number of the specified type of PDU received on the interface
that have been processed by the local system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="processed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """processed must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="processed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__processed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_processed(self):
    self.__processed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="processed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)


  def _get_dropped(self):
    """
    Getter method for dropped, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/dropped (yang:counter32)

    YANG Description: The number of the specified type of PDU received on the interface
that have been dropped.
    """
    return self.__dropped
      
  def _set_dropped(self, v, load=False):
    """
    Setter method for dropped, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/dropped (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dropped is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dropped() directly.

    YANG Description: The number of the specified type of PDU received on the interface
that have been dropped.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dropped", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dropped must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dropped", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__dropped = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dropped(self):
    self.__dropped = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dropped", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)


  def _get_sent(self):
    """
    Getter method for sent, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/sent (yang:counter32)

    YANG Description: The number of the specified type of PDU that have been sent by the
local system on the interface.
    """
    return self.__sent
      
  def _set_sent(self, v, load=False):
    """
    Setter method for sent, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/sent (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent() directly.

    YANG Description: The number of the specified type of PDU that have been sent by the
local system on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent(self):
    self.__sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)


  def _get_retransmit(self):
    """
    Getter method for retransmit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/retransmit (yang:counter32)

    YANG Description: The number of the specified type of PDU that that have been
retransmitted by the local system on the interface.
    """
    return self.__retransmit
      
  def _set_retransmit(self, v, load=False):
    """
    Setter method for retransmit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/retransmit (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retransmit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retransmit() directly.

    YANG Description: The number of the specified type of PDU that that have been
retransmitted by the local system on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retransmit must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__retransmit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retransmit(self):
    self.__retransmit = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)

  received = __builtin__.property(_get_received)
  processed = __builtin__.property(_get_processed)
  dropped = __builtin__.property(_get_dropped)
  sent = __builtin__.property(_get_sent)
  retransmit = __builtin__.property(_get_retransmit)


  _pyangbind_elements = OrderedDict([('received', received), ('processed', processed), ('dropped', dropped), ('sent', sent), ('retransmit', retransmit), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/packet-counters/iih/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational counters relating to IIH PDUs
  """
  __slots__ = ('_path_helper', '_extmethods', '__received','__processed','__dropped','__sent','__retransmit',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__retransmit = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    self.__received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    self.__processed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="processed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    self.__sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    self.__dropped = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dropped", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'levels', u'level', u'packet-counters', u'iih', u'state']

  def _get_received(self):
    """
    Getter method for received, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/received (yang:counter32)

    YANG Description: The number of the specified type of PDU received on the interface.
    """
    return self.__received
      
  def _set_received(self, v, load=False):
    """
    Setter method for received, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/received (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_received() directly.

    YANG Description: The number of the specified type of PDU received on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """received must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_received(self):
    self.__received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)


  def _get_processed(self):
    """
    Getter method for processed, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/processed (yang:counter32)

    YANG Description: The number of the specified type of PDU received on the interface
that have been processed by the local system.
    """
    return self.__processed
      
  def _set_processed(self, v, load=False):
    """
    Setter method for processed, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/processed (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_processed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_processed() directly.

    YANG Description: The number of the specified type of PDU received on the interface
that have been processed by the local system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="processed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """processed must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="processed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__processed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_processed(self):
    self.__processed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="processed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)


  def _get_dropped(self):
    """
    Getter method for dropped, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/dropped (yang:counter32)

    YANG Description: The number of the specified type of PDU received on the interface
that have been dropped.
    """
    return self.__dropped
      
  def _set_dropped(self, v, load=False):
    """
    Setter method for dropped, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/dropped (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dropped is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dropped() directly.

    YANG Description: The number of the specified type of PDU received on the interface
that have been dropped.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dropped", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dropped must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dropped", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__dropped = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dropped(self):
    self.__dropped = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dropped", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)


  def _get_sent(self):
    """
    Getter method for sent, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/sent (yang:counter32)

    YANG Description: The number of the specified type of PDU that have been sent by the
local system on the interface.
    """
    return self.__sent
      
  def _set_sent(self, v, load=False):
    """
    Setter method for sent, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/sent (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent() directly.

    YANG Description: The number of the specified type of PDU that have been sent by the
local system on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent(self):
    self.__sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)


  def _get_retransmit(self):
    """
    Getter method for retransmit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/retransmit (yang:counter32)

    YANG Description: The number of the specified type of PDU that that have been
retransmitted by the local system on the interface.
    """
    return self.__retransmit
      
  def _set_retransmit(self, v, load=False):
    """
    Setter method for retransmit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/packet_counters/iih/state/retransmit (yang:counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retransmit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retransmit() directly.

    YANG Description: The number of the specified type of PDU that that have been
retransmitted by the local system on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retransmit must be of a type compatible with yang:counter32""",
          'defined-type': "yang:counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)""",
        })

    self.__retransmit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retransmit(self):
    self.__retransmit = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter32', is_config=False)

  received = __builtin__.property(_get_received)
  processed = __builtin__.property(_get_processed)
  dropped = __builtin__.property(_get_dropped)
  sent = __builtin__.property(_get_sent)
  retransmit = __builtin__.property(_get_retransmit)


  _pyangbind_elements = OrderedDict([('received', received), ('processed', processed), ('dropped', dropped), ('sent', sent), ('retransmit', retransmit), ])


