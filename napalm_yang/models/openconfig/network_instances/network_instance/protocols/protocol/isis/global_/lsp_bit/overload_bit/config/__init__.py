
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/lsp-bit/overload-bit/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS Overload Bit configuration.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__set_bit','__set_bit_on_boot','__advertise_high_metric',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__set_bit_on_boot = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit-on-boot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__advertise_high_metric = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-high-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__set_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'lsp-bit', u'overload-bit', u'config']

  def _get_set_bit(self):
    """
    Getter method for set_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/set_bit (boolean)

    YANG Description: When set to true, IS-IS overload bit is set.
    """
    return self.__set_bit
      
  def _set_set_bit(self, v, load=False):
    """
    Setter method for set_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/set_bit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_bit() directly.

    YANG Description: When set to true, IS-IS overload bit is set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_bit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__set_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_bit(self):
    self.__set_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_set_bit_on_boot(self):
    """
    Getter method for set_bit_on_boot, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/set_bit_on_boot (boolean)

    YANG Description: When set to true, the IS-IS overload bit is set on system boot.
    """
    return self.__set_bit_on_boot
      
  def _set_set_bit_on_boot(self, v, load=False):
    """
    Setter method for set_bit_on_boot, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/set_bit_on_boot (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_bit_on_boot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_bit_on_boot() directly.

    YANG Description: When set to true, the IS-IS overload bit is set on system boot.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit-on-boot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_bit_on_boot must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit-on-boot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__set_bit_on_boot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_bit_on_boot(self):
    self.__set_bit_on_boot = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit-on-boot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_advertise_high_metric(self):
    """
    Getter method for advertise_high_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/advertise_high_metric (boolean)

    YANG Description: When set to true, the local IS advertises links with the highest
available metric regardless of their configured metric. The metric
value is based on the metric style - if wide metrics are utilised
the metric is advertised as 16777214, otherwise they are advertised
with a value of 63.
    """
    return self.__advertise_high_metric
      
  def _set_advertise_high_metric(self, v, load=False):
    """
    Setter method for advertise_high_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/advertise_high_metric (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_advertise_high_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_advertise_high_metric() directly.

    YANG Description: When set to true, the local IS advertises links with the highest
available metric regardless of their configured metric. The metric
value is based on the metric style - if wide metrics are utilised
the metric is advertised as 16777214, otherwise they are advertised
with a value of 63.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-high-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """advertise_high_metric must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-high-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__advertise_high_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_advertise_high_metric(self):
    self.__advertise_high_metric = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-high-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  set_bit = __builtin__.property(_get_set_bit, _set_set_bit)
  set_bit_on_boot = __builtin__.property(_get_set_bit_on_boot, _set_set_bit_on_boot)
  advertise_high_metric = __builtin__.property(_get_advertise_high_metric, _set_advertise_high_metric)


  _pyangbind_elements = {'set_bit': set_bit, 'set_bit_on_boot': set_bit_on_boot, 'advertise_high_metric': advertise_high_metric, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/lsp-bit/overload-bit/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS Overload Bit configuration.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__set_bit','__set_bit_on_boot','__advertise_high_metric',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__set_bit_on_boot = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit-on-boot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__advertise_high_metric = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-high-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__set_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'lsp-bit', u'overload-bit', u'config']

  def _get_set_bit(self):
    """
    Getter method for set_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/set_bit (boolean)

    YANG Description: When set to true, IS-IS overload bit is set.
    """
    return self.__set_bit
      
  def _set_set_bit(self, v, load=False):
    """
    Setter method for set_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/set_bit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_bit() directly.

    YANG Description: When set to true, IS-IS overload bit is set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_bit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__set_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_bit(self):
    self.__set_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_set_bit_on_boot(self):
    """
    Getter method for set_bit_on_boot, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/set_bit_on_boot (boolean)

    YANG Description: When set to true, the IS-IS overload bit is set on system boot.
    """
    return self.__set_bit_on_boot
      
  def _set_set_bit_on_boot(self, v, load=False):
    """
    Setter method for set_bit_on_boot, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/set_bit_on_boot (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_bit_on_boot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_bit_on_boot() directly.

    YANG Description: When set to true, the IS-IS overload bit is set on system boot.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit-on-boot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_bit_on_boot must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit-on-boot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__set_bit_on_boot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_bit_on_boot(self):
    self.__set_bit_on_boot = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set-bit-on-boot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_advertise_high_metric(self):
    """
    Getter method for advertise_high_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/advertise_high_metric (boolean)

    YANG Description: When set to true, the local IS advertises links with the highest
available metric regardless of their configured metric. The metric
value is based on the metric style - if wide metrics are utilised
the metric is advertised as 16777214, otherwise they are advertised
with a value of 63.
    """
    return self.__advertise_high_metric
      
  def _set_advertise_high_metric(self, v, load=False):
    """
    Setter method for advertise_high_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit/config/advertise_high_metric (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_advertise_high_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_advertise_high_metric() directly.

    YANG Description: When set to true, the local IS advertises links with the highest
available metric regardless of their configured metric. The metric
value is based on the metric style - if wide metrics are utilised
the metric is advertised as 16777214, otherwise they are advertised
with a value of 63.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-high-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """advertise_high_metric must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-high-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__advertise_high_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_advertise_high_metric(self):
    self.__advertise_high_metric = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-high-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  set_bit = __builtin__.property(_get_set_bit, _set_set_bit)
  set_bit_on_boot = __builtin__.property(_get_set_bit_on_boot, _set_set_bit_on_boot)
  advertise_high_metric = __builtin__.property(_get_advertise_high_metric, _set_advertise_high_metric)


  _pyangbind_elements = {'set_bit': set_bit, 'set_bit_on_boot': set_bit_on_boot, 'advertise_high_metric': advertise_high_metric, }


