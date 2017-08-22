
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
  from YANG module openconfig-system - based on the path /system/aaa/authentication/users/user/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for local users
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__username','__password','__password_hashed','__ssh_key','__role',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__username = YANGDynClass(base=unicode, is_leaf=True, yang_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    self.__password_hashed = YANGDynClass(base=unicode, is_leaf=True, yang_name="password-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    self.__password = YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    self.__role = YANGDynClass(base=[unicode,RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SYSTEM_ROLE_ADMIN': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:SYSTEM_ROLE_ADMIN': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),], is_leaf=True, yang_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=True)
    self.__ssh_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="ssh-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)

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
      return [u'system', u'aaa', u'authentication', u'users', u'user', u'config']

  def _get_username(self):
    """
    Getter method for username, mapped from YANG variable /system/aaa/authentication/users/user/config/username (string)

    YANG Description: Assigned username for this user
    """
    return self.__username
      
  def _set_username(self, v, load=False):
    """
    Setter method for username, mapped from YANG variable /system/aaa/authentication/users/user/config/username (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_username is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_username() directly.

    YANG Description: Assigned username for this user
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """username must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)""",
        })

    self.__username = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_username(self):
    self.__username = YANGDynClass(base=unicode, is_leaf=True, yang_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)


  def _get_password(self):
    """
    Getter method for password, mapped from YANG variable /system/aaa/authentication/users/user/config/password (string)

    YANG Description: The user password, supplied as cleartext.  The system
must hash the value and only store the hashed value.
    """
    return self.__password
      
  def _set_password(self, v, load=False):
    """
    Setter method for password, mapped from YANG variable /system/aaa/authentication/users/user/config/password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_password() directly.

    YANG Description: The user password, supplied as cleartext.  The system
must hash the value and only store the hashed value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)""",
        })

    self.__password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_password(self):
    self.__password = YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)


  def _get_password_hashed(self):
    """
    Getter method for password_hashed, mapped from YANG variable /system/aaa/authentication/users/user/config/password_hashed (oc-aaa-types:crypt-password-type)

    YANG Description: The user password, supplied as a hashed value
using the notation described in the definition of the
crypt-password-type.
    """
    return self.__password_hashed
      
  def _set_password_hashed(self, v, load=False):
    """
    Setter method for password_hashed, mapped from YANG variable /system/aaa/authentication/users/user/config/password_hashed (oc-aaa-types:crypt-password-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_password_hashed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_password_hashed() directly.

    YANG Description: The user password, supplied as a hashed value
using the notation described in the definition of the
crypt-password-type.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="password-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """password_hashed must be of a type compatible with oc-aaa-types:crypt-password-type""",
          'defined-type': "oc-aaa-types:crypt-password-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="password-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)""",
        })

    self.__password_hashed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_password_hashed(self):
    self.__password_hashed = YANGDynClass(base=unicode, is_leaf=True, yang_name="password-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)


  def _get_ssh_key(self):
    """
    Getter method for ssh_key, mapped from YANG variable /system/aaa/authentication/users/user/config/ssh_key (string)

    YANG Description: SSH public key for the user (RSA or DSA)
    """
    return self.__ssh_key
      
  def _set_ssh_key(self, v, load=False):
    """
    Setter method for ssh_key, mapped from YANG variable /system/aaa/authentication/users/user/config/ssh_key (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssh_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssh_key() directly.

    YANG Description: SSH public key for the user (RSA or DSA)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ssh-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssh_key must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ssh-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)""",
        })

    self.__ssh_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssh_key(self):
    self.__ssh_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="ssh-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)


  def _get_role(self):
    """
    Getter method for role, mapped from YANG variable /system/aaa/authentication/users/user/config/role (union)

    YANG Description: Role assigned to the user.  The role may be supplied
as a string or a role defined by the SYSTEM_DEFINED_ROLES
identity.
    """
    return self.__role
      
  def _set_role(self, v, load=False):
    """
    Setter method for role, mapped from YANG variable /system/aaa/authentication/users/user/config/role (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_role is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_role() directly.

    YANG Description: Role assigned to the user.  The role may be supplied
as a string or a role defined by the SYSTEM_DEFINED_ROLES
identity.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[unicode,RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SYSTEM_ROLE_ADMIN': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:SYSTEM_ROLE_ADMIN': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),], is_leaf=True, yang_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """role must be of a type compatible with union""",
          'defined-type': "openconfig-system:union",
          'generated-type': """YANGDynClass(base=[unicode,RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SYSTEM_ROLE_ADMIN': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:SYSTEM_ROLE_ADMIN': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),], is_leaf=True, yang_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=True)""",
        })

    self.__role = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_role(self):
    self.__role = YANGDynClass(base=[unicode,RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SYSTEM_ROLE_ADMIN': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:SYSTEM_ROLE_ADMIN': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),], is_leaf=True, yang_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=True)

  username = __builtin__.property(_get_username, _set_username)
  password = __builtin__.property(_get_password, _set_password)
  password_hashed = __builtin__.property(_get_password_hashed, _set_password_hashed)
  ssh_key = __builtin__.property(_get_ssh_key, _set_ssh_key)
  role = __builtin__.property(_get_role, _set_role)


  _pyangbind_elements = {'username': username, 'password': password, 'password_hashed': password_hashed, 'ssh_key': ssh_key, 'role': role, }


