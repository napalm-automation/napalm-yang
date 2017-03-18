
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import subinterface
class subinterfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of subinterfaces associated
with a physical interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__subinterface',)

  _yang_name = 'subinterfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

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
      return [u'interfaces', u'interface', u'subinterfaces']

  def _get_subinterface(self):
    """
    Getter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    return self.__subinterface
      
  def _set_subinterface(self, v, load=False):
    """
    Setter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subinterface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subinterface() directly.

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subinterface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)""",
        })

    self.__subinterface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subinterface(self):
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

  subinterface = __builtin__.property(_get_subinterface, _set_subinterface)


  _pyangbind_elements = {'subinterface': subinterface, }


import subinterface
class subinterfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of subinterfaces associated
with a physical interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__subinterface',)

  _yang_name = 'subinterfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

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
      return [u'interfaces', u'interface', u'subinterfaces']

  def _get_subinterface(self):
    """
    Getter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    return self.__subinterface
      
  def _set_subinterface(self, v, load=False):
    """
    Setter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subinterface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subinterface() directly.

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subinterface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)""",
        })

    self.__subinterface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subinterface(self):
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

  subinterface = __builtin__.property(_get_subinterface, _set_subinterface)


  _pyangbind_elements = {'subinterface': subinterface, }


import subinterface
class subinterfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of subinterfaces associated
with a physical interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__subinterface',)

  _yang_name = 'subinterfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

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
      return [u'interfaces', u'interface', u'subinterfaces']

  def _get_subinterface(self):
    """
    Getter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    return self.__subinterface
      
  def _set_subinterface(self, v, load=False):
    """
    Setter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subinterface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subinterface() directly.

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subinterface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)""",
        })

    self.__subinterface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subinterface(self):
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

  subinterface = __builtin__.property(_get_subinterface, _set_subinterface)


  _pyangbind_elements = {'subinterface': subinterface, }


import subinterface
class subinterfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of subinterfaces associated
with a physical interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__subinterface',)

  _yang_name = 'subinterfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

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
      return [u'interfaces', u'interface', u'subinterfaces']

  def _get_subinterface(self):
    """
    Getter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    return self.__subinterface
      
  def _set_subinterface(self, v, load=False):
    """
    Setter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subinterface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subinterface() directly.

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subinterface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)""",
        })

    self.__subinterface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subinterface(self):
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

  subinterface = __builtin__.property(_get_subinterface, _set_subinterface)


  _pyangbind_elements = {'subinterface': subinterface, }


import subinterface
class subinterfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of subinterfaces associated
with a physical interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__subinterface',)

  _yang_name = 'subinterfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

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
      return [u'interfaces', u'interface', u'subinterfaces']

  def _get_subinterface(self):
    """
    Getter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    return self.__subinterface
      
  def _set_subinterface(self, v, load=False):
    """
    Setter method for subinterface, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subinterface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subinterface() directly.

    YANG Description: The list of subinterfaces (logical interfaces) associated
with a physical interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subinterface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)""",
        })

    self.__subinterface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subinterface(self):
    self.__subinterface = YANGDynClass(base=YANGListType("index",subinterface.subinterface, yang_name="subinterface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='list', is_config=True)

  subinterface = __builtin__.property(_get_subinterface, _set_subinterface)


  _pyangbind_elements = {'subinterface': subinterface, }


