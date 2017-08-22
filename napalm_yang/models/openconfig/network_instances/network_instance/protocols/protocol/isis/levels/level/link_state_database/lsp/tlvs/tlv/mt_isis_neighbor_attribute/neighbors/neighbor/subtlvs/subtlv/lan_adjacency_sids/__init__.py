
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

from . import lan_adjacency_sid
class lan_adjacency_sids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/subtlvs/subtlv/lan-adjacency-sids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines segment routing LAN adjacency
SIDs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lan_adjacency_sid',)

  _yang_name = 'lan-adjacency-sids'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lan_adjacency_sid = YANGDynClass(base=YANGListType("value",lan_adjacency_sid.lan_adjacency_sid, yang_name="lan-adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='value', extensions=None), is_container='list', yang_name="lan-adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-isis-neighbor-attribute', u'neighbors', u'neighbor', u'subtlvs', u'subtlv', u'lan-adjacency-sids']

  def _get_lan_adjacency_sid(self):
    """
    Getter method for lan_adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/subtlvs/subtlv/lan_adjacency_sids/lan_adjacency_sid (list)

    YANG Description: Adjacency Segment-IDs List. An IGP-Adjacency Segment is
an IGP segment attached to a unidirectional adjacency or
a set of unidirectional adjacencies. By default, an IGP-
Adjacency Segment is local to the node which advertises
it.
    """
    return self.__lan_adjacency_sid
      
  def _set_lan_adjacency_sid(self, v, load=False):
    """
    Setter method for lan_adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/subtlvs/subtlv/lan_adjacency_sids/lan_adjacency_sid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lan_adjacency_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lan_adjacency_sid() directly.

    YANG Description: Adjacency Segment-IDs List. An IGP-Adjacency Segment is
an IGP segment attached to a unidirectional adjacency or
a set of unidirectional adjacencies. By default, an IGP-
Adjacency Segment is local to the node which advertises
it.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("value",lan_adjacency_sid.lan_adjacency_sid, yang_name="lan-adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='value', extensions=None), is_container='list', yang_name="lan-adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lan_adjacency_sid must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("value",lan_adjacency_sid.lan_adjacency_sid, yang_name="lan-adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='value', extensions=None), is_container='list', yang_name="lan-adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__lan_adjacency_sid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lan_adjacency_sid(self):
    self.__lan_adjacency_sid = YANGDynClass(base=YANGListType("value",lan_adjacency_sid.lan_adjacency_sid, yang_name="lan-adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='value', extensions=None), is_container='list', yang_name="lan-adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  lan_adjacency_sid = __builtin__.property(_get_lan_adjacency_sid)


  _pyangbind_elements = {'lan_adjacency_sid': lan_adjacency_sid, }


from . import lan_adjacency_sid
class lan_adjacency_sids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/subtlvs/subtlv/lan-adjacency-sids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines segment routing LAN adjacency
SIDs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lan_adjacency_sid',)

  _yang_name = 'lan-adjacency-sids'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lan_adjacency_sid = YANGDynClass(base=YANGListType("value",lan_adjacency_sid.lan_adjacency_sid, yang_name="lan-adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='value', extensions=None), is_container='list', yang_name="lan-adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-isis-neighbor-attribute', u'neighbors', u'neighbor', u'subtlvs', u'subtlv', u'lan-adjacency-sids']

  def _get_lan_adjacency_sid(self):
    """
    Getter method for lan_adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/subtlvs/subtlv/lan_adjacency_sids/lan_adjacency_sid (list)

    YANG Description: Adjacency Segment-IDs List. An IGP-Adjacency Segment is
an IGP segment attached to a unidirectional adjacency or
a set of unidirectional adjacencies. By default, an IGP-
Adjacency Segment is local to the node which advertises
it.
    """
    return self.__lan_adjacency_sid
      
  def _set_lan_adjacency_sid(self, v, load=False):
    """
    Setter method for lan_adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/subtlvs/subtlv/lan_adjacency_sids/lan_adjacency_sid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lan_adjacency_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lan_adjacency_sid() directly.

    YANG Description: Adjacency Segment-IDs List. An IGP-Adjacency Segment is
an IGP segment attached to a unidirectional adjacency or
a set of unidirectional adjacencies. By default, an IGP-
Adjacency Segment is local to the node which advertises
it.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("value",lan_adjacency_sid.lan_adjacency_sid, yang_name="lan-adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='value', extensions=None), is_container='list', yang_name="lan-adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lan_adjacency_sid must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("value",lan_adjacency_sid.lan_adjacency_sid, yang_name="lan-adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='value', extensions=None), is_container='list', yang_name="lan-adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__lan_adjacency_sid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lan_adjacency_sid(self):
    self.__lan_adjacency_sid = YANGDynClass(base=YANGListType("value",lan_adjacency_sid.lan_adjacency_sid, yang_name="lan-adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='value', extensions=None), is_container='list', yang_name="lan-adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  lan_adjacency_sid = __builtin__.property(_get_lan_adjacency_sid)


  _pyangbind_elements = {'lan_adjacency_sid': lan_adjacency_sid, }


