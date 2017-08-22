
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

from . import prefix_limit
class l3vpn_ipv6_multicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv6-multicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Multicast IPv6 L3VPN configuration options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__prefix_limit',)

  _yang_name = 'l3vpn-ipv6-multicast'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__prefix_limit = YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'l3vpn-ipv6-multicast']

  def _get_prefix_limit(self):
    """
    Getter method for prefix_limit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/l3vpn_ipv6_multicast/prefix_limit (container)

    YANG Description: Configure the maximum number of prefixes that will be
accepted from a peer
    """
    return self.__prefix_limit
      
  def _set_prefix_limit(self, v, load=False):
    """
    Setter method for prefix_limit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/l3vpn_ipv6_multicast/prefix_limit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_limit() directly.

    YANG Description: Configure the maximum number of prefixes that will be
accepted from a peer
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_limit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__prefix_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_limit(self):
    self.__prefix_limit = YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  prefix_limit = __builtin__.property(_get_prefix_limit, _set_prefix_limit)


  _pyangbind_elements = {'prefix_limit': prefix_limit, }


from . import prefix_limit
class l3vpn_ipv6_multicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/l3vpn-ipv6-multicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Multicast IPv6 L3VPN configuration options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__prefix_limit',)

  _yang_name = 'l3vpn-ipv6-multicast'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__prefix_limit = YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'l3vpn-ipv6-multicast']

  def _get_prefix_limit(self):
    """
    Getter method for prefix_limit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/l3vpn_ipv6_multicast/prefix_limit (container)

    YANG Description: Configure the maximum number of prefixes that will be
accepted from a peer
    """
    return self.__prefix_limit
      
  def _set_prefix_limit(self, v, load=False):
    """
    Setter method for prefix_limit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/l3vpn_ipv6_multicast/prefix_limit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_limit() directly.

    YANG Description: Configure the maximum number of prefixes that will be
accepted from a peer
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_limit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__prefix_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_limit(self):
    self.__prefix_limit = YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  prefix_limit = __builtin__.property(_get_prefix_limit, _set_prefix_limit)


  _pyangbind_elements = {'prefix_limit': prefix_limit, }


