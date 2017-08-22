
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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/confederation/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to BGP confederations
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__identifier','__member_as',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__member_as = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    self.__identifier = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="identifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'confederation', u'config']

  def _get_identifier(self):
    """
    Getter method for identifier, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/confederation/config/identifier (oc-inet:as-number)

    YANG Description: Confederation identifier for the autonomous system.
Setting the identifier indicates that the local-AS is part
of a BGP confederation.
    """
    return self.__identifier
      
  def _set_identifier(self, v, load=False):
    """
    Setter method for identifier, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/confederation/config/identifier (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_identifier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_identifier() directly.

    YANG Description: Confederation identifier for the autonomous system.
Setting the identifier indicates that the local-AS is part
of a BGP confederation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="identifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """identifier must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="identifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)""",
        })

    self.__identifier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_identifier(self):
    self.__identifier = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="identifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)


  def _get_member_as(self):
    """
    Getter method for member_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/confederation/config/member_as (oc-inet:as-number)

    YANG Description: Remote autonomous systems that are to be treated
as part of the local confederation.
    """
    return self.__member_as
      
  def _set_member_as(self, v, load=False):
    """
    Setter method for member_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/confederation/config/member_as (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_as() directly.

    YANG Description: Remote autonomous systems that are to be treated
as part of the local confederation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_as must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)""",
        })

    self.__member_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_as(self):
    self.__member_as = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)

  identifier = __builtin__.property(_get_identifier, _set_identifier)
  member_as = __builtin__.property(_get_member_as, _set_member_as)


  _pyangbind_elements = {'identifier': identifier, 'member_as': member_as, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/confederation/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to BGP confederations
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__identifier','__member_as',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__member_as = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    self.__identifier = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="identifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'confederation', u'config']

  def _get_identifier(self):
    """
    Getter method for identifier, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/confederation/config/identifier (oc-inet:as-number)

    YANG Description: Confederation identifier for the autonomous system.
Setting the identifier indicates that the local-AS is part
of a BGP confederation.
    """
    return self.__identifier
      
  def _set_identifier(self, v, load=False):
    """
    Setter method for identifier, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/confederation/config/identifier (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_identifier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_identifier() directly.

    YANG Description: Confederation identifier for the autonomous system.
Setting the identifier indicates that the local-AS is part
of a BGP confederation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="identifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """identifier must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="identifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)""",
        })

    self.__identifier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_identifier(self):
    self.__identifier = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="identifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)


  def _get_member_as(self):
    """
    Getter method for member_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/confederation/config/member_as (oc-inet:as-number)

    YANG Description: Remote autonomous systems that are to be treated
as part of the local confederation.
    """
    return self.__member_as
      
  def _set_member_as(self, v, load=False):
    """
    Setter method for member_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/confederation/config/member_as (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_as() directly.

    YANG Description: Remote autonomous systems that are to be treated
as part of the local confederation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_as must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)""",
        })

    self.__member_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_as(self):
    self.__member_as = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)

  identifier = __builtin__.property(_get_identifier, _set_identifier)
  member_as = __builtin__.property(_get_member_as, _set_member_as)


  _pyangbind_elements = {'identifier': identifier, 'member_as': member_as, }


