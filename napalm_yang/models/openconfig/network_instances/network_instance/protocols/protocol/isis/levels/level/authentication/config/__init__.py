
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/authentication/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS authentication configuration.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__csnp_authentication','__psnp_authentication','__lsp_authentication',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__csnp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="csnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__lsp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="lsp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__psnp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="psnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'authentication', u'config']

  def _get_csnp_authentication(self):
    """
    Getter method for csnp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/csnp_authentication (boolean)

    YANG Description: Enable or disable for IS-IS CSNPs.
    """
    return self.__csnp_authentication
      
  def _set_csnp_authentication(self, v, load=False):
    """
    Setter method for csnp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/csnp_authentication (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_csnp_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_csnp_authentication() directly.

    YANG Description: Enable or disable for IS-IS CSNPs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="csnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """csnp_authentication must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="csnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__csnp_authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_csnp_authentication(self):
    self.__csnp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="csnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_psnp_authentication(self):
    """
    Getter method for psnp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/psnp_authentication (boolean)

    YANG Description: Enable or disable authentication for IS-IS PSNPs.
    """
    return self.__psnp_authentication
      
  def _set_psnp_authentication(self, v, load=False):
    """
    Setter method for psnp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/psnp_authentication (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_psnp_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_psnp_authentication() directly.

    YANG Description: Enable or disable authentication for IS-IS PSNPs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="psnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """psnp_authentication must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="psnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__psnp_authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_psnp_authentication(self):
    self.__psnp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="psnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_lsp_authentication(self):
    """
    Getter method for lsp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/lsp_authentication (boolean)

    YANG Description: Enable or disable authentication for IS-IS LSPs.
    """
    return self.__lsp_authentication
      
  def _set_lsp_authentication(self, v, load=False):
    """
    Setter method for lsp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/lsp_authentication (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_authentication() directly.

    YANG Description: Enable or disable authentication for IS-IS LSPs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="lsp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_authentication must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="lsp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_authentication(self):
    self.__lsp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="lsp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  csnp_authentication = __builtin__.property(_get_csnp_authentication, _set_csnp_authentication)
  psnp_authentication = __builtin__.property(_get_psnp_authentication, _set_psnp_authentication)
  lsp_authentication = __builtin__.property(_get_lsp_authentication, _set_lsp_authentication)


  _pyangbind_elements = {'csnp_authentication': csnp_authentication, 'psnp_authentication': psnp_authentication, 'lsp_authentication': lsp_authentication, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/authentication/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS authentication configuration.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__csnp_authentication','__psnp_authentication','__lsp_authentication',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__csnp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="csnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__lsp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="lsp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__psnp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="psnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'authentication', u'config']

  def _get_csnp_authentication(self):
    """
    Getter method for csnp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/csnp_authentication (boolean)

    YANG Description: Enable or disable for IS-IS CSNPs.
    """
    return self.__csnp_authentication
      
  def _set_csnp_authentication(self, v, load=False):
    """
    Setter method for csnp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/csnp_authentication (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_csnp_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_csnp_authentication() directly.

    YANG Description: Enable or disable for IS-IS CSNPs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="csnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """csnp_authentication must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="csnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__csnp_authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_csnp_authentication(self):
    self.__csnp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="csnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_psnp_authentication(self):
    """
    Getter method for psnp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/psnp_authentication (boolean)

    YANG Description: Enable or disable authentication for IS-IS PSNPs.
    """
    return self.__psnp_authentication
      
  def _set_psnp_authentication(self, v, load=False):
    """
    Setter method for psnp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/psnp_authentication (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_psnp_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_psnp_authentication() directly.

    YANG Description: Enable or disable authentication for IS-IS PSNPs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="psnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """psnp_authentication must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="psnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__psnp_authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_psnp_authentication(self):
    self.__psnp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="psnp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_lsp_authentication(self):
    """
    Getter method for lsp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/lsp_authentication (boolean)

    YANG Description: Enable or disable authentication for IS-IS LSPs.
    """
    return self.__lsp_authentication
      
  def _set_lsp_authentication(self, v, load=False):
    """
    Setter method for lsp_authentication, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/authentication/config/lsp_authentication (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_authentication() directly.

    YANG Description: Enable or disable authentication for IS-IS LSPs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="lsp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_authentication must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="lsp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_authentication(self):
    self.__lsp_authentication = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="lsp-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  csnp_authentication = __builtin__.property(_get_csnp_authentication, _set_csnp_authentication)
  psnp_authentication = __builtin__.property(_get_psnp_authentication, _set_psnp_authentication)
  lsp_authentication = __builtin__.property(_get_lsp_authentication, _set_lsp_authentication)


  _pyangbind_elements = {'csnp_authentication': csnp_authentication, 'psnp_authentication': psnp_authentication, 'lsp_authentication': lsp_authentication, }


