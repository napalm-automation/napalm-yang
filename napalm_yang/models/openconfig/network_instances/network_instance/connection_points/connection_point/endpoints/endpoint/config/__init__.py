
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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the
endpoint
  """
  __slots__ = ('_path_helper', '_extmethods', '__endpoint_id','__precedence','__type',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    self.__precedence = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    self.__endpoint_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

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
      return [u'network-instances', u'network-instance', u'connection-points', u'connection-point', u'endpoints', u'endpoint', u'config']

  def _get_endpoint_id(self):
    """
    Getter method for endpoint_id, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/endpoint_id (string)

    YANG Description: An identifier for the endpoint
    """
    return self.__endpoint_id
      
  def _set_endpoint_id(self, v, load=False):
    """
    Setter method for endpoint_id, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/endpoint_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint_id() directly.

    YANG Description: An identifier for the endpoint
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__endpoint_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint_id(self):
    self.__endpoint_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)


  def _get_precedence(self):
    """
    Getter method for precedence, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/precedence (uint16)

    YANG Description: The precedence of the endpoint - the lowest precendence
viable endpoint will be utilised as the active endpoint
within a connection
    """
    return self.__precedence
      
  def _set_precedence(self, v, load=False):
    """
    Setter method for precedence, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/precedence (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_precedence is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_precedence() directly.

    YANG Description: The precedence of the endpoint - the lowest precendence
viable endpoint will be utilised as the active endpoint
within a connection
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """precedence must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)""",
        })

    self.__precedence = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_precedence(self):
    self.__precedence = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/type (identityref)

    YANG Description: The type of endpoint that is referred to by the current
endpoint
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of endpoint that is referred to by the current
endpoint
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)

  endpoint_id = __builtin__.property(_get_endpoint_id, _set_endpoint_id)
  precedence = __builtin__.property(_get_precedence, _set_precedence)
  type = __builtin__.property(_get_type, _set_type)


  _pyangbind_elements = OrderedDict([('endpoint_id', endpoint_id), ('precedence', precedence), ('type', type), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the
endpoint
  """
  __slots__ = ('_path_helper', '_extmethods', '__endpoint_id','__precedence','__type',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    self.__precedence = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    self.__endpoint_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

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
      return [u'network-instances', u'network-instance', u'connection-points', u'connection-point', u'endpoints', u'endpoint', u'config']

  def _get_endpoint_id(self):
    """
    Getter method for endpoint_id, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/endpoint_id (string)

    YANG Description: An identifier for the endpoint
    """
    return self.__endpoint_id
      
  def _set_endpoint_id(self, v, load=False):
    """
    Setter method for endpoint_id, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/endpoint_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint_id() directly.

    YANG Description: An identifier for the endpoint
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__endpoint_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint_id(self):
    self.__endpoint_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)


  def _get_precedence(self):
    """
    Getter method for precedence, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/precedence (uint16)

    YANG Description: The precedence of the endpoint - the lowest precendence
viable endpoint will be utilised as the active endpoint
within a connection
    """
    return self.__precedence
      
  def _set_precedence(self, v, load=False):
    """
    Setter method for precedence, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/precedence (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_precedence is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_precedence() directly.

    YANG Description: The precedence of the endpoint - the lowest precendence
viable endpoint will be utilised as the active endpoint
within a connection
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """precedence must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)""",
        })

    self.__precedence = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_precedence(self):
    self.__precedence = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/type (identityref)

    YANG Description: The type of endpoint that is referred to by the current
endpoint
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config/type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of endpoint that is referred to by the current
endpoint
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:REMOTE': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)

  endpoint_id = __builtin__.property(_get_endpoint_id, _set_endpoint_id)
  precedence = __builtin__.property(_get_precedence, _set_precedence)
  type = __builtin__.property(_get_type, _set_type)


  _pyangbind_elements = OrderedDict([('endpoint_id', endpoint_id), ('precedence', precedence), ('type', type), ])


