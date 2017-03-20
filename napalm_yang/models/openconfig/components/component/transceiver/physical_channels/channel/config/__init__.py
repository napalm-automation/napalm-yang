
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
  from YANG module openconfig-platform - based on the path /components/component/transceiver/physical-channels/channel/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for physical channels
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__index','__description','__tx_laser','__target_output_power',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tx_laser = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tx-laser", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='boolean', is_config=True)
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='uint16', is_config=True)
    self.__target_output_power = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='decimal64', is_config=True)
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='string', is_config=True)

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
      return [u'components', u'component', u'transceiver', u'physical-channels', u'channel', u'config']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /components/component/transceiver/physical_channels/channel/config/index (uint16)

    YANG Description: Index of the physical channnel or lane within a physical
client port
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /components/component/transceiver/physical_channels/channel/config/index (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Index of the physical channnel or lane within a physical
client port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='uint16', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='uint16', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /components/component/transceiver/physical_channels/channel/config/description (string)

    YANG Description: Text description for the client physical channel
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /components/component/transceiver/physical_channels/channel/config/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: Text description for the client physical channel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='string', is_config=True)


  def _get_tx_laser(self):
    """
    Getter method for tx_laser, mapped from YANG variable /components/component/transceiver/physical_channels/channel/config/tx_laser (boolean)

    YANG Description: Enable (true) or disable (false) the transmit label for the
channel
    """
    return self.__tx_laser
      
  def _set_tx_laser(self, v, load=False):
    """
    Setter method for tx_laser, mapped from YANG variable /components/component/transceiver/physical_channels/channel/config/tx_laser (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_laser is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_laser() directly.

    YANG Description: Enable (true) or disable (false) the transmit label for the
channel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="tx-laser", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_laser must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tx-laser", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='boolean', is_config=True)""",
        })

    self.__tx_laser = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_laser(self):
    self.__tx_laser = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tx-laser", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='boolean', is_config=True)


  def _get_target_output_power(self):
    """
    Getter method for target_output_power, mapped from YANG variable /components/component/transceiver/physical_channels/channel/config/target_output_power (decimal64)

    YANG Description: Target output optical power level of the optical channel,
expressed in increments of 0.01 dBm (decibel-milliwats)
    """
    return self.__target_output_power
      
  def _set_target_output_power(self, v, load=False):
    """
    Setter method for target_output_power, mapped from YANG variable /components/component/transceiver/physical_channels/channel/config/target_output_power (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_output_power is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_output_power() directly.

    YANG Description: Target output optical power level of the optical channel,
expressed in increments of 0.01 dBm (decibel-milliwats)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='decimal64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_output_power must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='decimal64', is_config=True)""",
        })

    self.__target_output_power = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_output_power(self):
    self.__target_output_power = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='decimal64', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  description = __builtin__.property(_get_description, _set_description)
  tx_laser = __builtin__.property(_get_tx_laser, _set_tx_laser)
  target_output_power = __builtin__.property(_get_target_output_power, _set_target_output_power)


  _pyangbind_elements = {'index': index, 'description': description, 'tx_laser': tx_laser, 'target_output_power': target_output_power, }


