
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interface_ref
class member(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-vlan - based on the path /vlans/vlan/members/member. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of references to interfaces / subinterfaces
associated with the VLAN.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_ref',)

  _yang_name = 'member'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=False)

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
      return [u'vlans', u'vlan', u'members', u'member']

  def _get_interface_ref(self):
    """
    Getter method for interface_ref, mapped from YANG variable /vlans/vlan/members/member/interface_ref (container)

    YANG Description: Reference to an interface or subinterface
    """
    return self.__interface_ref
      
  def _set_interface_ref(self, v, load=False):
    """
    Setter method for interface_ref, mapped from YANG variable /vlans/vlan/members/member/interface_ref (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ref() directly.

    YANG Description: Reference to an interface or subinterface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ref must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=False)""",
        })

    self.__interface_ref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ref(self):
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=False)

  interface_ref = __builtin__.property(_get_interface_ref)


  _pyangbind_elements = {'interface_ref': interface_ref, }


